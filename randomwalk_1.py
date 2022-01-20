from random import randint as rn,choice as ch
import matplotlib.pyplot as plt

class Random_Walk:
    '''3 variables are needed: the number of total points, and two [] for storing x and y coordinates of each points'''
    def __init__(self, point_num):
        self.point_num = point_num
        self.x_coordinates, self.y_coordinates = [0],[0]
        self.x,self.y = 0,0

    def fill_walk(self):

        for p in range(1,self.point_num):
            # x_dir = rn(-1,1) # return -1, 1 or 0
            # y_dir = rn(-1,1)
            x_dir = ch([-1,1])
            y_dir = ch([-1,1])
            x_steps = ch([0,1,2,3,4])
            y_steps = ch([0,1,2,3,4])
            self.x += x_dir * x_steps
            self.y += y_dir * y_steps
            self.x_coordinates.append(self.x)
            self.y_coordinates.append(self.y)



rw = Random_Walk(1000)
rw.fill_walk()
print(rw.x_coordinates)
print(rw.y_coordinates)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(rw.x_coordinates, rw.y_coordinates,c=rw.y_coordinates, cmap=plt.cm.YlOrBr, s=10)
ax.scatter(0,0,c='g',s=100)
ax.scatter(rw.x_coordinates[-1], rw.y_coordinates[-1], c='b',s=100)
ax.axis([-200, 200,-400, 400])
ax.get_xaxis().set_visible(False)
plt.show()



