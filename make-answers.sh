#!/bin/bash

export DEST=answers-$(git rev-parse --short HEAD)

for n in dutch english spanish greek; do
    mkdir -p $DEST/$n
    time ./pan-test -i corpus/*$n* -o $DEST/$n 2>>$DEST/stderr-$n.log
 done
