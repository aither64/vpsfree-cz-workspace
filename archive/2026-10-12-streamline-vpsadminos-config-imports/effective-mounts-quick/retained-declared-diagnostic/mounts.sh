specialMount "/fixture/host storage" "/fixture/backing storage" "x-initrd.mount,bind" "none"
specialMount "/fixture/backing storage/nixos" "/var/lib/nixos" "bind,x-gvfs-hide" "none"
specialMount "/fixture/backing storage/log" "/var/log" "bind,x-gvfs-hide" "none"
