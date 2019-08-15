import subprocess
input = open("testInput.txt","r")
for line in input:
	line=line.strip()
	command= "wget ftp://ftp.ebi.ac.uk/pub/databases/emdb/structures/EMD-"+line+"/map/emd_"+line+".map.gz"
	subprocess.check_call(command.split())
	f= 'emd_'+line+'.map.gz'
	command2= "gunzip "+f
	subprocess.check_call(command2.split())
	output=open("testInput2.txt","w")
	output.write(line)
	command3="chimera --nogui --script chimera_convert.py"
	subprocess.check_call(command3.split())
