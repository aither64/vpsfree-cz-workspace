# Delayed kobject release requires timer object debugging

For the NFS cancellation diagnostic kernel, enabling DEBUG_KOBJECT_RELEASE
alone made the Nix Linux configuration builder fail with `unused option:
DEBUG_KOBJECT_RELEASE` before compilation. Linux 6.12 Kconfig depends on
DEBUG_OBJECTS_TIMERS, which depends on DEBUG_OBJECTS. Set both explicitly in
structuredExtraConfig; DEBUG_KOBJECT controls logging and is not this dependency.

Related initiative: work/2026-09-12-nfs-cancellation. The corrected configuration
is being built; runtime diagnostic results belong in the initiative state.
