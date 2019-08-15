#!/bin/bash

input="$1"
xyzrfile="vossvolvox/xyzr/pdb_to_xyzr"
v="vossvolvox/bin"
output="3vvolumelog.txt"
xyzr="tmp.xyzr"
noions="tmp-noions.pdb"

#remove hetero atom
egrep "^ATOM " $input > $noions
#create xyzr file
$xyzrfile $noions > $xyzr

#write output
echo "$input" >> $output
$v -i $xyzr -p 1.5 -g 0.5 >> $output

#remove temperary files
rm $xyzr
rm $noions
