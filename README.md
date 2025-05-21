# Basic steps
The setup.py script has all steps to get the autoradiographs. Need to add a line to copy over the histology images and a python script to preprocess and fix them.

1. Copy data from inm1filesrv1
2. Convert TIF files to nii.gz using the reference section
3. Create .csv files that Brainbuilder uses to run the reconstruction
4. Launch reconstruction with docker container

These steps obiously don't all need to be run every time. Once steps 1-3 have been run, then only step 4 needs to be run.
