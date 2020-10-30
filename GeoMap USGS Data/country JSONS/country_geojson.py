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
    print("##    ",country,"  shape: ",cnt.shape)

    result = cnt.to_json(orient="records") #  index labels are not preserved with this encoding
    parsed = json.loads(result)
    #print("JSON :\n")
    dump=json.dumps(parsed, indent=4)
    #print("Object: \n",dump)

    feature_arr=[]

    # build each feature object in country
    for obj in parsed:
        #print("object: ",obj)
        print("\n************** New Object ********************")
        arr_obj={}
        arr_obj.update({"type":"Feature"})

        # add mineral tags
        min1=obj.get('commod1')
        min2=obj.get('commod2')
        min3=obj.get('commod3')

        mineral_tags=set()

        #print("\n***\n")
        # first tag
        if min1!=None:
            print("1: =>",min1)
            min1=min1.split(",")
            temp=[]
            for el in min1:
                el=el.replace(" ","")
                el=el.lower()
                temp.append(el)
                mineral_tags.add(el)
            print(temp)
        # second tag
        if min2!=None:
            print("2: =>",min2)
            min2=min2.split(",")
            temp=[]
            for el in min2:
                el=el.replace(" ","")
                el=el.lower()
                temp.append(el)
                mineral_tags.add(el)
            print(temp)
        # second tag
        if min3!=None:
            print("3: =>",min3)
            min3=min3.split(",")
            temp=[]
            for el in min3:
                el=el.replace(" ","")
                el=el.lower()
                temp.append(el)
                mineral_tags.add(el)
            print(temp)

        print("Minerals: ",list(mineral_tags))
        mineral_tags=list(mineral_tags)
        # add tag
        obj.update({"mineral_tags":mineral_tags})

        # update properties object
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
    fn=fn.lower()

    # export file
    output = open(fn, 'w')

    output.write(json.dumps(geojson_obj, indent=2))

    output.close()

########### main function

# test 1 produce GeoJSON for country
print("Test #1 => Belize")
nm="Belize"
countryJSON(nm)


# test 2 => latin amrican countries
print("Main function => countries data to GeoJSON")

north_america=["Belize","Costa Rica", "El Savador","Guatemala","Honduras","Mexico","Nicaragua","Panama"]
south_america=["Argentina","Bolivia","Brazil","Chile","Colombia","Ecuador","French Guiana","Guyana","Paraguay","Peru","Suriname","Uruguay","Venezuela"]
carribean=["Cuba","Dominican Republic","Haiti"]

for country in north_america:
    countryJSON(country)

for country in south_america:
    countryJSON(country)

for country in carribean:
    countryJSON(country)


#countryJSON("Belize")
