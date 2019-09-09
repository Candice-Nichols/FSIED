#!/bin/bash
input="$1"


voxel="$2"
echo "$voxel"
echo "$input"
vol10="/home/cc59863/varyingVolumes/FSIED/EM10.mrc"


#create lower resolution em map using lowpass filter
relion_image_handler --i $1 --o $vol10 --lowpass 10

#compute and record the EM volume for each em maps
echo "$input" >> /home/cc59863/varyingVolumes/FSIED/EMoutput.txt
cd /programs/x86_64-linux/eman/1.9/bin.capsules/
volume $vol10 $voxel >> /home/cc59863/varyingVolumes/FSIED/EMoutput.txt





