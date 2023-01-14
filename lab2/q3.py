# library & dataset
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('Iris.csv')  


# A correlogram is a combination of scatter plots and histograms.
# Basic correlogram
sns.pairplot(df)
plt.show()





"""
The seaborn library allows to draw a correlation matrix through the pairplot() function. The parameters to create the example graphs are:

    1. data : dataframe
    2. kind : kind of plot to make (possible kinds are ‘scatter’, ‘kde’, ‘hist’, ‘reg’)
"""
# with regression
sns.pairplot(df, kind="reg")
plt.show()
 
# without regression
sns.pairplot(df, kind="scatter")
plt.show()






"""
In a graph drawn by pairplot() function of seaborn, we can control the marker features, colors and data groups by using additional parameters such as:

    1. hue : variables that define subsets of the data
    2. markers : a list of marker shapes
    3. palette : set of colors for mapping the hue variable
    4. plot_kws : a dictionary of keyword arguments to modificate the plot
"""
sns.pairplot(df, kind="scatter", hue="Species", markers=["o", "s", "D"], palette="Set2")
plt.show()
 
# we can give other arguments with plot_kws.
sns.pairplot(df, kind="scatter", hue="Species", plot_kws=dict(s=80, edgecolor="white", linewidth=2.5))
plt.show()









"""
As we can select the kind of plot to make in pairplot() function, we can also select the kind of plot for the diagonal subplots.

    -> diag_kind : the kind of plot for the diagonal subplots (possible kinds are ‘auto’, ‘hist’, ‘kde’, None)

Note that we can use bw_adjust to increase or decrease the amount of smoothing.
"""
# Density
sns.pairplot(df, diag_kind="kde")
plt.show()
 
# Histogram
sns.pairplot(df, diag_kind="hist")
plt.show()
 
# we can custom it as a density plot or histogram so see the related sections
sns.pairplot(df, diag_kind="kde", diag_kws=dict(fill=True, bw_adjust=.05) )
plt.show()