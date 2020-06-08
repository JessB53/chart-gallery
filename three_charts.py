# # three_charts.py

# #
# # CHART 1 (PIE)
# #

pie_data = [
    {"company": "Company X", "market_share": 0.55},
    {"company": "Company Y", "market_share": 0.30},
    {"company": "Company Z", "market_share": 0.15}
]

print("----------------")
print("GENERATING PIE CHART...")
print(pie_data) # TODO: create a pie chart based on the pie_data


import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:

labels = []
sizes =[]
for x in pie_data:  
    labels.append(x["company"])
    sizes.append(x["market_share"])

print(labels)
print(sizes)


fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show() # need to explicitly "show" the chart window

# #
# # CHART 2 (LINE)
# #

line_data = [
    {"date": "2019-01-01", "stock_price_usd": 100.00},
    {"date": "2019-01-02", "stock_price_usd": 101.01},
    {"date": "2019-01-03", "stock_price_usd": 120.20},
    {"date": "2019-01-04", "stock_price_usd": 107.07},
    {"date": "2019-01-05", "stock_price_usd": 142.42},
    {"date": "2019-01-06", "stock_price_usd": 135.35},
    {"date": "2019-01-07", "stock_price_usd": 160.60},
    {"date": "2019-01-08", "stock_price_usd": 162.62},
]

print("----------------")
print("GENERATING LINE GRAPH...")
print(line_data) # TODO: create a line graph based on the line_data


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = []
y =[]
for i in line_data:  
     x.append(i["date"])
     y.append(i["stock_price_usd"])

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='date', ylabel='stock_price (usd)',
       title='Daily Stock Prices')
ax.grid()

fig.savefig("test.png")
plt.show()

#
# CHART 3 (HORIZONTAL BAR)
#

bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]

print("----------------")
print("GENERATING BAR CHART...")
print(bar_data) # TODO: create a horizontal bar chart based on the bar_data

import plotly.graph_objects as go

x = []
y = []
for i in bar_data:  
     x.append(i["viewers"])
     y.append(i["genre"])
fig = go.Figure(go.Bar(x=x, y=y, orientation='h'))

fig.show()
