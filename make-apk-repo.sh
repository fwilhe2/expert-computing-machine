#!/bin/bash

mkdir -p repo/x86_64
find . -name '*.apk' -exec cp {} repo/x86_64 \;
find . -name 'APKINDEX.tar.gz' -exec tar xf {} \;
python3 .github/workflows/merge-apk-index.py
touch repo/x86_64/DESCRIPTION
cat repo/x86_64/APKINDEX
pushd repo/x86_64
tar czf APKINDEX.tar.gz APKINDEX DESCRIPTION
popd
find repo