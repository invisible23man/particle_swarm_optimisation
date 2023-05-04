#%%
from tools.plots import makePlot
from PSO import PSO

import numpy as np
import logging
import datetime
import os
import hydra

@hydra.main(config_path = './../conf', config_name = "config.yaml")
def main(cfg):

    os.chdir(cfg.pathParameters.rootDir)
    logDir = cfg.pathParameters.logDir
    figDir = cfg.pathParameters.figDir
    runName = datetime.datetime.now().strftime("pso_%Y-%m-%d_%H-%M-%S")

    logging.basicConfig(filename=os.path.join(logDir, ".".join([runName,"log"])), 
                        level=logging.DEBUG, 
                        format='%(asctime)s %(levelname)s: %(message)s', 
                        datefmt='%Y-%m-%d %H:%M:%S')

    problem = cfg.problemDefinition
    params = cfg.psoParameters

    ## Run PSO
    pso = PSO(problem, params)
    pso.runPSO()

    ## Results
    logging.info("Global Best Cost = {0}".format(pso.globalBest)) 
    makePlot(pso.bestCosts, runName, figDir)

if __name__ == '__main__':
    main()
