from plotly.graph_objs import Bar, Layout
from plotly import offline
import numpy as np
import matplotlib.pyplot as plt

from die import Die


#create a D6
die = Die()
die1 = Die()
# roll 100 times and store the result into the array
result = []
for n in range(1000):
    r =die.roll() + die1.roll()
    result.append(r)
print(result)
'''Analyze the results'''
# use numpy.bincount method, remove the first in the array(for 0), if len(arr) < 6, add 0 to the array
# total_count = np.bincount(result)
# real_frequency = total_count[1:]
# new_array = []
# if len(real_frequency)< (die.num_sides*2):
#     for n in range((die.num_sides*2) - len(real_frequency)):
#         copy = np.append(real_frequency, 0)
#         real_frequency = copy
# print(real_frequency)

# use python method array.count and for loop
frequency =[result.count(x) for x in range(2, die.num_sides+die1.num_sides+1)]
# for n in range(2,die.num_sides*2+1 ):
#     occurance = result.count(n)
#     frequency.append(occurance)
print(frequency)

# '''Visualize the results'''
x_values = list(range(2, die.num_sides*2 +1))
# data = [Bar(x=x_values, y=frequency)]
# print(type(data))
# # config x and y axis
# x_axis_config = {'title': 'Rolling Two Dice Result', 'dtick':1}
# y_axis_config = {'title': 'Frequency of Result'}
# my_layout = Layout(title='Results of rolling two D6 1000 times',
#                    xaxis=x_axis_config, yaxis=y_axis_config)
# offline.plot({'data': data, 'layout': my_layout}, filename='D6.html')

#matplotlib
plt.style.use('seaborn')
fig,ax = plt.subplots(figsize=(10,6), dpi=128)
plt.bar(x_values,frequency)
plt.show()
