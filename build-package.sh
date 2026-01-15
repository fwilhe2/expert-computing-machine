#!/bin/bash

set -o errexit

PACKAGE=$1

melange build --arch x86_64,arm64 --keyring-append https://packages.wolfi.dev/os/wolfi-signing.rsa.pub --repository-append https://packages.wolfi.dev/os manifests/$PACKAGE.yaml

pushd packages/x86_64
tar xzf APKINDEX.tar.gz
mv APKINDEX $PACKAGE-APKINDEX-x86_64
popd


pushd packages/aarch64
tar xzf APKINDEX.tar.gz
mv APKINDEX $PACKAGE-APKINDEX-aarch64
popd

