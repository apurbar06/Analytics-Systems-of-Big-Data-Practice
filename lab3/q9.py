import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

temp = [98,87,90,85,95,75]
sales = [15,12,10,10,16,7]

sns.scatterplot(x=temp,y=sales)
plt.title('Sales')
plt.xlabel('Temperature')
plt.ylabel('Temperature VS Sels')
plt.show()

print()
corr_coeff = np.corrcoef(x=temp,y=sales)
print(corr_coeff)