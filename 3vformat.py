handle = open("3voutput.txt","r")
dict = {}
for line in handle:
	info = line.split()
	if len(info) == 1:
		key = info[0]
		key = key[:4]
	else:
		dict[key]=float(info[2])
print(dict)

