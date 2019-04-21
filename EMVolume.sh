#!/bin/bash
input="$1"


voxel="$2"
vol5="EM5.mrc"
vol10="EM10.mrc"
vol15="EM15.mrc"
vol20="EM20.mrc"

relion_image_handler --i $1 --o $vol5 --lowpass 5
relion_image_handler --i $1 --o $vol10 --lowpass 10
relion_image_handler --i $1 --o $vol15 --lowpass 15
relion_image_handler --i $1 --o $vol20 --lowpass 20

echo "$input" >> EMoutput.txt
volume $1 $voxel >> EMoutput.txt
volume $vol5 $voxel >> EMoutput.txt
volume $vol10 $voxel >> EMoutput.txt
volume $vol15 $voxel >> EMoutput.txt
volume $vol20 $voxel >> EMoutput.txt
echo "end $input" >> EMoutput.txt






