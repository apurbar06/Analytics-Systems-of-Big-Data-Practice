import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

standard_normal_dist = np.random.randn(30)
log_normal_dist = np.random.lognormal(size=30)


sns.violinplot(standard_normal_dist)
plt.title('Violin plot for Standard-Normal distribution')
plt.show()


sns.violinplot(log_normal_dist)
plt.title('Violin plot for Log-Normal distribution')
plt.show()