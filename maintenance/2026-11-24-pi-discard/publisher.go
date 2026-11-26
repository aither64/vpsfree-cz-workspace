//go:build linux && amd64

// The dated publisher is a root-only transport. The selected portal, not this
// program, validates live ownership and executes the exact discard transaction.
package main

import (
	"bytes"
	"crypto/rand"
	"encoding/hex"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"os"
	"os/user"
	"path/filepath"
	"regexp"
	"strconv"
	"strings"
	"syscall"
	"unicode/utf8"
	"unsafe"
)

const dirName = "dev-workspace-pi-discard"
const grantName = "startup-grant.json"
const lockName = ".dev-workspace-pi-discard.lock"
const portalGroup = "workspace-portal-owner"
const limit = 8192
const dirs = syscall.O_DIRECTORY | syscall.O_RDONLY | syscall.O_NOFOLLOW | syscall.O_CLOEXEC

var refused = errors.New("grant refused or not confirmed")

var storePath = regexp.MustCompile(`^/nix/store/[0-9abcdfghijklmnpqrsvwxyz]{32}-[A-Za-z0-9+._?=-]+$`)
var profileToken = regexp.MustCompile(`^pi-profile-v1:[0-9a-f]{64}$`)
var slug = regexp.MustCompile(`^[A-Za-z0-9][A-Za-z0-9_-]*$`)
var uuid = regexp.MustCompile(`^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$`)
var digest = regexp.MustCompile(`^[0-9a-f]{64}$`)

// Parse the exact case-sensitive field sets. Decoding directly into structs
// accepts case-folded keys and can collapse repeated or null-valued fields.
func object(data []byte, keys ...string) (map[string]json.RawMessage, bool) {
	d := json.NewDecoder(bytes.NewReader(data))
	if tok, err := d.Token(); err != nil || tok != json.Delim('{') {
		return nil, false
	}
	fields := make(map[string]json.RawMessage, len(keys))
	for d.More() {
		tok, err := d.Token()
		key, ok := tok.(string)
		if err != nil || !ok || len(fields) == len(keys) || fields[key] != nil {
			return nil, false
		}
		var value json.RawMessage
		if d.Decode(&value) != nil || bytes.Equal(value, []byte("null")) {
			return nil, false
		}
		fields[key] = value
	}
	if tok, err := d.Token(); err != nil || tok != json.Delim('}') || len(fields) != len(keys) {
		return nil, false
	}
	if _, err := d.Token(); err != io.EOF {
		return nil, false
	}
	for _, key := range keys {
		if fields[key] == nil {
			return nil, false
		}
	}
	return fields, true
}

func text(fields map[string]json.RawMessage, key string) string {
	var value string
	if json.Unmarshal(fields[key], &value) != nil {
		return ""
	}
	return value
}

func positive(data []byte) bool {
	var n int
	return json.Unmarshal(data, &n) == nil && n > 0
}

func validGrant(data []byte) bool {
	if len(data) > limit || !utf8.Valid(data) {
		return false
	}
	g, ok := object(data, "schema", "system", "package", "profileToken", "workspaceName", "workspaceRoot", "service", "owner", "claim", "target")
	if !ok || string(g["schema"]) != "1" {
		return false
	}
	name, root := text(g, "workspaceName"), text(g, "workspaceRoot")
	if !storePath.MatchString(text(g, "system")) || !storePath.MatchString(text(g, "package")) || !profileToken.MatchString(text(g, "profileToken")) ||
		!slug.MatchString(name) || !filepath.IsAbs(root) || filepath.Clean(root) != root || strings.ContainsAny(root, "\x00\uFFFD") ||
		text(g, "service") != "workspace-portal@"+name+".service" {
		return false
	}
	o, ok := object(g["owner"], "id", "slug")
	if !ok || !uuid.MatchString(text(o, "id")) || !slug.MatchString(text(o, "slug")) {
		return false
	}
	c, ok := object(g["claim"], "id", "repository", "selector", "adapter")
	selector := text(c, "selector")
	if !ok || !uuid.MatchString(text(c, "id")) || !slug.MatchString(text(c, "repository")) ||
		selector == "" || strings.ContainsAny(selector, "\x00\uFFFD") || !slug.MatchString(text(c, "adapter")) {
		return false
	}
	t, ok := object(g["target"], "requestId", "receiptId", "preparationAttempt", "creationAttempt", "slug", "incarnation", "epoch")
	return ok && uuid.MatchString(text(t, "requestId")) && digest.MatchString(text(t, "receiptId")) &&
		positive(t["preparationAttempt"]) && positive(t["creationAttempt"]) && slug.MatchString(text(t, "slug")) &&
		digest.MatchString(text(t, "incarnation")) && digest.MatchString(text(t, "epoch"))
}

