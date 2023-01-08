import numpy as np
import os #to change working directory
import pandas as pd #to work with dataframes/

tallies=[]
# masking
tally=""
def TallyMarks(count):
    global tally
    for i in range(1,count+1):
        if(i%5==0 ):
            tally=tally+'/'
        else:
            tally=tally+'l'
    tallies.append((tally))
    tally=""
        
    
#Opening CSv File
DataCSV=pd.read_csv('ColourData.csv',na_values=["NA"]) #blank cells read as NAN
#convert junk values to NAN by passing them as list to paramter na_values
FreqTable=(pd.DataFrame({'Frequency' : DataCSV.groupby( [ "Colour"] ).size()}).reset_index())
#print(FreqTable)
for i in FreqTable["Frequency"]:
    TallyMarks(i)
FreqTable["Tallies"]=tallies    
#print(tallies)
print(FreqTable)