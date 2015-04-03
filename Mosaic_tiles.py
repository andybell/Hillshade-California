# mosaic all of the NED tiles from USGS
import os
import arcpy

# create empty tile list to store tile paths
tile_list = []

#folder
dir_folder = r"C:\Users\ambell\Documents\NED"
output_name = "NED_Mosaic.tif"

# iterate over folders and add all files that end in ".flt" to the tile list
for root, dirs, files in os.walk(dir_folder):
	for file in files:
		if file.endswith(".flt"):
			print file
			tile_list.append(os.path.join(root, file))
			
			
# mosiac tiles to new raster 
arcpy.MosaicToNewRaster_management(tile_list, dir_folder, output_name,"#","32_BIT_SIGNED","#","1","BLEND","MATCH")			
