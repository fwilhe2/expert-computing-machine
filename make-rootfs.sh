#!/bin/bash

set -o errexit
set -x

apko --log-level debug --build-arch amd64 build-minirootfs os.yaml rootfs-amd64.tgz
mkdir -p rootfs-amd64
sudo tar xzf rootfs-amd64.tgz -C rootfs-amd64
sudo /sbin/mkfs.ext4 -L root -d ./rootfs-amd64/ rootfs-amd64.ext4 2G

apko --log-level debug --build-arch aarch64 build-minirootfs os.yaml rootfs-aarch64.tgz
mkdir -p rootfs-aarch64
sudo tar xzf rootfs-aarch64.tgz -C rootfs-aarch64
sudo /sbin/mkfs.ext4 -L root -d ./rootfs-aarch64/ rootfs-aarch64.ext4 2G
