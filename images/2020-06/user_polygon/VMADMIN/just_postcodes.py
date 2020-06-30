import json

jsonFile = open("postcode_all.json")
pythonObject = json.load(jsonFile)

i = 0
while i < len(pythonObject['features']):
    postcode1 = pythonObject['features'][i]['properties']['POSTCODE']
    infected = ["3038", "3064", "3047", "3060", "3012", "3032", "3055", "3042", "3021", "3046"]
    if postcode1 not in infected:
        pythonObject['features'][i]['properties']['Stage3'] = "No"
        i += 1
    else:
        pythonObject['features'][i]['properties']['Stage3'] = "Yes"
        i += 1
'''
    j = i + 1
    while j < len(pythonObject['features']):
        postcode2 = pythonObject['features'][j]['properties']['POSTCODE']

        if postcode1 == postcode2:
            pythonObject['features'][i]['geometry']['coordinates'].append(pythonObject['features'][j]['geometry']['coordinates'])
            del pythonObject['features'][j]
        else:
            j += 1

    i += 1
del pythonObject['features'][i]

        # Keys to remove
        removeKey = ['type', 'suburb', 'ward_name', 'easting', 'northing', 'melway_ref', 'dbh_mm', 'Genus', 'Species']
        for key in range(len(removeKey)):
            obProp.pop(removeKey[key])'''


# Save name as bottom left corner lat long
#'''
fileName = 'postcode_1' + ".json"
writeFile = open(fileName, 'x')
json.dump(pythonObject, writeFile)
#'''
