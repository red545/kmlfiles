import os
directory = '/Users/nik/Documents/LEADGEN/02_KML FILES GERMANY'
directory = '/Users/nik/Desktop/KML Files Test'
print 'Starting Convertion'

for filename in os.listdir(directory):
    print('in Loop')
    if filename.endswith(".shp"):
        newFilename =  filename.replace("plz-5stellig OGRGeoJSON Polygon_plz_", "")
        newFilename =  newFilename.replace(".shp", ".kml")
        newFile = os.path.join( newFilename)
        oldFile = os.path.join(directory, filename)

        newFile = newFile.replace("(","\\(").replace(")","\\)").replace(" ","\\ ")
        oldFile = oldFile.replace("(","\\(").replace(")","\\)").replace(" ","\\ ")

        print('NEW FILE: ' + newFile)
        os.system('ogr2ogr -f "KML" ' + newFile + ' ' + oldFile)
