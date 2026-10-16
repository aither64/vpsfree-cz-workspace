specialMount "none" "/" "x-initrd.mount" "tmpfs"

specialMount "devtmpfs" "/dev" "nosuid,strictatime,mode=755,size=5%" "devtmpfs"

specialMount "devpts" "/dev/pts" "nosuid,noexec,mode=620,ptmxmode=0666,gid=3" "devpts"

specialMount "tmpfs" "/dev/shm" "nosuid,nodev,strictatime,mode=1777,size=50%" "tmpfs"

specialMount "/fixture/host storage" "/fixture/backing storage" "x-initrd.mount,rbind" "none"

specialMount "/fixture/backing storage/bridge" "/fixture/bridge" "x-initrd.mount,bind" "none"

specialMount "proc" "/proc" "nosuid,noexec,nodev" "proc"

specialMount "tmpfs" "/run" "nosuid,nodev,strictatime,mode=755,size=25%" "tmpfs"

specialMount "tmpfs" "/run/keys" "nosuid,nodev,mode=750" "tmpfs"

specialMount "/fixture/bridge/state" "/var/lib/nixos" "x-initrd.mount,bind,x-gvfs-hide" "auto"
