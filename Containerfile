FROM cgr.dev/chainguard/wolfi-base

RUN apk add build-base busybox ca-certificates-bundle ncurses-dev scanelf flex bison bc wolfi-baselayout
