#!/bin/bash

pushd repo
trap 'popd' EXIT
python3 -m http.server &