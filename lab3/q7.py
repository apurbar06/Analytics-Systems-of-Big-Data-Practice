import plotly.graph_objects as go

categories = ['Textile', 'Jewellery','Cleaning Essentials','Cosmetics']

fig = go.Figure()

# creating Multiple Trace Radar Chart
fig.add_trace(go.Scatterpolar(
      r=[10,5,15,14],
      theta=categories,
      name='Quarter 1'
))
fig.add_trace(go.Scatterpolar(
      r=[6,5,20,10],
      theta=categories,
      name='Quarter 2'
))
fig.add_trace(go.Scatterpolar(
      r=[8,2,16,21],
      theta=categories,
      name='Quarter 3 '
))
fig.add_trace(go.Scatterpolar(
      r=[13,4,15,11],
      theta=categories,      
      name='Quarter 4'
))


fig.show()