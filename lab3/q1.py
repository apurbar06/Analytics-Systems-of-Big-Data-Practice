import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


age = [7, 9, 27, 28, 55, 45, 34, 65, 54, 67, 34, 23, 24, 66, 53, 45, 44, 88, 22, 33, 55, 35, 33, 37, 47, 41,31, 30, 29, 12]

mean = np.mean(age)
median = np.median(age)
stddev = np.std(age)
skew = (3*(mean-median)/stddev)


data = np.array(age)
data = pd.DataFrame(data = data)
sns.displot(data,kde = True, bins = 4, rug = True)            # Kernel Density Estimation (KDE) -> to estimate the probability density function of a continuous random variable.     
sns.displot(data,kde = True, bins = 8, rug = True)
sns.displot(data,kde = True, bins = 15, rug = True)
sns.displot(data,kde = True, bins = 20, rug = True)
plt.xlabel('Age of customers', fontsize= 13 );
plt.ylabel('Count', fontsize= 13);
plt.title('Distribution of age of Customers', fontsize=15);
plt.show()

print("\nMean:",mean,"Median:", median,"Std Dev:",stddev,"Skew:",skew)
print("Type of histogram is Unimodal.\n")