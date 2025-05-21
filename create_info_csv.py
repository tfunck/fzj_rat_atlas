import os
import pandas as pd
from glob import glob
from sys import argv
# Use pandas to create section, chunk, and hemisphere info csf files
# The section info file contains the columns: sub,hemisphere,acquisition,sample,chunk,raw
# The chunk info file contains the columns:  sub,hemisphere,acquisition,chunk,pixel_size_0,pixel_size_1,section_thickness,direction
# The hemisphere info file contains the columns: sub,hemisphere,acquisition,struct_ref_vol,wm_surf,gm_surf
# raw is the file path to the raw file


# fixed parameters
hemisphere = 'B' 
chunk = '1'
pixel_size_0=0.0048
pixel_size_1=0.0048
section_thickness=0.02
direction='rostral_to_caudal'
wm_surf=None
gm_surf=None

# The information to fill out these fields is contained in the file names of the tif (.TIF) files in rat/L6/img_lin/
# The sections look like "0617#L6#rt#R2031#musc#10928#0617#L.TIF" and have the following format:
# # <section_number>#L6#rt#<sub>#<acquisition>#<sheet>#<section_number>#L.TIF

section_info_df = pd.DataFrame(columns=['sub', 'hemisphere', 'acquisition', 'sample', 'chunk', 'raw'])
chunk_info_df = pd.DataFrame(columns=['sub', 'hemisphere', 'acquisition', 'chunk', 'pixel_size_0', 'pixel_size_1', 'section_thickness', 'direction'])
hemisphere_info_df = pd.DataFrame(columns=['sub', 'hemisphere', 'acquisition', 'struct_ref_vol', 'wm_surf', 'gm_surf'])

# The file names of the tif files are in the directory rat/L6/img_lin/
input_dir = argv[1] # 'rat/L6/img_lin/'
output_dir = argv[2] # 'rat/L6/section_df/'
struct_ref_vol = './WHS_SD_rat_atlas_v4_gm.nii.gz'

os.makedirs(output_dir, exist_ok=True)
# Get the list of all tif files in the input directory
file_list = glob(f'{input_dir}/*nii.gz')
# Loop through each file and extract the information
for raw_filename in file_list:
    # Extract the section number, sub, acquisition, and sample from the file name
    # The file name is in the format: <section_number>#L6#rt#<sub>#<acquisition>#<sheet>#<section_number>#L.TIF
    # Split the file name by '#' and extract the relevant information
    filename = raw_filename.replace('#X#','#').replace('#x#','#').replace('#L.TIF', '').replace('#rtL6','')

    parts = os.path.basename(filename).split('#')
    
    i=0
    if parts[0] == 'L6': 
        i=1

    # Get the section number, sub, acquisition, and sample
    section_number = parts[-1]
    sub = parts[3-i]
    acquisition = parts[4-i]
    sample = parts[5-i]
    
    # Create a new row for the section info dataframe
    new_row = pd.DataFrame({'sub': [sub], 'hemisphere': [hemisphere], 'acquisition': [acquisition], 'sample': [sample], 'chunk': [chunk], 'raw': [raw_filename]})
    
    # Append the new row to the section info dataframe
    section_info_df = pd.concat([section_info_df, new_row], ignore_index=True)
    
    # Create a new row for the chunk info dataframe
    new_row_chunk = pd.DataFrame({'sub': [sub], 'hemisphere': [hemisphere], 'acquisition': [acquisition], 'chunk': [chunk], 'pixel_size_0': [pixel_size_0], 'pixel_size_1': [pixel_size_1], 'section_thickness': [section_thickness], 'direction': [direction]})
    
    # Append the new row to the chunk info dataframe
    chunk_info_df = pd.concat([chunk_info_df, new_row_chunk], ignore_index=True)
# Create a new row for the hemisphere info dataframe
    new_row_hemisphere = pd.DataFrame({'sub': [sub], 'hemisphere': [hemisphere], 'acquisition': [acquisition], 'struct_ref_vol': [struct_ref_vol], 'wm_surf': [wm_surf], 'gm_surf': [gm_surf]})
    
    # Append the new row to the hemisphere info dataframe
    hemisphere_info_df = pd.concat([hemisphere_info_df, new_row_hemisphere], ignore_index=True)



# Get unique rows for chunk_info_df and hemisphere_info_df
chunk_info_df = chunk_info_df.drop_duplicates()
hemisphere_info_df = hemisphere_info_df.drop_duplicates()
section_info_df = section_info_df.drop_duplicates()

#
section_info_df = section_info_df.sort_values(['sub','hemisphere','acquisition','sample'])

# Save the dataframes to csv files
section_info_df.to_csv(f'section_info.csv', index=False)
chunk_info_df.to_csv(f'chunk_info.csv', index=False)
hemisphere_info_df.to_csv(f'hemisphere_info.csv', index=False)

print("section_info_df:")
print(section_info_df)
print("chunk_info_df:")
print(chunk_info_df)
print("hemisphere_info_df:")
print(hemisphere_info_df)
print("CSV files created successfully.")
