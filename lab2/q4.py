import matplotlib.pyplot as plt
import squarify    
import pandas as pd

# Create a data frame with fake data
df = pd.DataFrame({'value':[24.3, 8.13, 390.8, 213.7], 'name':["S&P 500", "Technology", "Communication Equipment", "Cisco System"] })

# plot it
squarify.plot(sizes=df['value'], label=df['name'], color=["red","green","blue", "grey"], alpha=.8 )
plt.axis('off')
plt.show()