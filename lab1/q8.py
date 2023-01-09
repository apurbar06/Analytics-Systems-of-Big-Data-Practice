import statistics

mid_sem = [10,8,5,21,28,11,14,29,27,29,18,25,26,17,19,23,24,23,21,15]
end_sem = [24,44,12,34,39,37,43,20,25,28,48,45,28,30,46,33,31,29,47,49]
assignment = [5,7,2,18,12,8,19,14,10,10,16,15,13,17,17,19,13,14,13,11]
total = []

for i in range(20):
	total.append(mid_sem[i]+end_sem[i]+assignment[i])

avg = statistics.mean(total)
passing_min = avg*0.5

passing_students_total_marks = 0
passing_student_number = 0
for i in range(20):
	if total[i] >= passing_min:
		passing_students_total_marks += total[i]
		passing_student_number += 1
passing_student_mean = passing_students_total_marks/passing_student_number

X = passing_student_mean - passing_min
max_mark = max(total)
S_cutoff = max_mark -0.1*(max_mark - passing_student_mean)
Y = S_cutoff - passing_student_mean
A_cutoff = passing_student_mean + Y*(5/8)
B_cutoff = passing_student_mean + Y*(2/8)
C_cutoff = passing_student_mean - X*(2/8)
D_cutoff = passing_student_mean - X*(5/8)
E_cutoff = passing_min


Grade = []
print("Class average is:", avg, end="\n\n")
print("Student \tTotal Marks \tGrades")

# deciding grade
for i in range(20):
	if total[i] >= S_cutoff:
		Grade.append('S')
	elif total[i] >= A_cutoff:
		Grade.append('A')
	elif total[i] >= B_cutoff:
		Grade.append('B')
	elif total[i] >= C_cutoff:
		Grade.append('C')
	elif total[i] >= D_cutoff:
		Grade.append('D')
	elif total[i] >= E_cutoff:
		Grade.append('E')
	else:
		Grade.append('U')
	print(i+1,'\t\t',total[i],'\t\t',Grade[i])


# counting frequency
freq = {'S':0,'A':0,'B':0,'C':0,'D':0,'E':0,'U':0}
for elem in Grade:
    freq[elem] += 1
print("\nGrade \tFrequency")
for i in freq:
    print(i, "\t", freq[i])
