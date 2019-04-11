#!/bin/bash
input="$1"

echo "Enter voxel size"

read voxel


vol5="EM5.mrc"
vol10="EM10.mrc"
vol15="EM15.mrc"
vol20="EM20.mrc"

relion_image_handler --i $1 --o $vol5 --lowpass 5
relion_image_handler --i $1 --o $vol10 --lowpass 10
relion_image_handler --i $1 --o $vol15 --lowpass 15
relion_image_handler --i $1 --o $vol20 --lowpass 20

volume $1 $voxel
volume $vol5 $voxel
volume $vol10 $voxel
volume $vol15 $voxel
volume $vol20 $voxel






