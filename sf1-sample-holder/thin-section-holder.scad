/* Copyright (C) 2023 Derek Leung <derekdvleung@gmail.com>
    This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License version 3 as published by the Free Software Foundation. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/


// thin-section dimensions
ptsLength = 47; //77;//long section
ptsWidth = 28;

// holder dimensions
holderLength = 130; //170;//long section
holderWidth = 62;
holderThickness = 6;

// this shifts the location of the window with respect to the centre of the holder
ptsShiftY = 24; // to provide a handle for the user to take in and pull out samples
ptsShiftX = 0.75; // because the window on the Plustek is slightly offset

// height at which thin section rests on the sample holder (in mm). For our tests, we found 2.4 mm to be best for the non-polarized light setup and 2.6 mm to be best for the circularly polarized light setup
level = 2.4;

// engraves the version number onto the sample holder.
versionNumber = "2021-10-14";


// inset edge
translate([ptsShiftX,ptsShiftY+ptsLength/2-1.6/2,  -holderThickness/2+level/2])
cube ([ptsWidth,3.2,level], center = true);

// inset edge
translate([ptsShiftX,ptsShiftY-ptsLength/2+1.6/2,  -holderThickness/2+level/2])
cube ([ptsWidth,3.2,level], center = true);

// bottom polarizer ledge
translate([ptsShiftX,ptsShiftY+ptsLength/2-4/2, -holderThickness/2+0.4/2])
cube ([ptsWidth,4,0.4], center = true);

translate([ptsShiftX,ptsShiftY-ptsLength/2+4/2,  -holderThickness/2+0.4/2])
cube ([ptsWidth,4,0.4], center = true);

difference(){
	union(){
		// slide holder
		cube([holderWidth,holderLength,holderThickness], center = true);
	}
	
	//bevelled corners of slide holder
		translate([holderWidth/2,-holderLength/2, 0])
		rotate([0,0,45])
		cube ([4,4,10], center = true);
		translate([-holderWidth/2,holderLength/2, 0])
		rotate([0,0,45])
		cube ([4,4,10], center = true);
		translate([-holderWidth/2,-holderLength/2, 0])
		rotate([0,0,45])
		cube ([4,4,10], center = true);
		translate([holderWidth/2,holderLength/2, 0])
		rotate([0,0,45])
		cube ([4,4,10], center = true);
	
	translate([0+ptsShiftX,ptsShiftY,0]){
		
		//thin section size
		cube([ptsWidth, ptsLength, 10], center = true);
	}
	
	
		//depth label
		translate([0,-40,holderThickness/2-0.4])
		linear_extrude(height = 0.8)
		text(str(level, " mm"), halign = "center", size = 8);
	
		//version label
		translate([0,-50,holderThickness/2-0.4])
		linear_extrude(height = 0.8)
		text(str(versionNumber), halign = "center", size = 6);
	
		translate([-holderWidth/2,ptsShiftY, 0])
		rotate([0,0,45])
		cube ([4,4,10], center = true);
		translate([holderWidth/2,ptsShiftY, 0])
		rotate([0,0,45])
		cube ([4,4,10], center = true);
		translate([ptsShiftX, ptsLength/2+ptsShiftY, 0])
		cylinder(r = 7, h = 10, center = true);
		translate([ptsShiftX, -ptsLength/2+ptsShiftY, 0])
		cylinder(r = 7, h = 10, center = true);
}

