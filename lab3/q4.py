import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

fuel = [3.6, 6.7, 9.8, 11.2, 14.7]
mass = [0.45, 0.91, 1.36, 1.81, 2.27 ]

plt.figure(figsize=(6,6))
plt.axis([0.4,2.5,3,15])
plt.scatter(mass,fuel)
sns.regplot(x=mass, y=fuel)

corr_coeff = np.corrcoef(mass,fuel)
plt.show()

print()
print(corr_coeff)
print("\nFrom the plot we can say that this is positive and linear co-relation.")