#!/bin/bash

set -o errexit

set -x

mkdir -p repo/x86_64
find . -name '*.apk' -exec grep x86_64 | cp {} repo/x86_64 \;
find . -name 'APKINDEX.tar.gz' -exec tar xf {} \;
python3 .github/workflows/merge-apk-index.py
touch repo/x86_64/DESCRIPTION
cat repo/x86_64/APKINDEX
pushd repo/x86_64
tar czf APKINDEX.tar.gz APKINDEX DESCRIPTION
popd

mkdir -p repo/aarch64
find . -name '*.apk' -exec grep aarch64 | cp {} repo/aarch64 \;
find . -name 'APKINDEX.tar.gz' -exec tar xf {} \;
python3 .github/workflows/merge-apk-index.py
touch repo/aarch64/DESCRIPTION
cat repo/aarch64/APKINDEX
pushd repo/aarch64
tar czf APKINDEX.tar.gz APKINDEX DESCRIPTION
popd


find repo