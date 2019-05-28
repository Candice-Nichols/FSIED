import subprocess
import os
handle = open("inputpdb.txt","r")

print("start computing volume sum")
volume_dict = {}
group_num = 1
volume_list =[]
multi={}
#Read in each group of protein files
for line in handle:
	line = line.strip()
	pdbids = line.split(",")

	#compute volume for each protein in the group
	for info in pdbids:
		info2=info.split("*")
		pdbid = info2[0] + ".pdb"
		if len(info2)==2:
			multi[pdbid]=info2[1]
		val = subprocess.check_call("./3vvolume.sh '%s'" % pdbid, shell=True)

	#compute individual protein volume and its sum
	handle2 = open("3vvolumelog.txt","r")
	protein_dict = {}
	volume_sum = 0
	for line in handle2:
		line = line.strip()
		info = line.split()
		#read the pdb id of the information
		if len(info) == 1:
			info= info[0]
			proteinid = info[:4]
		else:
			id=proteinid+".pdb"
			if id in multi.keys():
				volume= float(info[2])*float(multi[id])
			else:
				volume = float(info[2])
			protein_dict[id]=volume
			volume_sum+=volume
	protein_dict["sum"] = volume_sum
	volume_list.append(volume_sum)
	
	#determine group id (group containing 1 protein: id=pdbid, group containing more than one protein is assigned a number)
	if len(protein_dict)==2:
		group_id = proteinid
	else:
		group_id = "group "+str(group_num)
		group_num+=1
	volume_dict[group_id] = protein_dict

	handle2.close()
	os.remove("3vvolumelog.txt")
handle.close()

volume_list.sort()
print(volume_dict)

ordered_group = []
for item in volume_list:
	for key in volume_dict:
		proteinvol = volume_dict[key]
		if proteinvol["sum"]==item:
			ordered_group.append(key)
print(ordered_group)

output = open("volumeoutput.txt","w")
output.write(str(volume_dict))
output.write("\n")
output.write(str(ordered_group))
output.write("\n")
output.write("END OF ATOMIC VOLUME")
output.close()






