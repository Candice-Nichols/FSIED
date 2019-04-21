import subprocess
import os

print("start reading in mrc files")
#handle = open("inputmrc.txt","r")
#print("start computing the EMVolume")
#for line in handle:
#	line=line.strip()
#	info=line.split(":")
#	mrc_id=line[0] + ".mrc"
#	voxel_size=line[1]
#	val = subprocess.check_call("./EMVolume.sh %s %s" % (mrc_id, voxel_size), shell=True)

#handle.close()
print("Finish computing the EMVolume")

print("start computing the average EMVolume")
outputdict={}
avg_lst=[]
handle2 = open("EMoutput.txt","r")
for line in handle2:
	line=line.strip()
	info=line.split()
	if len(info) == 1:
		emfile = info[0]
		lst_vol = []
	elif len(info) == 6 and info[2]=="A^3":
		emvol = float(info[1])
		lst_vol.append(emvol)
	elif len(info) ==2 and info[0]=="end":
		new_dict = {}
		new_dict["reg"] = lst_vol[0]
		new_dict["5"] = lst_vol[1]
		new_dict["10"] = lst_vol[2]
		new_dict["15"] = lst_vol[3]
		new_dict["20"] = lst_vol[4]
		avg=sum(lst_vol)/len(lst_vol)
		new_dict["avg"] = avg
		avg_lst.append(avg)
		outputdict[emfile]=new_dict
print(outputdict)
handle2.close()
#os.remove("EMoutput.txt")

avg_lst.sort()
ordered_group = []
for key in outputdict:
	for item in avg_lst:
		proteinvol = outputdict[key]
		if proteinvol["avg"]==item:
			ordered_group.append(key)
print(ordered_group)

handle3 = open("volumeoutput.txt","a")
handle3.write("\n")
handle3.write(str(outputdict))
handle3.write("\n")
handle3.write(str(ordered_group))
handle3.write("\nEND OF EM VOLUME")
handle3.close()

