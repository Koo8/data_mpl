import random
import numpy as np
import plotly.express as px
from plotly import offline

class Dice:
    def __init__(self,side=6):
        self.side = side

    def roll(self):
        return random.randint(1, self.side)

d6 = Dice()
d10 = Dice(10)
x_values =np.array(range(2,17))
y1_values, y2_values = [],[]
for n in range(10000):
    y1_values.append(d6.roll())
    y2_values.append(d10.roll())
# print(y1_values)
# print(y2_values)
y_values = np.array(y1_values) + np.array(y2_values)
y_list = list(y_values)
frequencies = []
for n in x_values:
    frequencies.append(y_list.count(n))
# print(y_values)
fig = px.bar(x=x_values,y=frequencies)
offline.plot(fig)


