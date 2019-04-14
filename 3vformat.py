handle = open("3voutput.txt","r")
dict = {}
lst = []
for line in handle:
	info = line.split()
	#read the pdb id of the information
	if len(info) == 1:
		key = info[0]
		key = key[:4]
	#read the volume
	else:
		dict[key]=float(info[2])
		lst.append(float(info[2]))
lst.sort()
order = []
for item in lst:
	for v in dict:
		if item == dict[v]:
			order.append(v)
#volume in increasing order	
print(lst)
#pdb ID in increasing order
print(order)
#dictionary referencing volume and pdb ID
print(dict)

