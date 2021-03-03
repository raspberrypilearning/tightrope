#!/bin/python3

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

y = [255, 255, 0]
x = [0, 0, 0]
b = [0, 0, 255]

persx = 0
persy = 0

pad = [
  y,y,y,x,x,x,x,x,
  x,x,y,x,x,x,x,x,
  x,x,y,x,x,x,x,x,
  x,x,y,y,y,y,y,x,
  x,x,x,x,x,x,y,x,
  x,x,x,x,x,x,y,x,
  x,x,x,x,y,y,y,x,
  x,x,x,x,y,x,x,x
]

while True:
  sense.set_pixels(pad)
  sense.set_pixel(persx, persy, b)

  helling = sense.get_orientation()['pitch']
  kanteling = sense.get_orientation()['roll']

  print('Helling:', helling)
  print('Kanteling:', kanteling)

  if 270 < helling < 315 and persx < 7:
    persx += 1

  if 45 < helling < 90 and persx > 0:
    persx -= 1

  if 45 < kanteling < 90 and persy < 7:
    persy += 1

  if 270 < kanteling < 315 and persy > 0:
    persy -= 1

  huidige = sense.get_pixel(persx, persy)
  if huidige == x:
    persx = 0
    persy = 0

  sleep(0.4)
