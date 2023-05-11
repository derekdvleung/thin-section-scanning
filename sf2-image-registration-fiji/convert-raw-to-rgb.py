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

# This Fiji/ImageJ python script can be used to convert 48 bit 
# *.tif images into 24-bit rgb images. This is useful since most 
# applications do not need 24 bit depth after image preprocessing.

# The script also adds information for images scanned in 7,200 dpi.
# If scanning under different resolution, change the "distance=7200"
# parameter.

# Instructions:
# Drag and drop this file into Fiji/ImageJ. The macro editor will
# open. Press "Run" and a dialog box will open, prompting for a tif
# image that will be saved as a 24 bit tif. After an image is selected,
# another dialog box will open for the next image. Continue selecting
# images until done. When done, press cancel to exit the script.

from os import path, listdir
import os
from ij import IJ
from ij.io import OpenDialog
from ij.io import FileSaver


# asks for the first file name
od = OpenDialog("Choose a file", None)
filename = od.getFileName()


#terminates if no file name is given
while filename is not None:
	directory = od.getDirectory()
	filepath = directory + filename
	print filepath
	image = IJ.openImage(filepath)
	#image.show()

    # converts image into 24 bit image
	IJ.run (image, "RGB Color", "")
	IJ.run (image, "Set Scale...", "distance=7200 known=25.4 unit=mm")
	# add "rgb" to the image name
	newFilename = filename.rstrip(".tif") + "-rgb.tif"
	fs = FileSaver (image)
    
    # saves tif to same directory
	fs.saveAsTiff(directory + newFilename)
	print newFilename

    # asks for a new file name
	od = OpenDialog("Choose another file. Cancel to exit.", None)
	filename = od.getFileName()

# if no file name is given, then the script ends
print "User cancelled the dialog!"