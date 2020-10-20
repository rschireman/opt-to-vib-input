import os
import glob

output_files = glob.glob('*.out')
for output_file in output_files:
    print(output_file)
    with open(output_file, "r") as output:
        lines = output.readlines()
        space_group = lines[3]
        num_atoms = lines[5]
        title = lines[0]
        for i,val in enumerate(lines):    
            if "END" in val and "END" in lines[i+1]:
                x = i
            if "99 0" in val:
                y = i
                basis_data = lines[x+2:y]
            if "TOLINTEG" in val:
                scf_parmeters = lines[y:i+3]
            
                break
        for i,val in enumerate(lines):
            if " FINAL OPTIMIZED GEOMETRY - DIMENSIONALITY OF THE SYSTEM      3" in val:
                del lines[0:i]
        
            if "COORDINATES IN THE CRYSTALLOGRAPHIC CELL" in val:
                a = i
                lattice_parameters = lines[i-2]   
            if " T = ATOM BELONGING TO THE ASYMMETRIC UNIT" in val:
                coordinates = lines[a+3:i-1]      
                break
lattice_parameters = lattice_parameters.split()
parameter_dict = {}
parameter_dict['A'] = lattice_parameters[0]
parameter_dict['B'] = lattice_parameters[1]
parameter_dict['C'] = lattice_parameters[2]
parameter_dict['alpha'] = lattice_parameters[3]
parameter_dict['beta'] = lattice_parameters[4]
parameter_dict['gamma'] = lattice_parameters[5]
space_group_int = int(space_group)

with open("INPUT_" + output_file.replace(".out", '.txt'), "w+") as f:
    if space_group_int <= 2:
        print("Triclinic")
        
    elif space_group_int in range(3, 15):
        print(range(3,16))
        if space_group_int == 14:
            for i,val in enumerate(lines):
                if "_symmetry_space_group_name_H-M" in val:
                    space_group_name = val[1]
                    if space_group_name == "P21/c":
                        print("P21/c space group detected")
                    else:
                        print("WARNING")
                        print("Confirm space group")
        print("monoclinic")
        # check uniqeness of cell angles -- see CRYSTAL17 pg 20
        if alpha == gamma:
            print("Testing Uniqueness of angles")
            if alpha != beta:
                print("b unique")
                del parameter_dict["alpha"]
                del parameter_dict["gamma"]
        elif alpha == beta:
            print("Testing Uniquness of Angles")
            if alpha != gamma:
                print("c unique")
                del parameter_dict["alpha"]
                del parameter_dict["beta"]
        elif beta == gamma:
            print("Testing Uniquness of Angles")
            if alpha != beta:
                print("a unique")
                del parameter_dict["beta"]
                del parameter_dict["gamma"]


    elif space_group_int in range(16, 75):
            print("Orthorombic")
            del parameter_dict["alpha"]
            del parameter_dict["beta"]
            del parameter_dict["gamma"]

    elif space_group_int in range(75, 143):
            print("Tetragonal")
            del parameter_dict["B"]

    elif space_group_int in range(143,168):
            print("Trigonal")
            del parameter_dict["B"]

    elif space_group_int in range(168, 195):
            print("Hexagonal")
            del parameter_dict["B"]
    elif space_group_int in range(195, 231):
            print("Cubic")
            del parameter_dict["alpha"]
            del parameter_dict["beta"]
            del parameter_dict["gamma"]
            del parameter_dict["B"]
            del parameter_dict["C"]

    f.write(title)
    f.write("CRYSTAL\n" + "0 0 0\n")
    f.write(str(space_group_int) + "\n")
    for value in parameter_dict.values():
        f.write(value + " ")
    f.write("\n")    
    f.write(str(num_atoms))
    for line in coordinates:
        line = line.split()
        if "T" in line[1]:
            f.write(line[2] + " " + line[4] + " " + line[5] + " " + line[6] + "\n")
    f.write("FREQCALC\nINTENS\nEND\nEND\n")  
    for line in basis_data:
        f.write(line)   
    for line in scf_parmeters:
        f.write(line)