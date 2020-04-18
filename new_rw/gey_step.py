from random import choice

# def get_step():
#     # direction = choice([1,-1])
#     # destance = choice([0, 1, 2, 3, 4])
#     # step = destance * direction
#     direction = choice([1, -1])
#     destance = choice([0, 1, 2, 3, 4])
#     step = direction * destance
#     return step


class Get_step():
    #direction = choice([1,-1])
    #destance = choice([0, 1, 2, 3, 4])
    #step = destance * direction


    # def __init__(self):
    #
    #     self.direction = choice([1,-1])
    #     self.destance = choice([0, 1, 2, 3, 4])


    def result(self):
        self.direction = choice([1,-1])
        self.destance = choice([0, 1, 2, 3, 4])
        self.step = self.direction * self.destance
        return self.step

        #"""self表示类的实例，当只在乎返回结果时，上下两种等效"""
        # direction = choice([1,-1])
        # destance = choice([0, 1, 2, 3, 4])
        # step = direction * destance
        # return step
