import csv
import json
import os

#STEPS

#get total weighted pop for each month for each file

#https://www.census.gov/programs-surveys/cps/technical-documentation/methodology/producing-summary-statistics.html
def timeline(inputFile):
    print(inputFile)
    inputData = csv.reader(open(inputRoot+"/"+inputFile+'.csv','r'))
    for row in inputData:
        header = row
       # print(header)
        break
    formatted = {}
    noWeightCount = 0
    for row in inputData:
        #print(row)
        if row[header.index('prpertyp')]=='2': #ADULT CIVILIAN HOUSEHOLD MEMBER

            weight = row[header.index('pwcmpwgt')]#Composited Final Weight-4 decimals
            if weight !="":
                weight = float(weight)/10000
            else:
                noWeightCount+=1
               
        
       
            year = row[header.index('hryear4')]
            
            month = row[header.index('hrmonth')]
           # workStatus = row[header.index('prwksch')]
            yearMonth = year+"-"+month
        
            if yearMonth not in formatted.keys():
                formatted[yearMonth]={}
                formatted[yearMonth]["weighted"]=weight
                formatted[yearMonth]["yearMonth"]=yearMonth
                #formatted[yearMonth]["interviewed"]=1
            
            else:
               # formatted[yearMonth]["interviewed"]+=1
                formatted[yearMonth]["weighted"]+=weight
    print("NO WEIGHT", noWeightCount)
            
    
    outputFile = open(outputRoot+"/"+inputFile+".json",'w')
    json.dump(formatted,outputFile)
    

    # withYearMonthKeys=[]
 #    for f in formatted:
 #        #print(f)
 #        yearMonth = f
 #        entry = formatted[f]
 #        entry["yearMonth"]=yearMonth
 #        withYearMonthKeys.append(entry)
 #       # break
 #    #print(withYearMonthKeys)
 #
 #    json.dump(withYearMonthKeys,outputFile)

#inputRoot = '/Users/jzhang/Documents/whoWorks'
    
inputRoot = '/Users/jzhang/Documents/whoWorks/groupings'
outputRoot = inputRoot+"_timeline"
#timeline('reduced_11102022_hrinsta1_prtage16Plus')  
# inputRoot ='/Users/jzhang/Documents/whoWorks/groupings/'
#timeline('pemlr-2-2')

# timeline('peabsrsn-6-6')

#print(outputRoot)
files = os.listdir(inputRoot)

tally = {}
# timeline("reduced_11012022")
# timeline("prtage-16-A")
#print(files)
for f in files:
    if f!=".DS_Store":
        timeline(f.replace(".csv",""))
    #break
     
 
 
 
 
 