func parent() (int, error) {
	fd, err := syscall.Open("/", dirs, 0)
	if err != nil {
		return -1, err
	}
	for _, component := range []string{"", "var", "lib"} {
		if component != "" {
			next, err := syscall.Openat(fd, component, dirs, 0)
			syscall.Close(fd)
			if err != nil {
				return -1, err
			}
			fd = next
		}
		var st syscall.Stat_t
		if syscall.Fstat(fd, &st) != nil || st.Uid != 0 || st.Mode&0022 != 0 {
			syscall.Close(fd)
			return -1, refused
		}
	}
	return fd, nil
}

func tempName() string {
	var random [16]byte
	rand.Read(random[:])
	return ".pi-discard-" + hex.EncodeToString(random[:])
}

// Linux amd64 renameat2(2) with RENAME_NOREPLACE. No fallback to overwrite
// or a hard-link intermediate (which would violate the reader's nlink=1).
func renameNoReplace(srcDir int, src string, dstDir int, dst string) error {
	from, _ := syscall.BytePtrFromString(src)
	to, _ := syscall.BytePtrFromString(dst)
	const sysRenameat2 = 316
	_, _, errno := syscall.Syscall6(sysRenameat2, uintptr(srcDir), uintptr(unsafe.Pointer(from)), uintptr(dstDir), uintptr(unsafe.Pointer(to)), 1, 0)
	if errno != 0 {
		return errno
	}
	return nil
}

func removeTempDir(parent int, name string) {
	p, _ := syscall.BytePtrFromString(name)
	const atRemovedir = 0x200
	syscall.Syscall(syscall.SYS_UNLINKAT, uintptr(parent), uintptr(unsafe.Pointer(p)), atRemovedir)
}

func lockParent(parent int) (int, error) {
	fd, err := syscall.Openat(parent, lockName, syscall.O_RDWR|syscall.O_CREAT|syscall.O_NOFOLLOW|syscall.O_NONBLOCK|syscall.O_CLOEXEC, 0600)
	if err != nil {
		return -1, err
	}
	var st syscall.Stat_t
	if syscall.Fstat(fd, &st) != nil || st.Mode != syscall.S_IFREG|0600 || st.Uid != 0 || st.Nlink != 1 || st.Size != 0 ||
		syscall.Flock(fd, syscall.LOCK_EX|syscall.LOCK_NB) != nil {
		syscall.Close(fd)
		return -1, refused
	}
	return fd, nil
}

// Refuse extended POSIX ACLs, including inherited ones. Group bits alone
// might encode a mask while named users actually have access.
func noACL(fd int, directory bool) bool {
	names := []string{"system.posix_acl_access"}
	if directory {
		names = append(names, "system.posix_acl_default")
	}
	for _, name := range names {
		p, _ := syscall.BytePtrFromString(name)
		_, _, err := syscall.Syscall6(syscall.SYS_FGETXATTR, uintptr(fd), uintptr(unsafe.Pointer(p)), 0, 0, 0, 0)
		if err != syscall.ENODATA && err != syscall.ENOTSUP {
			return false
		}
	}
	return true
}

// Build the dedicated directory with correct metadata before publishing its
// name. A crash cannot strand a partially configured authoritative parent.
func createDir(parent, gid int) error {
	name := tempName()
	if err := syscall.Mkdirat(parent, name, 0700); err != nil {
		return err
	}
	defer removeTempDir(parent, name)
	fd, err := syscall.Openat(parent, name, dirs, 0)
	if err != nil {
		return err
	}
	defer syscall.Close(fd)
	if !noACL(fd, true) || syscall.Fchown(fd, 0, gid) != nil || syscall.Fchmod(fd, 0750) != nil || syscall.Fsync(fd) != nil {
		return refused
	}
	if err := renameNoReplace(parent, name, parent, dirName); err != nil {
		return err
	}
	return syscall.Fsync(parent)
}

