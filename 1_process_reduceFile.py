import csv
import json
import os

def getValidInterview():
    data = csv.reader(open('/Users/jzhang/Documents/whoWorks/cps_94_11172022/cps_94.csv','r'))

   reducedFile = csv.writer(open("11172022_hrinsta1_allColumns.csv","w"))
    for row in data:
       # print(row)
        print(len(row))
        header = row
       
        reducedFile.writerow(header)
        break
    
    lineNumber = 0
    for row in data:
        # print(row)
 #        print(row[header.index('pwsswgt')])#PWSSWGT
 #        break
        lineNumber+=1
        if lineNumber%100000==0:
            print(lineNumber)             
     
        if row[header.index('hrintsta')]=="1":
            reducedFile.writerow(row)
   
#getValidInterview()     






#takes a keys json and reduces all data to those columns, and filters by valid interviews, valid+age, or valid+not at work+age
# def reduce():
#     keysFile = json.load(open('/Users/jzhang/Documents/whoWorks/reduced_keys_withWeight.json','r'))
#     focusColumns = list(keysFile.keys())
#     print(focusColumns)
#     #return
#     data = csv.reader(open('/Users/jzhang/Documents/whoWorks/cps_94/cps_94.csv','r'))
#     #data = csv.reader(open('/Users/jzhang/Documents/whoWorks/apr22pub.csv','r'))
#   #  excludedColumns = ['hrhhid','hrmonth','hrhhid2','qstnum','hrsample','hrsersuf']
#
#     ##focusColumns =['peabsrsn','pedwlko','pedwavr','pedwavl','pedwlkwk','pedwrsn','pehract1','pehrrsn1','pehrrsn2','pehrrsn3','pejhrsn','pejhwant','pejhwko','pemjnum','penlfact','prabsrea','premphrs','prptrea','pruntype','puhroff1']
#
#     reducedFile = csv.writer(open("hrinsta1.csv","w"))
#     for row in data:
#        # print(row)
#         print(len(row))
#         header = row
#         newHeader = []
#         for h in header:
#             #print(h.upper())
#             if h.upper() in focusColumns:
#                 print(h)
#                 newHeader.append(h)
#         reducedFile.writerow(newHeader)
#         break
#       # print(count)
#     print(len(focusColumns))
#     lineNumber = 0
#     for row in data:
#         lineNumber+=1
#         if lineNumber%100000==0:
#             print(lineNumber)
#         newRow = []
#         if row[header.index('hrintsta')]=="1":
#             for h in newHeader:
#                 #print(h)
#                 value = row[header.index(h)]
#                 if value=="":
#                     value = "NA"
#                 newRow.append(value)
#         #print(newRow)
#             reducedFile.writerow(newRow)
#
#             if len(newRow)!=len(newHeader):
#                 print(newRow)
                #break
#reduce()       # break
#
# def addOctober():
#     data = csv.reader(open('/Users/jzhang/Documents/whoWorks/cps_94_11172022/oct22pub.csv','r'))
#     reducedFile = csv.writer(open("11172022_hrinsta1_allColumns.csv","a"))
#     for row in data:
#           # print(row)
#           print(len(row))
#           header = row
#
#           #reducedFile.writerow(header)
#           break
#          # print(count)
#       # print(len(focusColumns))
#
#     lineNumber = 0
#     for row in data:
#            # print(row)
#     #        print(row[header.index('pwsswgt')])#PWSSWGT
#     #        break
#         lineNumber+=1
#         if lineNumber%100000==0:
#             print(lineNumber)
#
#         if row[header.index('hrintsta')]=="1":
#             reducedFile.writerow(row)
# addOctober()
#

 

