import numpy as np
import nibabel as nib
import imageio 
import os
from glob import glob
from sys import argv

auto_affine = np.eye(4)
auto_affine[0,0] = 0.0048
auto_affine[1,1] = 0.0048

hist_affine = np.eye(4)
hist_affine[0,0] = 0.0048 #TODO CHECK IF THIS IS CORRECT, ASK NICOLA
hist_affine[1,1] = 0.0048 #TODO CHECK IF THIS IS CORRECT, ASK NICOLA

if __name__ == '__main__' :
    target_dir = argv[1]

    for fin in glob(f"{target_dir}/*TIF") :

        out_fin = fin.replace('.TIF', '.nii.gz')
        
        if not os.path.exists(out_fin) :
            ar = imageio.imread(fin)
            ar = np.squeeze(ar) 

            if 'cellbody' in fin or 'myelin' in fin :
                affine = hist_affine
            else :
                affine = auto_affine

            nib.Nifti1Image(ar, affine).to_filename(out_fin)

