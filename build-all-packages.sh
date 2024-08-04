#!/bin/bash

for file in manifests/*; do
    if [ -f "$file" ]; then
        echo "$file"
        ./build-package.sh `basename $file`
    fi
done
