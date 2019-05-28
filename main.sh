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
python Sort.py

#remove temporary files
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

