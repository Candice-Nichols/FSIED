#!/bin/bash
input="$1"
noions="tmp-noions.pdb"
xyzrfile="vossvolvox/xyzr/pdb_to_xyzr"
xyzr="tmp.xyzr"
v="vossvolvox/bin"
output="3voutput.txt"

egrep "^ATOM " $1 > $noions


$xyzrfile $noions > $xyzr

$v -i $xyzr -p 1.5 -g 0.5 > $output

python 3vformat.py


rm $output
rm $noions
rm $xyzr
