source_dir="/import" # This assumes that inmfilesrv1 is mounted to /import. Modify as needed

target_dir="/tmp/target" #TODO Enter your target directory for the rat reconstruction project
output_dir="/tmp/output" #TODO Define directory where reconstruction outputs will be saved

mkdir -p $target_dir $output_dir

### 1) Copy data from inm1filesrv1

cp `find ${source_dir}/AR_raw_data/rat/L6_3D-Rattenatlas/Digitalisierung_Autoradiogramme/img_farb/ -name "*pire*112*#L.TIF"` ${target_dir}/

ls ${target_dir}/*TIF | wc -l
### 2) Convert TIF files to nii.gz using the reference section
python3 convert_tif_to_nii.py $target_dir $reference_section

ls ${target_dir}/*nii.gz | wc -l

### 3) Create .csv files that Brainbuilder uses to run the reconstruction
# These csv files contain information about the files that are used for the reconstruction
python3 create_info_csv.py $target_dir $output_dir


### 4) Launch reconstruction
docker run -it --rm -v `pwd`:`pwd` -v $target_dir:$target_dir -v $output_dir:$output_dir tffunck/brainbuilder:latest python3 `pwd`/reconstruct_rat.py `pwd` $output_dir


