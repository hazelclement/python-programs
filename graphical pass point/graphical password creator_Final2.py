import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math as m
import mysql.connector as sql

con = sql.connect(host='localhost',user='root',password='cnd131')
cur = con.cursor()
cur.execute('create database if not exists password_generator')
cur.execute('use password_generator')
run=True

images={1:"Burj khalifa.jpg",2:"Chocolate lava cake.jpg",3:"Eiffel tower.jpg",4:"Hogwarts.jpg",5:"Lemonade.jpg",6:"Lighthouse.jpg",
        7:"mt fuji.jpg",8:"Pizza.jpg",9:"Taj mahal.jpg",10:"Elephants.jpg"}
while run:
 image = int(input("image::"))
 if image > 10 or image <1:
    print("Error-Invalid number")
 else:
     run=False
choice = int(input("do you want to generate or login a password(1/2)"))

if choice == 1:
  print("generate")
  img = Image.open(image)
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

  cur.execute('''create table if not exists password
               (username char(20) primary key,
                x1 decimal(28,20),
                y1 decimal(28,20),
                x2 decimal(28,20), 
                y2 decimal(28,20),
                x3 decimal(28,20),
                y3 decimal(28,20))''')
  username=input('please input your username')

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
    except sql.IntegrityError as err:
        print("Error- dulplicate value for username")


  else:
    print('Error - Number of characters is less than 4')


elif choice == 2:
 t = input('please enter your username')
 print("login")
 data = '''select x1,y1,x2,y2,x3,y3 from password where username='%s' ''' % (t,)
 cur.execute(data)
 data = cur.fetchall()

 '''for i in d:
 print(i[0],i[1],i[2],i[3],i[4],i[5],sep=" / ")'''

 img = Image.open(image)
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
 for i in data:
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
    print("password successful!!!")


  else:
    print("Error - Password incorrect, please try again ")
