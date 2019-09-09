import sys
import os.path
from chimera import runCommand # opens chimera without visual interface
from chimera import replyobj # emits status message
from chimera.tkgui import saveReplyLog


input=open("testInput2.txt","r")
for line in input:
	line=line.strip()
	fn='emd_'+line+'.map'
	replyobj.status('Processing ' + fn) # shows the file that is being worked on
	runCommand('open ' + fn)
	runCommand('volume all save '+line+'.mrc')
	runCommand('close all')

