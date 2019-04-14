from IPython.display import HTML
from pypdb import *
import pprint

#Prompt users to enter pdb IDs
pdbids=input("Please enter pdb ID(s), separated by comma: ")
pdbids=pdbids.split(",")

#Fetch pdb files corresponding to the user input
for id in pdbids:
	try:
		pdb_file= get_pdb_file(id, filetype='pdb', compression=False)
		filename = id + ".pdb"
		f = open(filename, "w")
		f.write(pdb_file)
	except:
		print("Sorry! The pdb ID "+ id + " does not exist!")
		exit()
print(pdbids)


