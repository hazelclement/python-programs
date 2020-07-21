import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
img = Image.open("flappy bird.jpg")
plt.imshow(img)
fig,ax = plt.subplots()
ax.imshow(img)

xy2imgxy = lambda x,y: (img.size[0] * x / np.max(ticklx),\
                        img.size[1] * (np.max(tickly) - y) / np.max(tickly))

ticklx = np.linspace(0,100,6)
tickly = np.linspace(0,100,6)
tickpx,tickpy = xy2imgxy(ticklx,tickly)

# Rewrite x,y ticks
ax.set_xticks(tickpx)
ax.set_yticks(tickpy)
ax.set_xticklabels(ticklx.astype('int'))
ax.set_yticklabels(tickly.astype('int'))

# Add scatter point on the image.
px,py = 10,70
imgx,imgy = xy2imgxy(px,py)
ax.scatter(imgx,imgy,s=100,lw=5,facecolor="none",edgecolor="yellow")

# Add plot on the image.
'''px = np.linspace(0,100,500)
py = 10*np.abs(np.sin(2*np.pi*0.02*px))
imgx,imgy = xy2imgxy(px,py)
ax.plot(imgx,imgy,color="yellow",lw=3)'''

# Adjust the axis.
ax.set_xlim(0,tickpx.max())
ax.set_ylim(tickpy.max(),0)

# Save figure.
plt.savefig("lena_color_mod.png",bbox_inches="tight",pad_inches=0.02,dpi=250)
plt.show()