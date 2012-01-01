#!/bin/bash

printf 'Content-type: text/html\n\n'
mkdir backup
cp -f *html backup/
git add backup backup/*
git commit -a -m update
git pull
git push
python make.py
echo '<br><br><br><a href="http://heardmag.com/">Heard Magazine</a>'
