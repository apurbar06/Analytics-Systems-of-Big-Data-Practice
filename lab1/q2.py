import numpy as np

marks = {}
roll="CSE20D0"
num=1
for i in range(19):
    if num%2==0:
        marks[roll+str(num)] = 25+((num+8)%10)
    else:
        marks[roll+str(num)] = 25+((num+7)%10)
    print(roll+str(num), marks[roll+str(num)])
    num+=1

mark=list((marks.values()))
print("Mean:", np.mean(mark), "Median:",np.median(mark))