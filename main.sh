#!/bin/bash
echo "start fetching pdb files"
python fetchpdb.py
echo "finished fetching pdb files"

echo "start calculating volume"
python sumvolume.py

echo "start calculating EM volume"
python AvgEMvolume.py

echo "start sorting"
python Sort.py

for file in *.pdb
	do
		rm $file
	done

#execute 3vvolume.sh only when pdb files are found in the directory
#if [ ! -f *.pdb ]; then
 #   echo "file(s) not found"
  #  exit 1
#else
 #   echo "the file(s) exist"
  #  ./3vvolume.sh
    
   # for file in *.pdb
    #    do
     #       rm $file
      #  done
#fi

