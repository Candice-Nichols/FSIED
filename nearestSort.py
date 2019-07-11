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
	score_dict={}
	lst_score = []
	pdbgroup=atomic_order[i]
	emfile=em_order[i]
	print(sum_dict[pdbgroup])
	score=abs(sum_dict[pdbgroup]-sum_em_dict[emfile])
	lst_score.append(score)
	setpair = (pdbgroup,emfile,0)
	score_dict[setpair]=score
	
	for j in range(2,0,-1):
		if (i-j)>=0:
			emfile=em_order[i-j]
			score=abs(sum_dict[pdbgroup]-sum_em_dict[emfile])
			lst_score.append(score)
			setpair = (pdbgroup,emfile,-j)
			score_dict[setpair]=score
		if (i+j)<count:
			emfile=em_order[i+j]
			score=abs(sum_dict[pdbgroup]-sum_em_dict[emfile])
			lst_score.append(score)
			setpair = (pdbgroup,emfile,j)
			score_dict[setpair]=score
	print(score_dict)

	lst_score.sort()
	min_diff = lst_score[0]
	for k in score_dict:
		if min_diff == score_dict[k]:
			x,y,z=(k)
			print(z)
	print(lst_score)

	lst_index= [z-2,z-1,z,z+1,z+2]
	for index in lst_index:
		index2= i+index
		if index2>=0 and index2<count:
			#print(index)
			emfile_2 = em_order[index2]
			score=abs(sum_dict[pdbgroup]-sum_em_dict[emfile_2])
			print(pdbgroup+": "+str(sum_dict[pdbgroup])+" , "+emfile_2+": "+str(sum_em_dict[emfile_2])+" " + str(score))
		if index2<0:
			index2= i-index+2
			#print(index2)
			emfile_2 = em_order[index2]
			score=abs(sum_dict[pdbgroup]-sum_em_dict[emfile_2])
			print(pdbgroup+": "+str(sum_dict[pdbgroup])+" , "+emfile_2+": "+str(sum_em_dict[emfile_2])+" " + str(score))
		if index2>=count:
			index2 = i-index-2
			#print(index2)
			emfile_2 = em_order[index2]
			score=abs(sum_dict[pdbgroup]-sum_em_dict[emfile_2])
			print(pdbgroup+": "+str(sum_dict[pdbgroup])+" , "+emfile_2+": "+str(sum_em_dict[emfile_2])+" " + str(score))
		

	if i == 0 or i == count-1:
		hol = 3
	elif i == 1 or i == count-2:
		hol = 4
	else:
		hol = 5



	#for q in lst_score:
	#	for k in score_dict:
	#		if q == score_dict[k]:
	#			x,y,z=(k)
	#			print(k)
	#			print(x+": "+str(sum_dict[x])+" , "+y+": "+str(sum_em_dict[y])+" " + str(q))

	print()

handle2.close()

