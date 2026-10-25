# Native Ruby locale in isolated launchers

An environment assembled only from Nix tool exports can omit the successful outer driver's explicit locale. This selected Ruby then used US-ASCII for File.read, and JSON 3.1.0 rejected an accented saved-description fixture. No application or dependency change caused the failure.

Retain the proven ordinary `LANG=C.UTF-8` and `LC_ALL=C.UTF-8` controls when isolating the environment. The same Ruby/JSON/native libc control reproduced the omitted-locale failure and parsed identical UTF-8 bytes with those two controls; no locale archive or download was needed. Bind the native libc and preserve the failed attempt.

The distinct corrected successor execution passed Go23 and Rust82 without changing source, probes, oracles, constraints or installed homes. See proof.json and ../actual-pair-1/result.json versus ../actual-pair-2/result.json.
