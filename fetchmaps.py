import subprocess
import os
import mrcfile
input = open("testInput.txt","r")
command1 = "rm EMoutput.txt"
subprocess.check_call(command1.split())
for line in input:
	line=line.strip()
	#fetch maps
	command= "wget ftp://ftp.ebi.ac.uk/pub/databases/emdb/structures/EMD-"+line+"/map/emd_"+line+".map.gz"
	subprocess.check_call(command.split())
	f= 'emd_'+line+'.map.gz'

	#unpack maps
	command2= "gunzip "+f
	subprocess.check_call(command2.split())
	output=open("testInput2.txt","w")
	output.write(line)
	output.close()

	#convert maps
	command3="chimera --nogui --script chimera_convert.py"
	subprocess.check_call(command3.split())

	#find voxel size
	name=line+".mrc"
	mrc = mrcfile.open(name, mode="r+")
	voxel= mrc.voxel_size.x
	os.system("./EMVolume2.sh {0} {1}".format(name,voxel))

	#rm maps
	command4="rm emd_"+line+".map"
	command5="rm "+name
	subprocess.check_call(command4.split())
	subprocess.check_call(command5.split())
