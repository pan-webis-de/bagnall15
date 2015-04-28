#!/bin/bash

lang=$1
dest=$2

(for x in $(./calc-score -v -t corpus/pan15-authorship-verification-training-dataset-$lang-2015-03-02/truth.txt -S -p answers-\*/$lang/raw-answers.txt); do echo $x; git show $x:pan-test |grep -A20 'CONFIG ='; echo; done) >  $dest
