import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

data = {
    'Activity'   : ['Studying', 'Sleeping', 'Playing', 'Hobbies','Others'],
    'Time Spent' : [33,30,18,5,14]
    }
df = pd.DataFrame(data, columns = ['Activity', 'Time Spent'])
	

plt.pie(df['Time Spent'],labels=df['Activity'], autopct='%1.1f%%', startangle=90)
plt.show()