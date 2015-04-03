# python snippet to pull national elevation tiles from usgs

import webbrowser

base_url = 'http://tdds3.cr.usgs.gov/Ortho9/ned/ned_13/float/'
zip = '.zip'

tiles = [(44,122)]

for tile in tiles:
	northing = tile[0]
	westing = tile[1]
	url = base_url + 'n' + str(northing) + 'w' + str(westing) + zip
	print url
	webbrowser.open(url)