import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import plotly.express as px


df = pd.read_csv('Iris.csv')    


# creating the bar plot
plt.bar(df["Id"], df["SepalLengthCm"], color ='maroon',width = 0.4)
plt.xlabel("ID")
plt.ylabel("SepalLengthCm")
plt.title("ID vs SepalLengthCm")
plt.show()




# creating the pareto chart
# Sort values in descending order and reset index
df_sorted = df.sort_values(by='SepalLengthCm', ascending=False).reset_index()
# Add cumulative percentage column
df_sorted["cum_percentage"] = round(df_sorted["SepalLengthCm"].cumsum()/df_sorted["SepalLengthCm"].sum()*100, 2)    # round upto 2 decimal points
# print(df_sorted)
# Set figure and axis
fig, ax = plt.subplots(figsize=(22,10))
# Plot bars (i.e. frequencies)
ax.bar(df_sorted.index, df_sorted["SepalLengthCm"], color ='maroon',width = 0.4)
ax.set_title("Pareto Chart")
ax.set_xlabel("Id")
ax.set_ylabel("SepalLengthCm")
# Second y axis (i.e. cumulative percentage)
ax2 = ax.twinx()
ax2.plot(df_sorted.index, df_sorted["cum_percentage"], color="red", marker="D", ms=7)
ax2.axhline(80, color="orange", linestyle="dashed")
ax2.yaxis.set_major_formatter(PercentFormatter())
ax2.set_ylabel("Cumulative Percentage")
plt.show()








# creating the scatter plot
plt.scatter(df["Id"], df["SepalWidthCm"])
plt.show()


# creating the line plot
plt.plot(df["Id"], df["SepalWidthCm"], linestyle = 'dotted')
plt.xlabel("ID")
plt.ylabel("SepalLengthCm")
plt.title("ID vs SepalWidthCm")
plt.show()



# creating radar chart
fig = px.line_polar(df, r='PetalLengthCm', theta='Id', line_close=True)
fig.show()


# creating Area plot
plt.fill_between(df["Id"], df["PetalLengthCm"])
plt.show()



# creating the histogram
plt.hist(x=df["PetalWidthCm"],bins= 90,color='red')
plt.show()




# creating the pie plot
FreqTable=(pd.DataFrame({'Frequency' : df.groupby(["Species"]).size()}).reset_index())
plt.pie(FreqTable['Frequency'],labels=FreqTable['Species'], autopct='%1.1f%%', startangle=90)
plt.show()


# creating the Doughnut chart
FreqTable=(pd.DataFrame({'Frequency' : df.groupby(["Species"]).size()}).reset_index())
# Create a circle at the center of the plot
my_circle = plt.Circle( (0,0), 0.7, color='white')
# Give color names
plt.pie(FreqTable['Frequency'], labels=FreqTable['Species'], colors=['red','green','blue'])
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.show()






