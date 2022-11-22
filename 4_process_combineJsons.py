import csv
import json
import os

def combine(folder):
    files = os.listdir(folder)
    formatted = {}
    for f in files:
        print(f)
        if f!=".DS_Store":
            key = f.replace(".json","")
            print(key)
            fileData = json.load(open(folder+f,'r'))
            print(fileData)
            formatted[key]=fileData
    
    outFile = open("combinedJsons_11212022.json",'w')
    json.dump(formatted,outFile)
    return formatted

combine("/Users/jzhang/Documents/whoWorks/groupings_timeline/")