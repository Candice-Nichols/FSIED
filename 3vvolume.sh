#!/bin/bash

#input="$1"
#noions="tmp-noions.pdb"
xyzrfile="vossvolvox/xyzr/pdb_to_xyzr"
#xyzr="tmp.xyzr"
v="vossvolvox/bin"
output="3voutput.txt"

for file in *.pdb
do
	xyzr="tmp.xyzr"
	noions="tmp-noions.pdb"
	egrep "^ATOM " $file > $noions
	$xyzrfile $noions > $xyzr
	echo "$file" >> $output
	$v -i $xyzr -p 1.5 -g 0.5 >> $output
	rm $xyzr
	rm $noions
done

python 3vformat.py


rm $output
#rm $noions
#rm $xyzr
