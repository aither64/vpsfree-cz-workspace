# Evaluated mail configuration

Source head: `e4c1ac0c5ae7426fb019b79ba936b30ce63e6e6c`.
Generated derivation text, inspected without building or running the system.
These are configured values, not observed service behavior.
Trailing whitespace is omitted from the displayed derivation snippets.

## Postfix main.cf

Derivation: `/nix/store/g3915x66jgrvpzvx5s4y6x6sdlvj8xi0-postfix-main.cf.drv`.

```text
alias_maps =
  hash:/etc/postfix/aliases
command_directory = /nix/store/lw3m90dv2gj83azq1ngvgl1r5prw3131-postfix-3.11.7/bin
compatibility_level = 3.11.7
daemon_directory = /nix/store/lw3m90dv2gj83azq1ngvgl1r5prw3131-postfix-3.11.7/libexec/postfix
data_directory = /var/lib/postfix/data
default_privs = nobody
html_directory = /nix/store/lw3m90dv2gj83azq1ngvgl1r5prw3131-postfix-3.11.7/share/postfix/doc/html
mail_owner = postfix
mail_spool_directory = /var/spool/mail/
mailq_path = /nix/store/lw3m90dv2gj83azq1ngvgl1r5prw3131-postfix-3.11.7/bin/mailq
manpage_directory = /nix/store/lw3m90dv2gj83azq1ngvgl1r5prw3131-postfix-3.11.7/share/man
message_size_limit = 10240000
meta_directory = /nix/store/lw3m90dv2gj83azq1ngvgl1r5prw3131-postfix-3.11.7/etc/postfix
milter_default_action = accept
mydestination =
  $myhostname,
  localhost.$mydomain,
  localhost
mynetworks_style = host
newaliases_path = /nix/store/lw3m90dv2gj83azq1ngvgl1r5prw3131-postfix-3.11.7/bin/newaliases
queue_directory = /var/lib/postfix/queue
readme_directory = no
recipient_delimiter =
relay_domains =

relayhost =

sample_directory = /etc/postfix
sendmail_path = /nix/store/lw3m90dv2gj83azq1ngvgl1r5prw3131-postfix-3.11.7/bin/sendmail
setgid_group = postdrop
shlib_directory = no
smtp_tls_CAfile = /nix/store/ngnbakidj612mzmkblzs4wf94x054f0c-nss-cacert-3.126/etc/ssl/certs/ca-bundle.crt
smtp_tls_security_level = may
smtpd_milters = inet:localhost:11332
smtpd_recipient_restrictions =
  permit_mynetworks,
  permit_sasl_authenticated,
  reject_unauth_pipelining,
  reject_non_fqdn_recipient,
  reject_unknown_recipient_domain,
  reject_unauth_destination,
  reject_unlisted_recipient,
  check_policy_service unix:/run/postgrey.sock,
  reject_rbl_client zen.spamhaus.org=127.0.0.[2..11],
  reject_rbl_client b.barracudacentral.org=127.0.0.2
smtpd_tls_chain_files =

smtpd_tls_security_level = none
transport_maps =
  hash:/etc/postfix/transport
```

## Postfix master.cf

Derivation: `/nix/store/g37bv85dz879rac5f2wx2vwz4lxbbw6g-postfix-master.cf.drv`.

