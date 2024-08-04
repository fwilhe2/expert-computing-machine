#!/bin/bash

apko --log-level debug build-minirootfs os.yaml rootfs.tgz
mkdir -p rootfs
sudo tar xzf rootfs.tgz -C rootfs
sudo /sbin/mkfs.ext4 -L root -d ./rootfs/ rootfs.ext4 2G
