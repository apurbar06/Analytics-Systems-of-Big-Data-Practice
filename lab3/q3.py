import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns

water = [3.2, 3.5, 3.6, 2.5, 2.8, 5.9, 2.9, 3.9, 4.9, 6.9, 7.9, 8.0, 3.3, 6.6, 4.4]
beverages = [2.2, 2.5, 2.6, 1.5, 3.8, 1.9, 0.9, 3.9, 4.9, 6.9, 0.1, 8.0, 0.3, 2.6, 1.4]

water_mean = np.mean(water)
water_median = np.median(water)
water_mode = stats.mode(water)
water_stddev = np.std(water)
water_skew = (3*(mean-median)/stddev)

beverages_mean = np.mean(beverages)
beverages_median = np.median(beverages)
beverages_mode = stats.mode(beverages)
beverages_stddev = np.std(beverages)
beverages_skew = (3*(mean-median)/stddev)


sns.distplot(water,hist=False,rug=True,label='Water')
sns.distplot(beverages,hist=False,rug=True,label='Beverages')
plt.show()


print("\nFor water \t Mean:",water_mean,"Median:", water_median,"Mode:", water_mode,"Std Dev:",water_stddev,"Skew:",water_skew)
print("\nFor beverage \t Mean:",beverages_mean,"Median:",beverages_median,"Mode:", beverages_mode,"Std Dev:",beverages_stddev,"Skew:",beverages_skew)
