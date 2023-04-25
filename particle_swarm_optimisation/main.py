#%%
from tools.plots import makePlot
from PSO import PSO

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
#%% Run PSO
pso = PSO()
pso.runPSO()


#%% Results

logging.info("Global Best Cost = {0}".format(pso.globalBest)) 
makePlot(pso.bestCosts, runName, figDir)


