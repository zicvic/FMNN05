# -*- coding: utf-8 -*-
from  __future__  import division
from  scipy       import *
from  matplotlib.pyplot import *
import numpy as np

from assimulo.problem import Implicit_Problem
from assimulo.solvers import IDA
import squeezer

y0,yp0=squeezer.init_squeezer() # Initial values
t0 = 0 # Initial time

squeezemodel = Implicit_Problem(squeezer.squeezer, y0, yp0, t0)

algvar = 7*[1.]+13*[0.]
sim = IDA(squeezemodel) # Create solver instance
sim.algvar = algvar
sim.suppress_alg=True
sim.atol = 1e-7
tf = .03 # End time for simulation

t, y, yd = sim.simulate(tf)

sim.plot(mask=7*[1]+13*[0])
grid(1)
axis([0, .03, -1.5, 1.5])
xlabel('Time, t [s]')
ylabel('Angle, [rad]')