# FSIED
Fitting subunits into electron densities


## Calculate volume of atomic structure using 3V


### Clone vossvolvox source code
```
git clone https://github.com/vosslab/vossvolvox.git
```

### Compile 3v program
```
cd vossvolvox
cd src
make vol
cd ..
cd ..
```

### Find fitted pairs
First, enter RCSB ids in the input file inputpdb.txt, format as following:
```
pdbid1
pdbid2
...
```
for multiple RCSB ids in one protein complex, format as following:
```
pdbid1,pdbid2,pdbid3...
```
for multiplication of the same RCSB id, format as following:
```
pdbid1*k
```
k is the number of multiplication.

After making sure that the experimental EM maps (in .mrc format) is located in the main directory, enter file name in inputmrc.txt, format as follwoing:
```
filename:voxel_size
```
for multiplication of the same experimental EM maps, format as following:
```
filename*k:voxel_size
```

To start calculating fitted pairs
```
./main.sh
```


### Optional: Refined fitted pairs
After running the fitted pair script, users can opt to compute a more refined pool of fitted pairs as following:
(this algorithm is still being worked on for improvement in accuracy)
```
python refineSort.py
```



