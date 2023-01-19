import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

chairs = [35, 54, 60, 65, 66, 67, 69, 70, 72, 73, 75, 76, 54, 25, 15, 60, 65, 66, 67, 69, 70, 72, 130, 73, 75, 76]

plt.figure(1,figsize=(6,6))
sns.boxplot(y=chairs)
plt.title('Box Plot')
plt.xlabel('Chair')
plt.ylabel('Number of chairs')
plt.show()

print()

plt.figure(2,figsize=(6,6))
sns.swarmplot(y=chairs)
plt.title('Swarm Plot')
plt.xlabel('Chair')
plt.ylabel('Number of chairs')
plt.show()

print("\nOutlire numbers are 15, 25, 35, 130")