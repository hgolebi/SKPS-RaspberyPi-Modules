#!/bin/bash
qemu-system-aarch64 -M virt \
-kernel Image  \
-m 1024 -smp 2 -cpu cortex-a53 \
-no-reboot -nographic  \
-device virtio-net-pci  \
-netdev user,id=net1,hostfwd=udp::8080-:8080 \
-device virtio-net-pci,netdev=net1  \
-drive file=root.ext4,if=virtio,format=raw  -append "root=/dev/vda"
