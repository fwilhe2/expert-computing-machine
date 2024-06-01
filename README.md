# expert-computing-machine

Playground for wolfi-based packages

See https://github.com/wolfi-dev/os/ for upstream source

Example command to build a package:

```
melange build --arch x86_64 --keyring-append https://packages.wolfi.dev/os/wolfi-signing.rsa.pub --repository-append https://packages.wolfi.dev/os bash.yaml 
```
