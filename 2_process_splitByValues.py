import csv
import json
import os

#filter to only age 16 and above
def over16(key,threshold,inputFile):
    print(key, threshold,inputFile)
    inputRoot = '/Users/jzhang/Documents/whoWorks/splits_combo/'
    outputRoot = '/Users/jzhang/Documents/whoWorks/splits_combo_2/'
    
    inputData = csv.reader(open(inputFile,'r'))
    
    count = 0
    valid = 0
    for row in inputData:
        header = row
        print(header)
        break
        
   
    outputFileName ="/Users/jzhang/Documents/whoWorks/11172022_hrinsta1_allColumns_16AndOver.csv"
        
    outputFile = csv.writer(open(outputFileName,"w"))

    outputFile.writerow(header)

    for row in inputData:
        count+=1
        
        if row[header.index(key)].isnumeric() and row[header.index('hrintsta')]=="1":
            splitValue = int(row[header.index(key)])
            #print(splitValue)
            if splitValue>= threshold:
                valid +=1
                outputFile.writerow(row)
        if count%10000==0:
            print (count, valid, round(valid/count*10000)/100)


def splitByThresholds(key,threshold,inputFile,inputBase):
    print(key, threshold,inputFile)
    outputRoot = '/Users/jzhang/Documents/whoWorks/groupings'
    
    inputData = csv.reader(open(inputFile,'r'))
    
    count = 0
    valid = 0
    for row in inputData:
        header = row
        break
        
   
    outputFileName =outputRoot+"/"+inputBase+"_"+key+"-"+str(threshold[0])+"-"+str(threshold[1])+".csv"
        
    outputFile = csv.writer(open(outputFileName,"w"))

    outputFile.writerow(header)

    for row in inputData:
        count+=1
        
        if row[header.index(key)].isnumeric():
            splitValue = int(row[header.index(key)])
            #print(splitValue)
            if splitValue>= threshold[0] and splitValue<=threshold[1]:
                valid +=1
                outputFile.writerow(row)
            if count%100000==0:
                print (count, valid, round(valid/count*10000)/100)


def splitByListOfValues(key,threshold,inputFile,inputBase,outFileName):
    print(key, threshold,inputFile)
    outputRoot = '/Users/jzhang/Documents/whoWorks/groupings'
    
    inputData = csv.reader(open(inputFile,'r'))
    
    count = 0
    valid = 0
    for row in inputData:
        header = row
        break
        
   
    outputFileName =outputRoot+"/"+inputBase+"_"+key+"-"+outFileName+".csv"
        
    outputFile = csv.writer(open(outputFileName,"w"))

    outputFile.writerow(header)

    for row in inputData:
        count+=1
        
        if row[header.index(key)].isnumeric():
            splitValue = int(row[header.index(key)])
            #print(splitValue)
            if splitValue in threshold:
                valid +=1
                outputFile.writerow(row)
            if count%100000==0:
                print (count, valid, round(valid/count*10000)/100)


#Steps
# percent of employed absent
#percent of absent because of childcare
#percent of childcare with young
#percent of childcare by education
#percent of childcare by race
#percent of childcare by gender

#PREMPNOT - 1 	EMPLOYED / 2	UNEMPLOYED

##KEYS
peeduca = [{"key":'peeduca',"threshold":[39,9999]},{"key":'peeduca',"threshold":[0,38]},{"key":'peeduca',"threshold":[0,40]},{"key":'peeduca',"threshold":[41,9999]},{"key":'peeduca',"threshold":[0,42]},{"key":'peeduca',"threshold":[43,9999]}]
pesex = [{"key":'pesex',"threshold":[2,2]},{"key":'pesex',"threshold":[1,1]}]
ptdtrace = [{"key":"ptdtrace","threshold":[1,1]},{"key":"ptdtrace","threshold":[2,2]},{"key":"ptdtrace","threshold":[3,3]},{"key":"ptdtrace","threshold":[4,4]},{"key":"ptdtrace","threshold":[5,5]},{"key":"ptdtrace","threshold":[6,9999]}]
prtage=[{"key":"prtage","threshold":[16,19]},{"key":"prtage","threshold":[20,29]},{"key":"prtage","threshold":[30,39]},{"key":"prtage","threshold":[40,49]},{"key":"prtage","threshold":[50,9999]}]

