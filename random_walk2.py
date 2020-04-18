#import matplotlib.pyplot as plt

#from random import choice

from get_step import Get_step

class RandomWalk():

    """初始化属性"""

    def __init__(self,num_point = 5000):

        self.num_point = num_point

        """随机漫步始于(0，0)"""

        self.x_values = [0]
        self.y_values = [0]

    # def get_step(self):
    #     #direction = choice([1,-1])
    #     #destance = choice([0, 1, 2, 3, 4])
    #     #step = destance * direction
    #     self.direction = choice([1,-1])
    #     self.destance = choice([0, 1, 2, 3, 4])
    #     self.step = self.direction * self.destance
    #     return self.step


    def fill_walk(self):
        while len(self.x_values) < self.num_point:

            """定义横坐标移动的方向与横坐标每一次移动的跨度"""
            # x_direction = choice([1, -1])
            # x_destance = choice([0, 1, 2, 3, 4])

            """定义横坐标下一步的位移"""
            # x_step = x_destance * x_direction

            step = Get_step()

            x_step = step.result()
            y_step = step.result()

            """定义纵坐标移动的方向与横坐标每一次移动的跨度"""
            # y_direction = choice([1, -1])
            # y_destance = choice([0, 1, 2, 3, 4])

            """定义纵坐标下一步的位移"""
            # y_step = y_destance * y_direction

            """当横坐标和纵坐标移动距离同时为零时，停止本次循环不执行本循环后面的语句，进入下一循环"""
            if x_step == 0 and y_step == 0:
                continue

            """记录下一次的位置，位置列表中最后一个与位移之和"""
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            """将下一次出现的位置添加至位置列表中"""
            self.x_values.append(next_x)
            self.y_values.append(next_y)
