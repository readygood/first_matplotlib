import matplotlib.pyplot as plt

from new_rw.random_walk import RandomWalk


while True:

    step = input("pls input Num: ")


    if step == "n":
        break

    else:

        try:

            rw = RandomWalk(num_point=int(step))

            rw.fill_walk()

            point_number = list(range(rw.num_point))

            #plt.plot(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Greens, edgecolors='none')

            plt.plot(rw.x_values, rw.y_values,linewidth=0.2)

            plt.scatter(0,0,c='k',s=30)

            plt.scatter(rw.x_values[-1],rw.y_values[-1],c='r',s=30)

            plt.show()


            #print(point_number)

        except ValueError:
            print("Input type error")