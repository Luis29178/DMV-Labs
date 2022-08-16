import copy
import decimal
import numpy
import pandas as pd

counterint= 0
def isAnogram(wordA, wordB):
    if(sorted(wordA) == sorted(wordB)):
        return True
    else: 
        return False




def isAnogramlist(one,m2,size):
    count = 0
    tempCount = 0
    anlist = []
    word = ""

                             
    
    if len(m2) > 0:
        Bone  = m2[0]
        if Bone in m2:
            m2.remove(Bone)

        tempCount , word , anlist,  = isAnogramlist(one,m2,len(m2))
                
    if(isAnogram(one,Bone)):
        if Bone in m2:
            count += 1     
         
        
        
    if count > 0:    
        anlist.append(word)
    
    
    count += tempCount
    return count , Bone , anlist 
    
                
            
        
        



filesize = 0
progress = 0    

tempfile = open("C:\\Users\\Luis\\Desktop\\DVM\\data\\dict.txt") 
masterfile = []
masterfile2 = []
for word in tempfile:
    masterfile.append(word)
    masterfile2.append(word)
    filesize += 1
tempfile.close()

one= ""
two = ""
nullish = ""


tempWinner = []
winnerlist = []

count = 0    
tempCount = 0

x = 0
file = copy.deepcopy(masterfile)
for line in file:
    one = line
    tempWinner.append(one)
    progressprint = decimal.Decimal(progress) / decimal.Decimal(filesize)
    spliterint = filesize/750
    spliterint = round(spliterint)
    # masterfilerecursive = numpy.array_split(masterfile2,spliterint)
    
    
    print(progressprint*100,"%    ",progress,"/",filesize)
    progress += 1
    if one in masterfile2:
        masterfile2.remove(one)
    arrlen = len(masterfile)
    tempCount , nullish, tempWinner = isAnogramlist(one,masterfile2,arrlen)
            
    if tempCount > count:
        count = tempCount
        winnerlist = copy.deepcopy(tempWinner)
        
    tempWinner = []
    tempCount = 0
    
    
print(count,winnerlist)        


            
            

        
                
                
                