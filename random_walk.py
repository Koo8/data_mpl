from random import choice

class RandomWalk:
    '''A class to generate random walks'''

    def __init__(self, num_points = 5000):
        self.num_points = num_points
        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''from (0,0) calculate every following step by randomly decided direction and step (between 0 and 4) for both x and y directions'''
        while (len(self.y_values)) < self.num_points:
            # choose x moving steps and direction
            x_step = self.get_step()
            # choose y moving steps and directions
            y_step = self.get_step()
            # do nothing if not moving at all
            if x_step == 0 and y_step == 0:
                continue
            # calculate the new x,y positions and append them to each list
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        direction = choice([-1,1])
        distance = choice([0,1,2,3,4])
        step = distance * direction
        return step

