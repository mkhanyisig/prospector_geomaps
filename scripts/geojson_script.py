"""
Prospector Geospatial Data
Create GeoJSON object from USGS data

"""


# load libraries
import pandas as pd
import csv
import json
from IPython.display import display
import time

df = pd.read_csv('MRDS Data.csv')
print("Shape:  ",df.shape)

def produce(sz):
    test=df.head(sz)

    result = test.to_json(orient="records") #  index labels are not preserved with this encoding
    parsed = json.loads(result)
    #print("JSON :\n")
    dump=json.dumps(parsed, indent=4)

    feature_arr=[]

    for obj in parsed:
        print("object: ",obj)
        arr_obj={}
        arr_obj.update({"type":"Feature"})
        arr_obj.update({"properties":obj})

        geometry={}
        geometry.update({"type":"Point"})
        geometry.update({"coordinates":[obj.get('longitude'),obj.get('latitude')]}) # needs fixing

        arr_obj.update({"geometry":geometry})

        feature_arr.append(arr_obj)

    geojson_obj={}
    geojson_obj.update({"type":"FeatureCollection"})
    geojson_obj.update({"features":feature_arr})

    outname="test_"+str(sz)+".json"

    output = open(outname, 'w')

    output.write(json.dumps(geojson_obj, indent=2))

    output.close()


def countryJSON(country):
    # loab object specifications from dataframe
    cnt=df[df['country']==country]
    print(country,"  shape: ",cnt.shape)

    result = cnt.to_json(orient="records") #  index labels are not preserved with this encoding
    parsed = json.loads(result)
    #print("JSON :\n")
    dump=json.dumps(parsed, indent=4)
    #print("Object: \n",dump)

    feature_arr=[]

    # build each feature object in country
    for obj in parsed:
        #print("object: ",obj)
        arr_obj={}
        arr_obj.update({"type":"Feature"})
        arr_obj.update({"properties":obj})

        geometry={}
        geometry.update({"type":"Point"})
        geometry.update({"coordinates":[obj.get('longitude'),obj.get('latitude')]}) # needs fixing

        arr_obj.update({"geometry":geometry})

        feature_arr.append(arr_obj)

    print("Total # items: ",len(feature_arr))

    geojson_obj={}
    geojson_obj.update({"type":"FeatureCollection"})
    geojson_obj.update({"features":feature_arr})

    fn=""
    fn+=country+".json"
    fn=fn.replace(" ","_")

    # export file
    output = open(fn, 'w')

    output.write(json.dumps(geojson_obj, indent=2))

    output.close()

########### main function

## Test 1 -> produce GEOJSON from first n rows
print("starting")
produce(1000)


# test 2 produce GeoJSON for country
print("Test #2")
nm="Belize"
countryJSON(nm)
