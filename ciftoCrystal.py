# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 11:16:39 2019

@author: raysc
"""

# Check final input to ensure compatibility with CRYSTAL
# Check lattice parameters and make sure only what CRYSTAL needs are present
# Required inputs below

##############################################
##############################################
import os
import glob
from periodictable import elements
from BSEtoCrystal import GetBasisData
from getAtoms import getAtoms



def getINPUT(title, basis, functional, shrink, tolinteg, toldee):



elif "_cell_length_a" in value:
A = val[1]
parameter_dict["A"] = A
elif "_cell_length_b" in value:
B = val[1]
parameter_dict["B"] = B
elif "_cell_length_c" in value:
C = val[1]
parameter_dict["C"] = C
elif "_cell_angle_alpha" in value:
alpha = val[1]
parameter_dict["alpha"] = alpha
elif "_cell_angle_beta" in value:
beta = val[1]
parameter_dict["beta"] = beta
elif "_cell_angle_gamma" in value:
gamma = val[1]
parameter_dict["gamma"] = gamma

# edit lattice parameters based on space group
if space_group_int <= 2:
print("Triclinic")
continue
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
except UnboundLocalError:
space_group= "N/A"
continue
coordinates = {}
for i,val in enumerate(lines):
if "_atom_site_fract_z" in val:
x = i
del lines[0:x+1]

for i,val in enumerate(lines):
if "loop_" in val:
x = i
del lines[x:len(lines)]

for item in lines:
try:
atom = item[0]
x = item[2]
y = item[3]
z = item[4]
coordinates[atom] = [x,y,z]
except IndexError:
continue

# clean coordinates
atomic_number_coordinates = []

for atom in elements:
for key,value in coordinates.items():

if atom.symbol in key:

key = str(atom.number)
new_coordinates = key + " " + str(value)
new_coordinates = new_coordinates.replace(",", " ")
new_coordinates = new_coordinates.replace("[", "")
new_coordinates = new_coordinates.replace("]", "")
new_coordinates = new_coordinates.replace("'", "")
atomic_number_coordinates.append(new_coordinates)





with open("INPUT_" + cif_file.name.replace(".cif", ".txt"), "w+") as f:
f.write(title + "\n")
f.write("CRYSTAL" + "\n")
f.write("0 0 0" + "\n")
f.write(space_group + "\n")
for key,value in parameter_dict.items():
f.write(value + " ")
f.write("\n")
f.write(str(len(atomic_number_coordinates))+"\n")
for line in atomic_number_coordinates:
f.write(" " + line + "\n")

# Write calculation parameters here
for line in calculationtype:
if calctype == "Single Point Energy":
break
else:
f.write(line + '\n')

f.write("END")
# f.write("\n")

if atom_override == "Zr":
f.write("\n")
with open("Zr_Basis_data.txt", "r") as zr_basis_data:
lines = zr_basis_data.readlines()
for line in lines:
f.write(line)

f.write("\n")
for line in basis_data:
f.write(line)



with open("INPUT_"+ cif_file.name.replace(".cif", ".txt"), "r+") as clean_input_file:
lines = clean_input_file.readlines()
for i,val in enumerate(lines):
if "!" in val:
del lines[i]

# write keywords to end of input file
with open("INPUT_"+ cif_file.name.replace(".cif", ".txt"), "w+") as clean_input_file:
clean_input_file.writelines(lines)
clean_input_file.write("99 0" + "\n" + "END" + "\n" + "DFT" + "\n" + str(functional) + "\n" + "XLGRID" + "\n" + "END" + "\n" + "PPAN\n" + "MAXCYCLE\n" + "200\n"  + "SHRINK" + "\n" + str(shrink) + " " + str(shrink) + "\n" + "TOLDEE" + "\n" + str(toldee) + "\n" + "TOLINTEG" + "\n" + tolinteg + "\n" + "END")

if os.path.exists("response.txt"):
os.remove("response.txt")
if os.path.exists("basis_data.txt"):
os.remove("basis_data.txt")
if os.path.exists("clean_lines.txt"):
os.remove("clean_lines.txt")


input_dict = {}
# print(cif_file.name)

for file_name in os.listdir(directory):

file_list = glob.glob("INPUT_*")

for cif in os.listdir(directory):

cif_file_list = glob.glob("*.cif")

for item in cif_file_list:
os.remove(item)


for filename in file_list:

with open(filename, "r") as f:
lines = f.readlines()
input_dict[filename] = lines
os.remove(filename)
return input_dict
































