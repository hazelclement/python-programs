import matplotlib.pyplot as plt
import numpy as np

image = np.random.rand(5,5)

#1 pixel = 100 meters
r = 1./100.

fig, ax = plt.subplots()
ax.imshow(image, extent=(0,image.shape[1]/r,0,image.shape[0]/r) )
ax.set_xlabel("distance [m]")
ax.set_ylabel("distance [m]")

plt.show()