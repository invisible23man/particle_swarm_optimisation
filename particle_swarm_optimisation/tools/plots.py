from matplotlib import pyplot as plt
import os

def makePlot(bestCosts, runName, figDir, showPlot = True):
    # create a new figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Add a grid    
    plt.grid(True)

    # set the labels for line plot
    ax1.plot(bestCosts, linewidth=2)
    ax1.set_xlabel('Iteration')
    ax1.set_ylabel('Best Cost')

    # set the labels for semilog plot
    ax2.semilogy(bestCosts, linewidth=2)
    ax2.set_xlabel('Iteration')
    ax2.set_ylabel('Best Cost (log scale)')

    # Save the plots as separate PNG images
    plt.savefig(os.path.join(figDir,"_".join([runName,'Plot.png'])), dpi=300, bbox_inches='tight')
   
    if showPlot:
        # display the plot
        plt.show()