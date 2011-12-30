#!/bin/bash

printf 'Content-type: text/html\n\n'
nohup python make.py &
echo '<a href="http://heardmag.com/">Heard Magazine</a>'