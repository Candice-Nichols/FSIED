#!/bin/bash

python fetchpdb.py



#execute 3vvolume.sh only when pdb files are found in the directory
if [ ! -f *.pdb ]; then
    echo "file(s) not found"
    exit 1
else
    echo "the file(s) exist"
    ./3vvolume.sh
    
    for file in *.pdb
        do
            rm $file
        done
fi

