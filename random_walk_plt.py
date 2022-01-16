import plotly.express as px
from plotly.graph_objs import Scatter,Layout
from plotly import offline
from random_walk import RandomWalk
from matplotlib import pyplot as plt
import pandas as pd

example = RandomWalk()
example.fill_walk()
point_numbers = range(example.num_points)
# print(type(point_numbers))
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(10, 6), dpi=128) #A larger dpi will therefore act like a magnifying glass. All elements are scaled by the magnifying power of the lens.
ax.set_title('Random Walk', fontsize=24)
ax.set_xlabel('Step', fontsize = 10)
ax.set_ylabel('Position Reached', fontsize =10)
ax.tick_params(axis='both', labelsize= 14)
# use cmap to track the path along each step generated
plt.plot(example.x_values, example.y_values,linewidth=1)
# color start and end point seperately
ax.scatter(0,0, c='red', edgecolor=None, s=100)
ax.scatter(example.x_values[-1],example.y_values[-1], c='green', edgecolor=None, s=100)
ax.axis([-200,200,-200,200])
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
# plt.savefig('random_walk_noEdge_plt.png', bbox_inches='tight')
# plt.show()

# plotly
x = example.x_values
y = example.y_values
px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16]).show()
px.scatter(x, y).show()