prchld=[{"key":'prchld',"threshold":[1,2,5,6,7,8,9,11,12,13,14,15],"label":"0-5andOther"},
{"key":'prchld',"threshold":[1,5,6,7,11,12,13,15],"label":"0-2andOther"},
{"key":'prchld',"threshold":[2,5,8,9,11,12,14,15],"label":"3-5andOther"},
{"key":'prchld',"threshold":[3,4,10],"label":"childrenOver5Only"}]

prmjind1 = [
    {"key":"prmjind1","threshold":[1,1],"label":"Agriculture"},
    {"key":"prmjind1","threshold":[2,2],"label":"Mining"},
    {"key":"prmjind1","threshold":[3,3],"label":"construction"},
    {"key":"prmjind1","threshold":[4,4],"label":"manufacturing"},
    {"key":"prmjind1","threshold":[5,5],"label":"wholesale retail"},
    {"key":"prmjind1","threshold":[6,6],"label":"transportation utilities"},
    {"key":"prmjind1","threshold":[7,7],"label":"information"},
    {"key":"prmjind1","threshold":[8,8],"label":"financial activities"},
    {"key":"prmjind1","threshold":[9,9],"label":"profssional_business"},
    {"key":"prmjind1","threshold":[10,10],"label":"education_health"},
    {"key":"prmjind1","threshold":[11,11],"label":"leisure_hospitality"},
    {"key":"prmjind1","threshold":[13,13],"label":"public admin"}
]

prnmchld= [{"key":'prnmchld',"threshold":[0,0]},{"key":'prnmchld',"threshold":[1,9999]},{"key":'prnmchld',"threshold":[1,1]},{"key":'prnmchld',"threshold":[2,2]},{"key":'prnmchld',"threshold":[2,9999]},{"key":'prnmchld',"threshold":[3,3]}]
peabsrsn = {"key":"peabsrsn","threshold":[6,6]}
pemlr ={"key":"pemlr","threshold":[1,1]}
##END KEYS


#step 0 get 16 and over within valid interviews
everyone = "/Users/jzhang/Documents/whoWorks/11172022_hrinsta1_allColumns.csv"
#over16('prtage',16,everyone)

#step 1 split by employed not at work
inputBase = "16AndOver"
#splitByThresholds(pemlr['key'],pemlr['threshold'],'/Users/jzhang/Documents/whoWorks/11172022_hrinsta1_allColumns_16AndOver.csv',inputBase)

#step 2 all employed
inputBase = "16AndOver"
#splitByThresholds('prempnot',[1,1],'/Users/jzhang/Documents/whoWorks/hrinsta1_allColumns_16AndOver.csv',inputBase)

# step 3 split by not at work because of parenting
inputBase = "pemlr-2-2"
#splitByThresholds(peabsrsn['key'],peabsrsn['threshold'],'/Users/jzhang/Documents/whoWorks/groupings/16AndOver_pemlr-2-2.csv',inputBase)


#step 4 split by all other
#pesex,
#prnmchld,prchld,ptdtrace,prtage,
allCats = [prnmchld]
count = 0
for splits in allCats:
    for s in splits:
        count+=1
        print(s['key'],s['threshold'])
        splitByThresholds(s["key"],s["threshold"],'/Users/jzhang/Documents/whoWorks/groupings/pemlr-2-2_peabsrsn-6-6.csv',"peabsrsn-6-6")
        splitByThresholds(s["key"], s["threshold"],'/Users/jzhang/Documents/whoWorks/groupings/16AndOver_prempnot-1-1.csv',"prempnot-1-1")
        splitByThresholds(s["key"], s["threshold"],'/Users/jzhang/Documents/whoWorks/groupings/16AndOver_pemlr-2-2.csv',"pemlr-2-2")
# break
#print(count)
#
