"""Main module."""
import numpy as np
import copy
import numpy.random as rnd
import ParticleSwarmUtility as PSU

def particleSwarm(f, bounds, p, c1, c2, vMax, tol):
    print('Placing particles and giving random velocities')
