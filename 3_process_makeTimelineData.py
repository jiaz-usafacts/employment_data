import csv
import json
import os

#STEPS

#get weighted pop for each month
#get percentage of weighted pop for people not at work because of childcare
#get percentage of groups within childcare

#https://www.census.gov/programs-surveys/cps/technical-documentation/methodology/producing-summary-statistics.html
def timeline(inputFile):
    print(inputFile)
    inputData = csv.reader(open(inputRoot+"/"+inputFile+'.csv','r'))
    for row in inputData:
        header = row
        print(header)
        break
    formatted = {}
    for row in inputData:
        #print(row)
        if row[header.index('prpertyp')]=='2':
            weight = row[header.index('pwcmpwgt')]
            if weight !="":
                weight = float(weight)/10000
            else:
                weight = 0
          #  print(weight)
        
     #
     #        print( float(weight))
        
       
            year = row[header.index('hryear4')]
            
            month = row[header.index('hrmonth')]
            workStatus = row[header.index('prwksch')]
            yearMonth = year+"-"+month
        
            if yearMonth not in formatted.keys():
                formatted[yearMonth]={}
                formatted[yearMonth]["weighted"]=weight
                formatted[yearMonth]["yearMonth"]=yearMonth
                #formatted[yearMonth]["interviewed"]=1
            
            else:
               # formatted[yearMonth]["interviewed"]+=1
                formatted[yearMonth]["weighted"]+=weight
            
    
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
     
 
 
 
 
 