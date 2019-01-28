#!/bin/bash
input="$1"
noions="tmp-noions.pdb"
xyzrfile="vossvolvox/xyzr/pdb_to_xyzr"
xyzr="tmp.xyzr"
v="vossvolvox/bin"

egrep "^ATOM " $1 > $noions


$xyzrfile $noions > $xyzr

$v -i $xyzr -p 1.5 -g 0.5

