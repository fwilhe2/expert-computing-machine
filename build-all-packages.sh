#!/bin/bash

set -o errexit

for file in manifests/*; do
    if [ -f "$file" ]; then
        echo "$file"
        ./build-package.sh `basename "${file%.*}"`
        # fixme: make this optional/on demand
        # /tmp does not enough space on my laptop..
        sudo rm -rf /tmp/melange-* /tmp/apk*
    fi
done
