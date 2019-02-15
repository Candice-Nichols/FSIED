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
./myscript.sh 6he8.pdb
```


## Calculate volume of atomic structure using chimera
The script is scripted for the sample file 6he8.pdb- to calculate a different file, change path to fn in chimera_volume.py
```
chimera --nogui --script chimera_volume.py > volume_reply_log.txt
```

## Calculate volume of electron density using chimera
The script is scripted for the sample file emd_0212.map- to calculate a different file, change path to fn in chimera_volume.py
```
chimera --nogui --script chimera_EMvolume.py > density_volume_reply_log.txt
```

