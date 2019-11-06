input="$1"

outputgmm="6CT0_200.gmm"
outputpdb="pdbfile.pdb"

#convert atomic structure to gaussion
./gmconvert A2G -ipdb $input -ng 200

#convert gaussion to surface
./gmconvert G2S -igmm 6CT0_200.gmm -gw 4 -opdb pdbfile.pdb

#calculate surface volume using chimera
