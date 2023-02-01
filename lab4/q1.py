from scipy.stats import zscore
import pandas as pd


from IPython.display import Javascript
display(Javascript('google.colab.output.setIframeHeight(0, true, {maxHeight: 5000})'))


# Create a sample df
df = pd.DataFrame({'Age': [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]})

# Calculate the min-max and drop min-max into new column
df['min-max'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())    

# Calculate the zscores and drop zscores into new column
df['z_score'] = zscore(df['Age'])

# Calculate the decimal scaling and drop decimal scaling into new column
p = df['Age'].max()
q = len(str(abs(p)))
df['decimal_scaling'] = df['Age']/10**q

display(df)