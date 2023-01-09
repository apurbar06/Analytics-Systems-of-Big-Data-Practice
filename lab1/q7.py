import statistics

MidSem = [10,8,5,21,28,11,14,29,27,29,18,25,26,17,19,23,24,23,21,15]
EndSem = [24,44,12,34,39,37,43,20,25,28,48,45,28,30,46,33,31,29,47,49]
Assignment = [5,7,2,18,12,8,19,14,10,10,16,15,13,17,17,19,13,14,13,11]
Total = []

for i in range(20):
	Total.append(MidSem[i]+EndSem[i]+Assignment[i])

avg = statistics.mean(Total)
Grade = []
print("Class average is:", avg, end="\n\n")
print("Student \tTotal Marks \tGrades")

# deciding grade
for i in range(20):
	if Total[i] >= 90:
		Grade.append('S')
	elif Total[i] >= 80:
		Grade.append('A')
	elif Total[i] >= 70:
		Grade.append('B')
	elif Total[i] >= 60:
		Grade.append('C')
	elif Total[i] >= 50:
		Grade.append('D')
	elif Total[i] >= 0.5*avg:
		Grade.append('E')
	else:
		Grade.append('U')
	print(i+1,'\t\t',Total[i],'\t\t',Grade[i])


# counting frequency
freq = {'S':0,'A':0,'B':0,'C':0,'D':0,'E':0,'U':0}
for elem in Grade:
    freq[elem] += 1
print("\nGrade \tFrequency")
for i in freq:
    print(i, "\t", freq[i])
