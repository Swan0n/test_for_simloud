#!/bin/bash
find $1 -iname '*.jpg' -o -iname '*.jpeg' > sooMain.txt | sed  's/\.jpg/\.jpeg/g' sooMain.txt


