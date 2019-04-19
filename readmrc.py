import subprocess
import os

print("start reading in mrc files")
handle = open("inputmrc.txt","r")
print("start computing the EMVolume")
for line in handle:
	line=line.strip()
	info=line.split(":")
	mrc_id=line[0] + ".mrc"
	voxel_size=line[1]
	val = subprocess.check_call("./EMVolume.sh %s %s" % (mrc_id, voxel_size), shell=True)

handle.close()
print("Finish computing the EMVolume")


#handle2 = open("outputmrc.txt","r")
#handle2.close()
