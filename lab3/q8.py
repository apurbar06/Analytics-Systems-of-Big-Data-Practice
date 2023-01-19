import plotly.express as px

data = dict( number=[50,110,250,180,70], 
             steps=["Requirement Elicitation","Requirement Anlaysis","Software Development","Debugging and Testing","Others" ])

fig = px.funnel(data, x='number', y='steps')
fig.show()