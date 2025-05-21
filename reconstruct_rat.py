from brainbuilder.reconstruct import reconstruct
from sys import argv

input_dir = argv[1]
output_dir = argv[2]

reconstruct( 
    input_dir+'/hemisphere_info.csv', ##'hemisphere_df.csv', 
    input_dir+'/chunk_info.csv', #'slab_df.csv',
    input_dir+'/section_info.csv', #'section_df_with_conversion_factors.csv', 
    [0.5, 0.3, 0.2, 0.1, 0.075, 0.05], 
    output_dir,
    max_resolution_3d = 0.03,
    seg_method = 'triangle',
    )

