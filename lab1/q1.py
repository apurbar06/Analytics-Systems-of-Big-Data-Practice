import pandas as pd 



DataCSV=pd.read_csv('colors.csv',na_values=["NA"]) #blank cells read as NAN
FreqTable=(pd.DataFrame({'Frequency' : DataCSV.groupby( [ "Colour"] ).size()}).reset_index())


tallies=[]
for count in FreqTable["Frequency"]:
    tally=""
    for i in range(1,count+1):
        if(i%5==0 ):
            tally=tally+'\ '
        else:
            tally=tally+'|'
    tallies.append((tally))
    

FreqTable["Tallies"]=tallies    
print(FreqTable)