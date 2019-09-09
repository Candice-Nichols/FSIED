#!/bin/bash
#fetch pdb files
echo "start fetching pdb files"
python fetchpdb.py
echo "finished fetching pdb files"

#calculate atomic structure volumes
echo "start calculating volume"
python sumvolume.py

#calculate EM volume
echo "start calculating EM volume"
python AvgEMvolume.py

#sort by volumes
echo "start sorting"
python assemble2.py

echo "start sorting"
python assemble_sort.py

#remove temporary files
for file in *.pdb
	do
		rm $file
	done
