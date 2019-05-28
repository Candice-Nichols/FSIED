#from IPython.display import HTML
#from pypdb import *
#import pprint
import subprocess

#Read input file
handle = open("inputpdb.txt","r")
linenum = 1
for line in handle:
	line=line.strip()
	pdbids=line.split(",")
	for idlst in pdbids:
		#parse pdbids from input
		idlst=idlst.split("*")
		id=idlst[0]
		command = "wget https://files.rcsb.org/download/"+id+".pdb"
		subprocess.check_call(command.split())
		
        	#try:
                #	pdb_file= get_pdb_file(id, filetype='pdb', compression=False)
                #	filename = id + ".pdb"
                #	f = open(filename, "w")
                #	f.write(pdb_file)
        	#except:
                #	print("Sorry! The pdb ID "+ id + "in line "+ str(linenum) + " does not exist!")
                #	exit()
	linenum+=1
handle.close()	
	


