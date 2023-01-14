import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import seaborn as sns
import pandas as pd




# X-Y Plots With a Regression Line between two arrays
x = np.arange(10, 20)
y = np.array([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])

slope, intercept, r, p, stderr = scipy.stats.linregress(x, y)       # get the slope and the intercept of the regression line
line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'       # get the string with the equation of the regression line and the value of the correlation coefficient
# plot the graph
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=0, marker='s', label='Data points')
ax.plot(x, intercept + slope * x, label=line)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(facecolor='white')
plt.show()






# X-Y Plots With a Regression Line between SepalLengthCm and PetalLengthCm of Iris dataset
df = pd.read_csv('Iris.csv')  

slope, intercept, r, p, stderr = scipy.stats.linregress(df["SepalLengthCm"], df["PetalLengthCm"])       # get the slope and the intercept of the regression line
line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'       # get the string with the equation of the regression line and the value of the correlation coefficient
# plot the graph
fig, ax = plt.subplots()
ax.plot(df["SepalLengthCm"], df["PetalLengthCm"], linewidth=0, marker='s', label='Data points')
ax.plot(df["SepalLengthCm"], intercept + slope * df["SepalLengthCm"], label=line)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(facecolor='white')
plt.show()







# hitmap on random dataset
# Create a dataset
df = pd.DataFrame(np.random.random((10,10)), columns=["a","b","c","d","e","f","g","h","i","j"])
# plot a heatmap with annotation
heatmap = sns.heatmap(df, annot=True, annot_kws={"size": 7})
heatmap.set(title = "Hitmap on random dataset\n")  
plt.show()






# hitmap on iris dataset
dataframe = pd.read_csv('Iris.csv')  
correlation = dataframe.corr()  
heatmap = sns.heatmap(correlation, annot = True)  
heatmap.set(xlabel = 'IRIS values on x axis', ylabel = 'IRIS values on y axis\t', title = "Correlation matrix of IRIS dataset\n")  
plt.show()  