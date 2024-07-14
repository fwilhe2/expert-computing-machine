#!/bin/bash

# Assuming you have bzImage and rootfs.ext4 in pwd, this should bring up a vm with a shell

qemu-system-x86_64 \
	-cpu "Broadwell-v1" \
	-enable-kvm \
	-m 2G \
	-smp 2 \
	-kernel ./bzImage \
	-append "rw console=ttyS0 init=/myinit root=/dev/sda earlyprintk=serial net.ifnames=0 systemd.journald.forward_to_console=1" \
	-drive file=rootfs.ext4,format=raw \
	-net user,host=10.0.2.10,hostfwd=tcp:127.0.0.1:10021-:22 \
	-net nic,model=e1000 \
	-nographic
