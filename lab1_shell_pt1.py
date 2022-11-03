# PHYS 1312 vpython lab 1 shell
# Fall 2022 PCS
from __future__ import division, print_function
from vpython import *

oofpez=9.0e9
qe=3e-19
sf=3e-16
np=6e-9
source = sphere(pos = vector(0,0,0), radius = 1.e-9, color = color.red)

q_source = qe
R = 1e-8
g_arrow = 1e-8

r_obs = vector(R,0,0)
r = r_obs - source.pos
rhat = r/mag(r)
E = ((oofpez * qe) / mag(r) **2) * rhat
r_arrow = arrow(pos=r_obs, axis=E*sf, color = color.orange)
arrow(pos=vector(0,0,0), axis=vector(g_arrow,0,0), color=color.green)
arrow(pos=vector(0,0,0), axis=vector(0,g_arrow,0), color=color.green)
arrow(pos=vector(0,0,0), axis=vector(0,0,g_arrow), color=color.green)
arrow(pos=vector(0,0,0), axis=vector(-g_arrow,0,0), color=color.green)
arrow(pos=vector(0,0,0), axis=vector(0,-g_arrow,0), color=color.green)
arrow(pos=vector(0,0,0), axis=vector(0,0,-g_arrow), color=color.green)
r_obs = vector(0,R,0)
r = r_obs - source.pos
rhat = r/mag(r)
E = ((oofpez * qe) / mag(r) **2) * rhat
r_arrow = arrow(pos=r_obs, axis=E*sf, color = color.orange)
print(E*sf)

r_obs = vector(0,0,R)
r = r_obs - source.pos
rhat = r/mag(r)
E = ((oofpez * qe) / mag(r) **2) * rhat
r_arrow = arrow(pos=r_obs, axis=E*sf, color = color.orange)

r_obs = vector(-R,0,0)
r = r_obs - source.pos
rhat = r/mag(r)
E = ((oofpez * qe) / mag(r) **2) * rhat
r_arrow = arrow(pos=r_obs, axis=E*sf, color = color.orange)

r_obs = vector(0,-R,0)
r = r_obs - source.pos
rhat = r/mag(r)
E = ((oofpez * qe) / mag(r) **2) * rhat
r_arrow = arrow(pos=r_obs, axis=E*sf, color = color.orange)

r_obs = vector(0,0,-R)
r = r_obs - source.pos
rhat = r/mag(r)
E = ((oofpez * qe) / mag(r) **2) * rhat
r_arrow = arrow(pos=r_obs, axis=E*sf, color = color.orange)

# How far away is the source charge? What is the magnitude of the the vector r?

# 
#


while True:
  continue
