# Copyright (C) 2023 Derek Leung <derekdvleung@gmail.com>
# This program is free software: you can redistribute it 
# and/or modify it under the terms of the GNU General Public 
# License version 3 as published by the Free Software 
# Foundation. This program is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY; without even the 
# implied warranty of MERCHANTABILITY or FITNESS FOR A 
# PARTICULAR PURPOSE.  See the GNU General Public License for 
# more details. You should have received a copy of the GNU 
# General Public License along with this program.  If not, see 
# <https://www.gnu.org/licenses/>.

from register_virtual_stack import Register_Virtual_Stack_MT
from ij.io import DirectoryChooser
from os import path, listdir
import os

dir = DirectoryChooser ("enter the input directory")
folder = dir.getDirectory()
print (folder)

# source directory
source_dir = folder + "rgb/"

# if source directory exists, proceed. Otherwise, skip it and print a note
if path.isdir(source_dir):

	# output directory
	target_dir = folder + "stacked/"
	if not path.exists(target_dir) and not path.isdir(target_dir):
		os.mkdir(target_dir)
	#print(target_dir)
	
		
	# transforms directory (not needed)
	#transf_dir = folder + sampleNames + "/stacked/transform/"
	#if not path.exists(transf_dir) and not path.isdir(transf_dir):
	#	os.mkdir(transf_dir)
	# reference image

	reference_name = listdir(folder + "rgb/")
	
	for filename in listdir(folder +"rgb/"):
		if filename.find("nopol") != -1:		
			reference_name = filename
	
	print(reference_name)
	
	# shrinkage option (false)
	use_shrinking_constraint = 0
	
	p = Register_Virtual_Stack_MT.Param()
	# The "maximum image size":
	p.sift.maxOctaveSize = 1024
	# The "inlier ratio":
	p.minInlierRatio = 0.05
	# Detect features using an (1) a rigid model, affine model (3)
	p.featuresModelIndex = 3
	# Use moving least squares to align (5)
	# Note that technically a rigid transformation should be used (1)
	# but the cpl images are sufficiently different, so the nopol image is used as a reference
	p.registrationModelIndex = 5
	# The maxiumum error in alignment. Lower means better alignment, but if too low, then the alignment fails
	#p.maxEpsilon = 3
	

	Register_Virtual_Stack_MT.exec(source_dir, target_dir, None, 
	reference_name, p, use_shrinking_constraint)