'''import matplotlib.pyplot as plt


def create_circle():
    circle = plt.Circle((0, 0), radius=5)
    return circle


def show_shape(patch):
    ax = plt.gca()
    ax.add_patch(patch)
    plt.axis('scaled')
    plt.show()

if __name__ == '__main__':
    c = create_circle()
    show_shape(c)'''

import matplotlib.pyplot as plt
plt.axes()
rectangle = plt.Rectangle((0,0), 50, 50, fc='transparent',ec="red")
plt.gca().add_patch(rectangle)
plt.axis('scaled')
plt.show()