```text
# ==================================================================================
# service   type  private  unpriv  chroot  wakeup   maxproc  command + args
#                 (yes)    (yes)   (no)    (never)  (100)
# ==================================================================================
anvil       unix  -        -       -       -        1        anvil
bounce      unix  -        -       -       -        0        bounce
cleanup     unix  n        -       -       -        0        cleanup
defer       unix  -        -       -       -        0        bounce
discard     unix  -        -       -       -        -        discard
error       unix  -        -       -       -        -        error
flush       unix  n        -       -       1000?    0        flush
lmtp        unix  -        -       -       -        -        lmtp
local       unix  -        n       -       -        -        local
pickup      unix  n        -       -       60       1        pickup
proxymap    unix  -        -       -       -        -        proxymap
proxywrite  unix  -        -       -       -        1        proxymap
qmgr        unix  n        -       -       300      1        qmgr
relay       unix  -        -       -       -        -        smtp
  -o smtp_fallback_relay=
retry       unix  -        -       -       -        -        error
rewrite     unix  -        -       -       -        -        trivial-rewrite
scache      unix  -        -       -       -        1        scache
showq       unix  n        -       -       -        -        showq
smtp        unix  -        -       -       -        -        smtp
smtp        inet  n        -       -       -        -        smtpd
tlsmgr      unix  -        -       -       1000?    1        tlsmgr
trace       unix  -        -       -       -        0        bounce
verify      unix  -        -       -       -        1        verify
virtual     unix  -        n       -       -        -        virtual

```

## Postgrey service

Derivation: `/nix/store/6zpa7r4wpixn4h3qr92f478mcahak3ic-unit-postgrey.service.drv`.

```text
[Unit]
Before=postfix.service
Description=Postfix Greylisting Service

[Service]
Environment="LOCALE_ARCHIVE=/nix/store/dc427sjs33dci797apv4lvsg1a69szn0-glibc-locales-2.42-100/lib/locale/locale-archive"
Environment="PATH=/nix/store/bhv6xyvqw6gjs3j488gi1z6wdv18bdpa-coreutils-9.11/bin:/nix/store/nl0wq6d4bpjrxmlax141liq0qr9z87gn-findutils-4.10.0/bin:/nix/store/cqhgy07rpxdwk9kd2qlc3cw4s9ajzm9f-gnugrep-3.12/bin:/nix/store/0s17nja4n8b63by0nlg1m31mxn2bq1g1-gnused-4.10/bin:/nix/store/kmzlca218j6j1ar292fxj7707qzypij8-systemd-260.5/bin:/nix/store/bhv6xyvqw6gjs3j488gi1z6wdv18bdpa-coreutils-9.11/sbin:/nix/store/nl0wq6d4bpjrxmlax141liq0qr9z87gn-findutils-4.10.0/sbin:/nix/store/cqhgy07rpxdwk9kd2qlc3cw4s9ajzm9f-gnugrep-3.12/sbin:/nix/store/0s17nja4n8b63by0nlg1m31mxn2bq1g1-gnused-4.10/sbin:/nix/store/kmzlca218j6j1ar292fxj7707qzypij8-systemd-260.5/sbin"
Environment="TZDIR=/nix/store/mkbbamycmw838fwxk21jz0nw3mhnmk16-tzdata-2026c/share/zoneinfo"
ExecStart=/nix/store/7vl6j7957fz8l073ssbs34hvaafy5chf-postgrey-1.37/bin/postgrey \
          --unix=/run/postgrey.sock --socketmode=0777 \
          --group=postgrey --user=postgrey \
          --dbdir=/var/postgrey \
          --delay=300 \
          --max-age=35 \
          --retry-window=2 \
          --lookup-by-subnet \
          --ipv4cidr=24 --ipv6cidr=64 \
          --privacy \
          --auto-whitelist-clients=5 \
          --greylist-action=DEFER_IF_PERMIT \
          --greylist-text="Greylisted for %%s seconds" \
          --x-greylist-header="X-Greylist: delayed %%t seconds by postgrey-%%v at %%h; %%d" \
           \


ExecStartPre=/nix/store/bhv6xyvqw6gjs3j488gi1z6wdv18bdpa-coreutils-9.11/bin/mkdir -p /var/postgrey
ExecStartPre=/nix/store/bhv6xyvqw6gjs3j488gi1z6wdv18bdpa-coreutils-9.11/bin/chown postgrey:postgrey /var/postgrey
ExecStartPre=/nix/store/bhv6xyvqw6gjs3j488gi1z6wdv18bdpa-coreutils-9.11/bin/chmod 0770 /var/postgrey
Restart=always
RestartSec=5
TimeoutSec=10
Type=simple

[Install]
WantedBy=multi-user.target

```
