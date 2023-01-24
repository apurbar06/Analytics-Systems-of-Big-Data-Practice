import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

temp = [98,87,90,85,95,75]
sales = [15,12,10,10,16,7]

sns.scatterplot(x=temp,y=sales)
sns.regplot(x=temp, y=sales)
plt.xlabel('Temperature')
plt.ylabel('Sales')
plt.title('Temperature VS Sales')
plt.show()

print()
corr_coeff = np.corrcoef(x=temp,y=sales)
print(corr_coeff)
print("\nFrom the plot we can say that there is a positive co-relation between temperature and sales. Sales increases with the increament of temperature.")