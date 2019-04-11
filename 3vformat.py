handle = open("3voutput.txt","r")
for line in handle:
	info = line.split()
print(info[2])

