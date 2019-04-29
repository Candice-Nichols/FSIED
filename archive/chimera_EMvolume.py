#import os

from chimera import runCommand # opens chimera without visual interface
from chimera import replyobj # emits status message
from chimera.tkgui import saveReplyLog

#os.chdir("/home/cmccaffe/varyingVolumes") # change to directory where data is $

#filenames = [fn for fn in os.listdir(".") if fn.endswith(".pdb")] # grabs all $

fn=("emd_0212.map")
#for fn in filenames: # loop through and performs computation on each file
replyobj.status('Processing ' + fn) # shows the file that is being worked on
runCommand('open ' + fn)
#runCommand('surf #0')
runCommand('measure volume #0')
runCommand('measure area #0')
runCommand('close all')
