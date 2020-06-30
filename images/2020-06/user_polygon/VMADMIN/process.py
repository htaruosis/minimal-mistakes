import json

jsonFile = open("POSTCODE_POLYGON.geojson")
pythonObject = json.load(jsonFile)

i = 0
while i < len(pythonObject['features']):
    postcode1 = pythonObject['features'][i]['properties']['POSTCODE']

    j = i + 1
    while j < len(pythonObject['features']):
        postcode2 = pythonObject['features'][j]['properties']['POSTCODE']

        if postcode1 == postcode2:
            pythonObject['features'][i]['geometry']['coordinates'].append(pythonObject['features'][j]['geometry']['coordinates'])
            del pythonObject['features'][j]
        else:
            j += 1

    i += 1

'''
        # Keys to remove
        removeKey = ['type', 'suburb', 'ward_name', 'easting', 'northing', 'melway_ref', 'dbh_mm', 'Genus', 'Species']
        for key in range(len(removeKey)):
            obProp.pop(removeKey[key])'''


# Save name as bottom left corner lat long
#'''
fileName = 'postcode_processed' + ".geojson"
writeFile = open(fileName, 'x')
json.dump(pythonObject, writeFile)
#'''
