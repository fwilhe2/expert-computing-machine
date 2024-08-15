#!/bin/bash

set -o errexit

PACKAGE=$1

melange build --arch x86_64 --log-level debug --keyring-append https://packages.wolfi.dev/os/wolfi-signing.rsa.pub --repository-append https://packages.wolfi.dev/os --runner qemu manifests/$PACKAGE.yaml

pushd packages/x86_64
tar xzf APKINDEX.tar.gz
mv APKINDEX $PACKAGE-APKINDEX

popd