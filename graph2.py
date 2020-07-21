import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
img = Image.open("/flappy bird.jpg")
plt.imshow(img)
fig,ax = plt.subplots()
ax.imshow(img)


x = np.arange(-10, 10)
y = x ** 2
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
coords = []


def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    print(ix, iy)
    global coords
    coords.append(ix, iy)
    if len(coords) == 2:
        fig.canvas.mpl_disconnect(cid)
    return coords


'''cid = fig.canvas.mpl_connect('button_press_event', onclick)

fig, ax = plt.subplots()
ax.plot(np.random.rand(10))


def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))


cid = fig.canvas.mpl_connect('button_press_event', onclick)'''

