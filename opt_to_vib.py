import os
import glob

output_files = glob.glob('*.out')
for output_file in output_files:
    print(output_file)
    with open(output_file, "r") as output:
        lines = output.readlines()
        space_group = lines[3]
        num_atoms = lines[5]
        for i,val in enumerate(lines):    
            if " FINAL OPTIMIZED GEOMETRY - DIMENSIONALITY OF THE SYSTEM      3" in val:
                del lines[0:i]
            
            if "COORDINATES IN THE CRYSTALLOGRAPHIC CELL" in val:
                lattice_parameters = lines[i-2]              
            if "END" in val and "END" in lines[i+1]:
                x = i
            if "99 0" in val:
                y = i
                basis_data = lines[x+2:y]

                
                
              
