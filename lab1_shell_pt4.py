# PHYS 1312 vpython lab 1 shell
# Fall 2022 PCS
from __future__ import division, print_function
from vpython import *

oofpez=9.0e9
qe=3e-19
sf=3e-16
np=-5e-9
source = sphere(pos = vector(np,0,0), radius = 1.e-9, color = color.red)

q_source = qe
R = 1e-8
g_arrow = 1e-8

arrow(pos=vector(0,0,0), axis=vector(g_arrow,0,0), color=color.green)
arrow(pos=vector(0,0,0), axis=vector(0,g_arrow,0), color=color.green)
arrow(pos=vector(0,0,0), axis=vector(0,0,g_arrow), color=color.green)
arrow(pos=vector(0,0,0), axis=vector(-g_arrow,0,0), color=color.green)
arrow(pos=vector(0,0,0), axis=vector(0,-g_arrow,0), color=color.green)
arrow(pos=vector(0,0,0), axis=vector(0,0,-g_arrow), color=color.green)

theta = 0
while theta < 2*pi:
  x = 1e-8*cos(theta)
  y = 1e-8*sin(theta)
  r_obs = vector(x,y,0)
  r = r_obs - source.pos
  rhat = r/mag(r)
  E = ((oofpez * qe) / mag(r) **2) * rhat
  r_arrow = arrow(pos=r_obs, axis=E*sf, color = color.orange)
  theta += pi/6

while True:
  continue
