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
        break
        
   
    outputFileName ="/Users/jzhang/Documents/whoWorks/cps_1994_hrinststa_1_16AndOver.csv"
        
    outputFile = csv.writer(open(outputFileName,"w"))

    outputFile.writerow(header)

    for row in inputData:
        count+=1
        
        if row[header.index(key)].isnumeric():
            splitValue = int(row[header.index(key)])
            #print(splitValue)
            if splitValue>= threshold:
                valid +=1
                outputFile.writerow(row)
        if count%10000==0:
            print (count, valid, round(valid/count*10000)/100)

#everyone = "/Users/jzhang/Documents/whoWorks/cps_94_hrintsta_1.csv"
#over16('prtage',16,everyone)


def splitByThresholds(key,threshold,inputFile):
    print(key, threshold,inputFile)
    outputRoot = '/Users/jzhang/Documents/whoWorks/groupings_absence'
    
    inputData = csv.reader(open(inputFile,'r'))
    
    count = 0
    valid = 0
    for row in inputData:
        header = row
        break
        
   
    outputFileName =outputRoot+"/"+key+"-"+str(threshold[0])+"-"+str(threshold[1])+".csv"
        
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

#PEABSRSN 6 CHILD CARE PROBLEMS

#splitByThresholds('peabsrsn',"threshold":[6,6],'/Users/jzhang/Documents/whoWorks/reduced_11102022_pemlr2_hrinsta1_prtage16Plus.csv')


# peeduca = [{"key":'peeduca',"threshold":[39,9999]},{"key":'peeduca',"threshold":[0,38]},{"key":'peeduca',"threshold":[0,40]},{"key":'peeduca',"threshold":[41,9999]},{"key":'peeduca',"threshold":[0,42]},{"key":'peeduca',"threshold":[43,9999]}]
# pesex = [{"key":'pesex',"threshold":[2,2]},{"key":'pesex',"threshold":[1,1]}]
# prnmchld= [{"key":'prnmchld',"threshold":[0,0]},{"key":'prnmchld',"threshold":[1,9999]},{"key":'prnmchld',"threshold":[1,1]},{"key":'prnmchld',"threshold":[2,9999]}]
# prchld=[{"key":'prchld',"threshold":[1,1]},{"key":'prchld',"threshold":[1,2]},{"key":'prchld',"threshold":[3,9999]}]
# ptdtrace = [{"key":"ptdtrace","threshold":[1,1]},{"key":"ptdtrace","threshold":[2,2]},{"key":"ptdtrace","threshold":[3,3]},{"key":"ptdtrace","threshold":[4,4]},{"key":"ptdtrace","threshold":[5,5]},{"key":"ptdtrace","threshold":[6,9999]}]
# prtage=[{"key":"prtage","threshold":[16,19]},{"key":"prtage","threshold":[20,49]},{"key":"prtage","threshold":[50,9999]}]
#
# peabsrsn = [{"key":"peabsrsn","threshold":[6,6]}]
# peabsrsn = [{"peabsrsn":[6,6]}]
inputFile = '/Users/jzhang/Documents/whoWorks/groupings/reduced_11102022_hrinsta1_prtage16Plus.csv'
#inputFile = '/Users/jzhang/Documents/whoWorks/cps_94/cps_94.csv'
#
# for splits in prtage:
#     print (splits)
#     splitByThresholds(splits["key"], splits["threshold"],inputFile)
   # break
    
##splitByThresholds("pemlr",[2,2],inputFile)

inputFile = '/Users/jzhang/Documents/whoWorks/groupings_absence/pemlr-2-2.csv'
splitByThresholds("peabsrsn",[6,6],inputFile)

#isolateBy ={"ptdtrace":1,"ptdtrace":2,"ptdtrace":3,"ptdtrace":4,"ptdtrace":5,"ptdtrace":6}
#groupBy = ["prtage"]


               # break
   # break
#
#
# combinationsAll = []
# for l in columns:
#    # combinationsAll.append(l)
#     for l2 in columns:
#         if l!=l2:
#             combinationsAll= combinationsAll+list(itertools.product(l,l2))
#             # for l3 in columns:
# #                 if l!=l2 and l!=l3 and l2!=l3:
# #                     combinationsAll= combinationsAll+list(itertools.product(l,l2,l3))
#                     #break
#             #break
# print(len(combinationsAll))
#
# #split('prchld',"threshold":[0,0],"prtage-16-A")
# split('prchld',"threshold":[-1,0],"prtage-16-A")
# print(combinationsAll[20])
#for c in combinationsAll:
#     print(c)
   # break
#firstLastCombo = [splitBy[0]]+[splitBy[2]]
#print(firstLastCombo)
#list(itertools.product(*firstLastCombo))+ list(itertools.product(*splitBy[0:2]))+ list(itertools.product(*splitBy[1:]))
#combinations =list(itertools.product(peeduca,pesex,prnmchld,prchld,ptdtrace,prtage))
#print(len(combinations))
#split("prtage",16,"reduced_11012022")
#
# for i in combinationsAll:
#     print(i)
#     for c in i:
#         # print(c)
#   #       print(c.keys())
#         key = list(c.keys())[0]
#         value = list(c.values())[0]
#         print(key,value)
#         split(key,value,"prtage-16-A")

#
# startingInput = "prtage-16-A"
# for c in combinationsAll:
#   #  print(c)
#     inputFile = "prtage-16-A"
#     for i in c:
#         # print(i)
#         key = list(i.keys())[0]
#         value = list(i.values())[0]
#        # print(key, value)
#         # inputFile+=key+"-"+str(value)
#         # print(inputFile)
#         outputFileName = split(key,value,inputFile)
#        # print(outputFileName)
#         inputFile = outputFileName
#
#
 
 
        # if inputFile=="reduced_11012022":
  #           inputFile = key+"-"+str(value)+"-A"
  #       else:
  #           inputFile += "_"+key+"-"+str(value)+"-A"
  #       print(inputFile)
        
    #break
        

# for s in splitBy:
#    print(s)


