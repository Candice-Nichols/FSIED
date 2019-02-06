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

### Calculate volume of test file
```
./myscript.sh pdb5m3l.pdb
```


## Calculate volume of atomic structure using chimera
The script is scripted for the sample file pdb5m3l.pdb- to calculate a different file, change path to fn in chimera_volume.py
```
chimera --nogui --script chimera_volume.py > reply_log.txt
```
