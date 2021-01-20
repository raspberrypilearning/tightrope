#!/bin/python3

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

y = [255, 255, 0]
x = [0, 0, 0]
b = [0, 0, 255]

perx = 0
pery = 0

ruta = [
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
  sense.set_pixels(ruta)
  sense.set_pixel(perx, pery, b)

  cabeceo = sense.get_orientation()['pitch']
  alabeo = sense.get_orientation()['roll']

  print('Pitch:', alabeo)
  print('Roll:', cabeceo)

  if 270 < cabeceo < 315 and perx < 7:
    perx += 1

  if 45 < cabeceo < 90 and perx > 0:
    perx -= 1

  if 45 < alabeo < 90 and pery < 7:
    pery += 1

  if 270 < alabeo < 315 and pery > 0:
    pery -= 1

  pixel_actual= sense.get_pixel(perx, pery)
  if pixel_actual == x:
    perx = 0
    pery = 0

  sleep(0.4)
