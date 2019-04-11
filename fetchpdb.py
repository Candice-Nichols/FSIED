from IPython.display import HTML
from pypdb import *
import pprint

pdbids=input("Please enter pdb ID, separated by comma: ")
pdbids=pdbids.split(",")
for id in pdbids:
	pdb_file= get_pdb_file(id, filetype='pdb', compression=False)
	filename = id + ".pdb"
	f = open(filename, "w")
	f.write(pdb_file)
print(pdbids)


