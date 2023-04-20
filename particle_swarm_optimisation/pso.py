#%%
from costFunctions.sphere import Sphere
from tools.plots import makePlot

import numpy as np
import logging
import datetime
import os

os.chdir('/Users/invisible_man/Documents/DTU/Courses/Drones/ProgrammingResources/particle_swarm_optimisation')
logDir = './logs'
figDir = './figures'
runName = datetime.datetime.now().strftime("pso_%Y-%m-%d_%H-%M-%S")

logging.basicConfig(filename=os.path.join(logDir, ".".join([runName,"log"])), 
                    level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s: %(message)s', 
                    datefmt='%Y-%m-%d %H:%M:%S')
#%% Problem Definition

costFunction = Sphere           # Cost Function in Use
nVar = 5                        # Decision Variables 
varSize = (1, nVar)             # Matrix Size of Decision Variables
varMin = -10                    # Lower Bound of Decision Variables
varMax = 10                     # Upper Bound of Decision Variables

#%% Parameters of PSO

maxIt = 1000                    # Maximum Number of Iterations
nPop = 50                       # Population Size (Swarm Size)
w = 1                           # Inertia Coefficient
wDamp = 0.99                    # Damping Ratio of Inertia Coefficient
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
    particle[i]["Best"] = {
        "Position": particle[i]["Position"].copy(),
        "Cost": particle[i]["Cost"].copy()
    }

    # Update the Global Best
    if particle[i]["Best"]["Cost"] < globalBest["Cost"]:
        globalBest = {
            "Cost" : particle[i]["Best"]["Cost"].copy(),
            "Position" : particle[i]["Best"]["Position"].copy()
        }

# Array to Hold Best Cost Value on Each Iteration
bestCosts = np.zeros((maxIt,1))

#%% Main Loop of PSO

for it in range(maxIt):

    for i in range(nPop): 
    
        # Update Velocity
        particle[i]["Velocity"] = w*particle[i]["Velocity"] \
            + c1*(np.random.random(varSize)*(particle[i]["Best"]["Position"]-particle[i]["Position"])) \
            + c2*(np.random.random(varSize)*(globalBest["Position"]-particle[i]["Position"]))

        # Update Position
        particle[i]["Position"] = particle[i]["Position"] + particle[i]["Velocity"]

        # Evaluation
        particle[i]["Cost"] = costFunction(particle[i]["Position"])

        # Update Personal Best
        if particle[i]["Cost"] < particle[i]["Best"]["Cost"]:
            particle[i]["Best"] = {
                "Position": particle[i]["Position"].copy(),
                "Cost": particle[i]["Cost"].copy()
            }   

        # Update the Global Best
        if particle[i]["Best"]["Cost"] < globalBest["Cost"]:
            globalBest = {
                "Cost" : particle[i]["Best"]["Cost"].copy(),
                "Position" : particle[i]["Best"]["Position"].copy()
            }   

    # Damping Inertia Coefficient
    w = w* wDamp

    # Store the Best Cost Value
    bestCosts[it] = globalBest["Cost"]
    logging.info("Iteration {0}: Best Cost = {1}".format(it, bestCosts[it])) 

logging.info("Global Best Cost = {0}".format(globalBest)) 

#%% Results

makePlot(bestCosts, runName, figDir)