func sameGrant(dir, gid int, input []byte) (bool, error) {
	fd, err := syscall.Openat(dir, grantName, syscall.O_RDONLY|syscall.O_NOFOLLOW|syscall.O_NONBLOCK|syscall.O_CLOEXEC, 0)
	if errors.Is(err, syscall.ENOENT) {
		return false, nil
	}
	if err != nil {
		return false, err
	}
	f := os.NewFile(uintptr(fd), grantName)
	defer f.Close()
	var st syscall.Stat_t
	if syscall.Fstat(fd, &st) != nil || st.Mode != syscall.S_IFREG|0440 || st.Uid != 0 || st.Gid != uint32(gid) ||
		st.Nlink != 1 || st.Size != int64(len(input)) || !noACL(fd, false) {
		return false, refused
	}
	data, err := io.ReadAll(io.LimitReader(f, limit+1))
	if err != nil || !bytes.Equal(data, input) || f.Sync() != nil {
		return false, refused
	}
	return true, nil
}

func publish(dir, gid int, data []byte) error {
	// No group-readable grant bytes until the authoritative rename. A crash
	// can leave an inert random staging name, still private to root.
	name := tempName()
	if err := syscall.Mkdirat(dir, name, 0700); err != nil {
		return err
	}
	defer removeTempDir(dir, name)
	stage, err := syscall.Openat(dir, name, dirs, 0)
	if err != nil {
		return err
	}
	defer syscall.Close(stage)
	fd, err := syscall.Openat(stage, grantName, syscall.O_WRONLY|syscall.O_CREAT|syscall.O_EXCL|syscall.O_NOFOLLOW|syscall.O_CLOEXEC, 0600)
	if err != nil {
		return err
	}
	defer syscall.Unlinkat(stage, grantName)
	f := os.NewFile(uintptr(fd), name)
	defer f.Close()
	written, err := f.Write(data)
	if err != nil || written != len(data) || syscall.Fchown(fd, 0, gid) != nil || syscall.Fchmod(fd, 0440) != nil || f.Sync() != nil || f.Close() != nil {
		return refused
	}
	if err := renameNoReplace(stage, grantName, dir, grantName); err != nil {
		return err
	}
	return syscall.Fsync(stage)
}

func operation(parent, gid int, verb string, data []byte) (string, error) {
	lock, err := lockParent(parent)
	if err != nil {
		return "", err
	}
	defer syscall.Close(lock)
	dir, err := syscall.Openat(parent, dirName, dirs, 0)
	if errors.Is(err, syscall.ENOENT) {
		if verb == "retire" {
			return "absent", syscall.Fsync(parent)
		}
		if err := createDir(parent, gid); err != nil {
			return "", err
		}
		dir, err = syscall.Openat(parent, dirName, dirs, 0)
	}
	if err != nil {
		return "", err
	}
	defer syscall.Close(dir)
	var st syscall.Stat_t
	if syscall.Fstat(dir, &st) != nil || st.Uid != 0 || st.Gid != uint32(gid) || st.Mode&07777 != 0750 ||
		!noACL(dir, true) || syscall.Fsync(parent) != nil {
		return "", refused
	}
	present, err := sameGrant(dir, gid, data)
	if err != nil {
		return "", err
	}
	if verb == "publish" {
		if present {
			return "present", syscall.Fsync(dir)
		}
		if err := publish(dir, gid, data); err != nil {
			return "", err
		}
		return "published", syscall.Fsync(dir)
	}
	if !present {
		return "absent", syscall.Fsync(dir)
	}
	if syscall.Unlinkat(dir, grantName) != nil || syscall.Fsync(dir) != nil {
		return "", refused
	}
	if stillPresent, err := sameGrant(dir, gid, data); err != nil || stillPresent {
		return "", refused
	}
	return "retired", nil
}

func run() (string, error) {
	if os.Getuid() != 0 || os.Geteuid() != 0 || len(os.Args) != 2 || (os.Args[1] != "publish" && os.Args[1] != "retire") {
		return "", refused
	}
	data, err := io.ReadAll(io.LimitReader(os.Stdin, limit+1))
	if err != nil || !validGrant(data) {
		return "", refused
	}
	group, err := user.LookupGroup(portalGroup)
	if err != nil {
		return "", refused
	}
	gid, err := strconv.ParseUint(group.Gid, 10, 31)
	if err != nil || gid == 0 {
		return "", refused
	}
	fd, err := parent()
	if err != nil {
		return "", err
	}
	defer syscall.Close(fd)
	syscall.Umask(0077)
	return operation(fd, int(gid), os.Args[1], data)
}

func main() {
	status, err := run()
	if err != nil {
		fmt.Fprintln(os.Stderr, "pi-discard-grant: grant refused or not confirmed")
		os.Exit(1)
	}
	fmt.Println(status)
}
