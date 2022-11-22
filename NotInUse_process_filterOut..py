import csv
import json
import os


def filterNotInWorkforce(inputFile):
    inputData = csv.reader(open('/Users/jzhang/Documents/whoWorks/splits/'+inputFile+'.csv','r'))
    outputFile = csv.writer(open('/Users/jzhang/Documents/whoWorks/splits/'+inputFile+'_inWorkforce.csv','w'))
    for row in inputData:
        header = row
        outputFile.writerow(row)
        break
    for row in inputData:
        employementValue = row[header.index("prwksch")]
        if employementValue!="0":
            outputFile.writerow(row)
            
#filterNotInWorkforce('16-A')



    

#makeCombinations()
def filterOutNoninterviews():
    data = csv.reader(open('/Users/jzhang/Documents/whoWorks/cps_94/cps_94.csv','r'))
    newData = csv.writer(open('cps_94_hrintsta_1.csv','w'))
    for row in data:
       # print(row)
        print(len(row))
        print(row)
        header = row
        newData.writerow(header)
        break
    count = 0
    for row in data:
        # print(row)
 #        break
       # print(row[header.index('hrintsta')])
        if row[header.index('hrintsta')]=="1":
            #print(row)
            newData.writerow(row)
            count+=1
            if count%10000==0:
                print(count)

#filterOutNoninterviews()



def filterOutByColumnValue(column,value):
    data = csv.reader(open('/Users/jzhang/Documents/whoWorks/cps_94/cps_94.csv','r'))
    newData = csv.writer(open('cps_94_'+column+"_"+value+'.csv','w'))
    for row in data:
       # print(row)
        print(len(row))
        print(row)
        header = row
        newData.writerow(header)
        break
    count = 0
    for row in data:
        # print(row)
 #        break
       # print(row[header.index('hrintsta')])
        if row[header.index(column)]==value:
            #print(row)
            newData.writerow(row)
            count+=1
            if count%1000==0:
                print(count)

#PEDWRSN 6 
#PEABSRSN 6	CHILD CARE PROBLEMS
#PRABSREA		2		REASON NOT AT WORK AND PAY STATUS 							385 - 386
#						3	FT PAID-CHILD CARE PROBLEMS

#PREMPHRS		2		REASON NOT AT WORK OR HOURS AT WORK							391 - 392
#
#						5	W/JOB, NOT AT WORK-CHILD CARE PROBLEMS
#
# #filterOutByColumnValue("pedwrsn","6")
# #filterOutByColumnValue("peabsrsn","6")
# filterOutByColumnValue("prabsrea","3")
# filterOutByColumnValue("prabsrea","33")
# #filterOutByColumnValue("premphrs","5")

def filterColumns():
    data = csv.reader(open('/Users/jzhang/Documents/whoWorks/cps_94_hrintsta_1.csv','r'))
    keysFile = json.load(open('/Users/jzhang/Documents/whoWorks/reduced_keys_11102022.json','r'))
    focusColumns = list(keysFile.keys())
    print(focusColumns)
    
    
    
    outputFile = csv.writer(open('/Users/jzhang/Documents/whoWorks/reduced_11102022.csv','w'))
    
    for row in data:
       # print(row)
        print(len(row))
        header = row
        newHeader = []
        for h in header:
            #print(h.upper())
            if h.upper() in focusColumns:
                print(h)
                newHeader.append(h)
        outputFile.writerow(newHeader)
        break
      # print(count)
    print(len(focusColumns))
    lineNumber = 0
    validCount = 0
    for row in data:
        lineNumber+=1
        newRow = []
        undefinedRow = "false"
        
        for h in header:
            #print(h.upper())
            if h.upper() in focusColumns:
                value = row[header.index(h)]
                if value=="undefined" or value=="":
                    undefinedRow="true"
                
                newRow.append(value)
                
        if undefinedRow=="false":
            validCount+=1
            outputFile.writerow(newRow)
        if lineNumber%10000==0:
            print(lineNumber,validCount)
       
        
filterColumns()
