from IPython.display import HTML
from pypdb import *
import pprint

#Read input file
handle = open("inputpdb.txt","r")
linenum = 1
for line in handle:
	line=line.strip()
	pdbids=line.split(",")
	for id in pdbids:
        	try:
                	pdb_file= get_pdb_file(id, filetype='pdb', compression=False)
                	filename = id + ".pdb"
                	f = open(filename, "w")
                	f.write(pdb_file)
        	except:
                	print("Sorry! The pdb ID "+ id + "in line "+ str(linenum) + " does not exist!")
                	exit()
	linenum+=1
handle.close()	
	


