import mrcfile
mrc = mrcfile.open('0502.mrc',mode='r+')
print(mrc.voxel_size.x)
