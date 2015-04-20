#!/bin/bash

export DEST=answers-$(git rev-parse --short HEAD)

echo "writing to $DEST"

if [[ "$1" ]]; then
    languages="$1"
else
    languages='dutch english spanish greek'
fi

for n in $languages; do
    mkdir -p $DEST/$n
    time ./pan-test -i corpus/*$n* -o $DEST/$n --raw-answers  2>>$DEST/stderr-$n.log
 done
