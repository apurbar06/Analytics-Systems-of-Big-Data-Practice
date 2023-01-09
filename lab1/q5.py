import numpy as np
import pandas as pd #to work with dataframes
import matplotlib.pyplot as plt

data = {
    'Grades': ['S', 'B', 'C', 'D'], 
    'Count' : [31,29,25,15]
    }
df = pd.DataFrame(data, columns = ['Grades', 'Count'])
	

# Create a pie chart
plt.pie(df['Count'],labels=df['Grades'], autopct='%1.1f%%', startangle=90)    # autopct enables you to display the percent value
plt.show()

# Create a bar graph
x_pos = np.arange(len(df['Grades']))    # arange() function is used to get evenly spaced values within a given interval.
plt.bar(x_pos, df['Count'], align='center')
plt.xticks(x_pos, df['Grades'])
plt.ylabel('Number of Students')
plt.title('Grades')
plt.show()