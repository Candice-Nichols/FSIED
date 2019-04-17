#!/bin/bash

input="$1"
#noions="tmp-noions.pdb"
xyzrfile="vossvolvox/xyzr/pdb_to_xyzr"
#xyzr="tmp.xyzr"
v="vossvolvox/bin"
output="3vvolumelog.txt"


xyzr="tmp.xyzr"
noions="tmp-noions.pdb"
egrep "^ATOM " $input > $noions
$xyzrfile $noions > $xyzr
echo "$input" >> $output
$v -i $xyzr -p 1.5 -g 0.5 >> $output
rm $xyzr
rm $noions




#rm $output
#rm $noions
#rm $xyzr
