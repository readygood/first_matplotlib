import matplotlib.pyplot as plt
from random_walk import RandomWalk

while 1:
    rw = RandomWalk(num_point=50)

    rw.fill_walk()

    plt.plot(rw.x_values,rw.y_values)

    plt.show()

    keep_moving = input()

    if keep_moving == "n":
        break

