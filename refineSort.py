import ast
handle = open("volumeoutput.txt","r")

#read dictionary of group volume
line1=handle.readline()
atomic_dict=line1.strip()
atomic_dict=ast.literal_eval(atomic_dict)
#create dictionary of volume of sum
sum_dict={}
for key in atomic_dict:
	temp_dict = atomic_dict[key]
	sum_dict[key] = temp_dict["sum"]


#read order of atomic structure groups
line2= handle.readline()
atomic_order=line2.strip()
atomic_order=ast.literal_eval(atomic_order)


#skip line 4
handle.readline()

#read dictionary of em volume
line4=handle.readline()
em_dict=line4.strip()
em_dict=ast.literal_eval(em_dict)
sum_em_dict={}
#create dictionary of volume of sum
for key in em_dict:
	temp_dict = em_dict[key]
	sum_em_dict[key] = temp_dict["avg"]



#read order of em maps
line5=handle.readline()
em_order=line5.strip()
em_order=ast.literal_eval(em_order)


handle.close()

#sorting
handle2=open("refinefittedpairs.txt","w")
handle2.write("atomid: atom_vol, EMid: EM_vol, score\n")
print("atomid: atom_vol, EMid: EM_vol, score")
count=len(em_order)
for i in range(count):
	score_lst=[]
	output_dict={}
	pdbgroup=atomic_order[i]
	emfile=em_order[i]
	score=abs(sum_dict[pdbgroup]-sum_em_dict[emfile])/sum_dict[pdbgroup]
	score_lst.append(score)
	output_dict[score]=(pdbgroup+": "+str(sum_dict[pdbgroup])+" , "+emfile+": "+str(sum_em_dict[emfile])+" " + str(score))
	for j in range(3,0,-1):
		if (i-j)>=0:
			emfile=em_order[i-j]
			score=abs(sum_dict[pdbgroup]-sum_em_dict[emfile])/sum_dict[pdbgroup]+j
			score_lst.append(score)
			output_dict[score]=(pdbgroup+": "+str(sum_dict[pdbgroup])+" , "+emfile+": "+str(sum_em_dict[emfile])+" " + str(score))
		if (i+j)<count:
			emfile=em_order[i+j]
			score=abs(sum_dict[pdbgroup]-sum_em_dict[emfile])/sum_dict[pdbgroup]+j
			score_lst.append(score)
			output_dict[score]=(pdbgroup+": "+str(sum_dict[pdbgroup])+" , "+emfile+": "+str(sum_em_dict[emfile])+" " + str(score))
	score_lst.sort()
	firstmatch= score_lst[0]
	secondmatch = score_lst[1]
	thirdmatch = score_lst[2]
	forthmatch = score_lst[3]
	print(output_dict[firstmatch])
	handle2.write(output_dict[firstmatch])
	handle2.write("\n")
	print(output_dict[secondmatch])
	handle2.write(output_dict[secondmatch])
	handle2.write("\n")
	print(output_dict[thirdmatch])
	handle2.write(output_dict[thirdmatch])
	handle2.write("\n")
	print(output_dict[forthmatch])
	handle2.write(output_dict[forthmatch])
	handle2.write("\n")
	print()
	handle2.write("\n")


handle2.close()


