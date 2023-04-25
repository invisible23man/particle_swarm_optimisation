
from utils import costFunctions
import numpy as np
import logging

class PSO:
    def __init__(self, problem, params):
        self.problem = problem
        self.params = params
        
        self.defineProblem()
        self.setParameters()
        self.initialize()

    ## Problem Definition
    def defineProblem(self):
        
        self.costFunction = \
            getattr(costFunctions, self.problem.costFunction)   # Cost Function in Use
        self.nVar = self.problem.nVar                           # Decision Variables 
        self.varSize = (1, self.nVar)                           # Matrix Size of Decision Variables
        self.varMin = self.problem.varMin                       # Lower Bound of Decision Variables
        self.varMax = self.problem.varMax                       # Upper Bound of Decision Variables

    ## Parameters of PSO
    def setParameters(self):
        self.maxIt = self.params.maxIt       # Maximum Number of Iterations
        self.nPop = self.params.nPop         # Population Size (Swarm Size)
        self.w = self.params.w               # Inertia Coefficient
        self.wDamp = self.params.wDamp       # Damping Ratio of Inertia Coefficient
        self.c1 = self.params.c1             # Personal Acceleration Coefficient
        self.c2 = self.params.c2             # Social Acceleration Coefficient

    ## Initialisation
    def initialize(self):
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

        # Create Population Array
        self.particle = np.array([emptyParticle.copy() for _ in range(self.nPop)])

        # Initialize Global Best
        self.globalBest = {
            'Position': None,
            'Cost': np.inf
        } 

        # Initialize Population Members
        for i in range(self.nPop):

            # Generate Random Solution
            self.particle[i]["Position"] = np.random.uniform(self.varMin, self.varMax, self.varSize)

            # Initialize Velocity
            self.particle[i]["Velocity"] = np.zeros(self.varSize)

            # Evaluation 
            self.particle[i]["Cost"] = self.costFunction(self.particle[i]["Position"])
            
            # Update the Personal Best
            self.particle[i]["Best"] = {
                "Position": self.particle[i]["Position"].copy(),
                "Cost": self.particle[i]["Cost"].copy()
            }

            # Update the Global Best
            if self.particle[i]["Best"]["Cost"] < self.globalBest["Cost"]:
                self.globalBest = {
                    "Cost" : self.particle[i]["Best"]["Cost"].copy(),
                    "Position" : self.particle[i]["Best"]["Position"].copy()
                }

        # Array to Hold Best Cost Value on Each Iteration
        self.bestCosts = np.zeros((self.maxIt,1))

    ## Main Loop of PSO
    def runPSO(self):

        for it in range(self.maxIt):

            for i in range(self.nPop): 
            
                # Update Velocity
                self.particle[i]["Velocity"] = self.w*self.particle[i]["Velocity"] \
                    + self.c1*(np.random.random(self.varSize)*(self.particle[i]["Best"]["Position"]-self.particle[i]["Position"])) \
                    + self.c2*(np.random.random(self.varSize)*(self.globalBest["Position"]-self.particle[i]["Position"]))

                # Update Position
                self.particle[i]["Position"] = self.particle[i]["Position"] + self.particle[i]["Velocity"]

                # Evaluation
                self.particle[i]["Cost"] = self.costFunction(self.particle[i]["Position"])

                # Update Personal Best
                if self.particle[i]["Cost"] < self.particle[i]["Best"]["Cost"]:
                    self.particle[i]["Best"] = {
                        "Position": self.particle[i]["Position"].copy(),
                        "Cost": self.particle[i]["Cost"].copy()
                    }   

                # Update the Global Best
                if self.particle[i]["Best"]["Cost"] <self.globalBest["Cost"]:
                    self.globalBest = {
                        "Cost" : self.particle[i]["Best"]["Cost"].copy(),
                        "Position" : self.particle[i]["Best"]["Position"].copy()
                    }   

            # Damping Inertia Coefficient
            self.w = self.w * self.wDamp

            # Store the Best Cost Value
            self.bestCosts[it] = self.globalBest["Cost"]
            logging.info("Iteration {0}: Best Cost = {1}".format(it, self.bestCosts[it])) 

        return self.bestCosts
