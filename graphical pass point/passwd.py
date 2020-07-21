import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import mysql.connector as sql
import math as m

con = sql.connect(host='localhost',user='root',password='cnd131')
cur = con.cursor()
cur.execute('create database if not exists password_generator')
cur.execute('use password_generator')

def password_creator():
  image=input("Lemonade.jpg")
  img = Image.open("Lemonade.jpg")

  ticklx = np.linspace(0,100,6)
  tickly = np.linspace(0,100,6)
  fig,ax = plt.subplots()
  ax.imshow(img)

  xy2imgxy = lambda x,y: (img.size[0] * x / np.max(ticklx),\
                        img.size[1] * (np.max(tickly) - y) / np.max(tickly))
  tickpx,tickpy = xy2imgxy(ticklx,tickly)

  # Rewrite x,y ticks
  ax.set_xticks(tickpx)
  ax.set_yticks(tickpy)
  ax.set_xticklabels(ticklx.astype('int'))
  ax.set_yticklabels(tickly.astype('int'))

  # Adjust the axis.
  ax.set_xlim(0,tickpx.max())
  ax.set_ylim(tickpy.max(),0)


  coords = []


  def onclick(event):
    click = event.xdata, event.ydata
    if None not in click:  # clicking outside the plot area produces a coordinate of None, so we filter those out.
        print('x = {}, y = {}'.format(*click))

        coords.append(click)



  plt.gca().figure.canvas.mpl_connect('button_press_event', onclick)
  plt.show()  # stops the CLI until the user closes the graph window

  #print("The clicked coordinates were: {}".format(coords))

  cur.execute('''create table if not exists password
               (username char(20) primary key,
                x1 decimal(28,20),
                y1 decimal(28,20),
                x2 decimal(28,20), 
                y2 decimal(28,20),
                x3 decimal(28,20),
                y3 decimal(28,20))''')

  username=input('input')
  if len(username)>=4:
    try:
       for i in range(3):
         g = [username]
         for t in coords:
             for x in t:
                 g.append(x)
                 t1 = tuple(g)
       cur.execute('''insert into password values
       ('%s',%s,%s,%s,%s,%s,%s)''' % t1 )
       con.commit()
    except ValueError:
        print("error")

  else:
    print('Error - Number of characters is less than 4')


password_creator()


t = input('please enter your username')
data = '''select x1,y1,x2,y2,x3,y3 from password where username='%s' ''' % (t,)
cur.execute(data)
d = cur.fetchall()

'''for i in d:
 print(i[0],i[1],i[2],i[3],i[4],i[5],sep=" / ")'''

img = Image.open("Lemonade.jpg")
'''plt.imshow(img)'''
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

# Adjust the axis.
ax.set_xlim(0,tickpx.max())
ax.set_ylim(tickpy.max(),0)


coords = []


def onclick(event):
    click = event.xdata, event.ydata
    if None not in click:  # clicking outside the plot area produces a coordinate of None, so we filter those out.
        print('x = {}, y = {}'.format(*click))

        coords.append(click)



plt.gca().figure.canvas.mpl_connect('button_press_event', onclick)
plt.show()  # stops the CLI until the user closes the graph window

#print("The clicked coordinates were: {}".format(coords))


def calculateDistance(x1, y1, x2, y2):
    dist = m.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist
for i in d:
 print(i[0],i[1],i[2],i[3],i[4],i[5],sep=" / ")
 a= float(i[0])
 b=float(i[1])
 c=float(i[2])
 d=float(i[3])
 e=float(i[4])
 f=float(i[5])
 dist1=calculateDistance(a, b, coords[0][0], coords[0][1])
 dist2=calculateDistance(c, d, coords[1][0], coords[1][1])
 dist3=calculateDistance(e, f, coords[2][0], coords[2][1])
 print(dist1,dist2,dist3)
if dist1<20 and dist2<20 and dist3<20:
    pass
else:
    print("Error - Password incorrect, please try again ")





