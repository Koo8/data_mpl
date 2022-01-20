import random
import plotly.express as px
from plotly import  offline
import numpy as np


class Dice:
    '''the roll() should generate a randint of (1,sides of the dice)'''
    def __init__(self, side=6, round=1):
        self.side = side
        self.round = round
        self.x_values = list(range(self.round,self.side*self.round+1))
        self.y_values = np.zeros(len(self.x_values))
        # print(self.x_values)
        # print(self.y_values)

    def roll(self):
        value = 0
        for _ in range(self.round):
            value +=random.randint(1, self.side)
        return value

    def fill_y_values(self, num):
        for _ in range(num):
            self.y_values[self.roll()-self.round] +=1
        return self.y_values

dice = Dice(round=3)
y = np.array(dice.fill_y_values(10000))
print(y)
x = dice.x_values
fig = px.bar(x=x, y=y)
offline.plot(fig)




