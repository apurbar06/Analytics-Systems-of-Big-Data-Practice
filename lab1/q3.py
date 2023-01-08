import random
import statistics

x = []
y = []
for i in range(20):
	x.append(random.randint(6,100))
	y.append((2*x[i])+3) 

stddev = statistics.stdev(y)
print(x)
print(y)
print("Standard Deviation",stddev)