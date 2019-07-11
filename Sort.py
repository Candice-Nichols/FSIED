import ast
handle = open("volumeoutput.txt","r")
#handle = open("volumeoutput_copy.txt","r")

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
handle2=open("fittedpairs.txt","w")
handle2.write("atomid: atom_vol, EMid: EM_vol, score\n")
print("atomid: atom_vol, EMid: EM_vol, score")
count=len(em_order)
for i in range(count):
	pdbgroup=atomic_order[i]
	emfile=em_order[i]
	print(sum_dict[pdbgroup])
	score=abs(sum_dict[pdbgroup]-sum_em_dict[emfile])/sum_dict[pdbgroup]
	print(pdbgroup+": "+str(sum_dict[pdbgroup])+" , "+emfile+": "+str(sum_em_dict[emfile])+" " + str(score))
	handle2.write(pdbgroup+": "+str(sum_dict[pdbgroup])+" , "+emfile+": "+str(sum_em_dict[emfile])+" "+str(score)+"\n")
	#sorting using nearest neighbor
	for j in range(3,0,-1):
		if (i-j)>=0:
			emfile=em_order[i-j]
			score=abs(sum_dict[pdbgroup]-sum_em_dict[emfile])/sum_dict[pdbgroup]+j
			print(pdbgroup+": "+str(sum_dict[pdbgroup])+" , "+emfile+": "+str(sum_em_dict[emfile])+" " + str(score))
			handle2.write(pdbgroup+": "+str(sum_dict[pdbgroup])+" , "+emfile+": "+str(sum_em_dict[emfile])+" "+str(score)+"\n")
		if (i+j)<count:
			emfile=em_order[i+j]
			score=abs(sum_dict[pdbgroup]-sum_em_dict[emfile])/sum_dict[pdbgroup]+j
			print(pdbgroup+": "+str(sum_dict[pdbgroup])+" , "+emfile+": "+str(sum_em_dict[emfile])+" " + str(score))
			handle2.write(pdbgroup+": "+str(sum_dict[pdbgroup])+" , "+emfile+": "+str(sum_em_dict[emfile])+" "+str(score)+"\n")
	print()
	handle2.write("\n")
handle2.close()

