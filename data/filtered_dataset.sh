#!/bin/bash
mkdir $2
mkdir $2/train
mkdir $2/train/good_0
mkdir $2/train/bad_0
mkdir $2/val
mkdir $2/val/good_0
mkdir $2/val/bad_1
rsync -a  $1/train/good_0 --files-from=$3 $2/train/good_0
rsync -a  $1/train/bad_1 --files-from=$4 $2/train/bad_1
cp $1/val/good_0/*.jpg $2/val/good_0
cp $1/val/bad_1/*.jpg $2/val/bad_1

