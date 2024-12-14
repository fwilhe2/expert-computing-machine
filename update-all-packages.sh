#!/bin/bash

set -o errexit

for file in manifests/*yaml; do
    if [ -f "$file" ]; then
        echo "$file"
        python3 update.py `basename "${file%.*}"`
    fi
done
