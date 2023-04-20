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
emptyParticle = {
    'Position': None,
    'Velocity': None,
    'Cost': None,
    'Best': {
        'Position': None,
        'Cost': np.inf
    }
}

nPop = 50  # number of particles

# Create Population Array
particle = np.array([emptyParticle.copy() for _ in range(nPop)])

# Initialize Global Best
globalBest = {
    'Position': None,
    'Cost': np.inf
} 

# Initialize Population Members
for i in range(nPop):

    # Generate Random Solution
    particle[i]["Position"] = np.random.uniform(varMin, varMax, varSize)

    # Initialize Velocity
    particle[i]["Velocity"] = np.zeros(varSize)

    # Evaluation 
    particle[i]["Cost"] = costFunction(particle[i]["Position"])
    
    # Update the Personal Best
    particle[i]["Best"]["Position"] = particle[i]["Position"]
    particle[i]["Best"]["Cost"] = particle[i]["Cost"]

    # Update the Global Best
    if particle[i]["Best"]["Cost"] < globalBest["Cost"]:
        globalBest["Cost"] = particle[i]["Best"]["Cost"]

# Array to Hold Best Cost Value on Each Iteration
bestCosts = np.zeros(maxIt, 1)

#%% Main Loop of PSO

#%% Results

