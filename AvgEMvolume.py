import subprocess
import os

#read input
print("start reading in mrc files")
handle = open("inputmrc.txt","r")
print("start computing the EMVolume")

dict_multi={}
for line in handle:
	#parse info from input file
	line=line.strip()
	info=line.split(":")
	mrc_info=info[0].split("*")

	#parse em map filenames
	mrc_id=mrc_info[0] + ".mrc"
	#for multiple em maps
	if len(mrc_info)==2:
		multi = mrc_info[1]
		dict_multi[mrc_id]=multi
	#parse voxel size
	voxel_size=info[1]
	#compute em volume
	val = os.system("./EMVolume.sh {0} {1}".format(mrc_id, voxel_size))

handle.close()
print("Finish computing the EMVolume")

#compute average EM volume
print("start computing the average EMVolume")
outputdict={}
avg_lst=[]
handle2 = open("EMoutput.txt","r")
for line in handle2:
	line=line.strip()
	info=line.split()
	#parse emfile name
	if len(info) == 1:
		emfile = info[0]
		lst_vol = []
	#parse em volume and compute total em volume if multiple em maps 
	elif len(info) == 7 and info[2]=="A^3":
		if emfile in dict_multi:
			emvol = float(info[1])*float(dict_multi[emfile])
		else:
			emvol = float(info[1])
		lst_vol.append(emvol)
	#compute average and record output
	elif len(info) ==2 and info[0]=="end":
		new_dict = {}
		new_dict["reg"] = lst_vol[0]
		new_dict["5"] = lst_vol[1]
		new_dict["10"] = lst_vol[2]
		new_dict["15"] = lst_vol[3]
		new_dict["20"] = lst_vol[4]
		avg=sum(lst_vol)/(len(lst_vol))
		new_dict["avg"] = avg
		avg_lst.append(avg)
		outputdict[emfile]=new_dict
#print(avg_lst)
#print(outputdict)
handle2.close()
os.remove("EMoutput.txt")

#order output by average size
avg_lst.sort()
print(avg_lst)
ordered_group = []
for item in avg_lst:
	for key in outputdict:
		proteinvol = outputdict[key]
		if proteinvol["avg"]==item:
			ordered_group.append(key)
print(ordered_group)

#write output file
handle3 = open("volumeoutput.txt","a")
handle3.write("\n")
handle3.write(str(outputdict))
handle3.write("\n")
handle3.write(str(ordered_group))
handle3.write("\nEND OF EM VOLUME")
handle3.close()

