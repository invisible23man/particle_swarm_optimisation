#%%
from costFunctions.sphere import Sphere
import numpy as np

#%% Problem Definition

costFunction = Sphere           # Cost Function in Use
nVar = 5                        # Decision Variables 
varSize = [1, nVar]             # Matrix Size of Decision Variables
varMin = -10                    # Lower Bound of Decision Variables
varMax = 10                     # Upper Bound of Decision Variables

#%% Parameters of PSO

maxIt = 100                     # Maximum Number of Iterations
nPop = 50                       # Population Size (Swarm Size)
w = 1                           # Inertia Coefficient
c1 = 2                          # Personal Acceleration Coefficient
c2 = 2                          # Social Acceleration Coefficient
#%% Initialisation

# The Particle Template
empty_particle = {
    'Position': None,
    'Velocity': None,
    'Cost': None,
    'Best': {
        'Position': None,
        'Cost': np.inf
    }
}

nPop = 10  # number of particles

# Create Population Array
particle = np.array([empty_particle.copy() for _ in range(nPop)])

# Initialize Population Members
for i in range(nPop):

    # Generate Random Solution
    particle[i]["Position"] = np.random.uniform(varMin, varMax, varSize)

    # Evaluation 
    particle[i]["Cost"] = costFunction(particle[i]["Position"])


#%% Main Loop of PSO

#%% Results

