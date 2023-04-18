import numpy as np 
import copy
import numpy.random as rnd
import time
import matplotlib.pyplot as plt
 
 
def Rosenbrock(X):
    f = sum( 100.0*(X[i+1]-X[i]**2)**2 + (1-X[i])**2 for i in range(0,len(X)-1) )
    return f
 
def StyblinskiTang(X):
    f_sum=sum((X[i]**4)-(16*X[i]**2)+(5*X[i]) for i in range(len(X)))
    return f_sum/2
 
def Ackley(x):
    d=len(x)
    a=20
    b=0.2
    c=np.pi*2
    sum1=sum(x[i]**2 for i in range(d))
    sum1=(-a)*np.exp(((-b)*np.sqrt(sum1/d)))
    sum2=sum(np.cos(c*x[i]) for i in range(d))
    sum2=np.exp((sum2/d))
    return sum1-sum2+a+np.exp(1)
 
 
def local_best_get(particle_pos,particle_pos_val,p):
    local_best=[0]*p #creating empty local best list
    for j in range(p):  #finding the best particle in each neighbourhood 
                        #and storing it in 'local_best'
        local_vals=np.zeros(3)
        local_vals[0]=particle_pos_val[j-2]
        local_vals[1]=particle_pos_val[j-1]
        local_vals[2]=particle_pos_val[j]
        min_index=int(np.argmin(local_vals))
        local_best[j-1]=particle_pos[min_index+j-2][:]
    return np.array(local_best)
 
 
 
 
def initiation(f,bounds,p):
    d=len(bounds) #finding number of dimensions
    particle_pos=np.zeros(p) #creating empty position array
    particle_pos=particle_pos.tolist() #converting array to list
    particle_velocity=particle_pos[:] #empty velocity array
    particle_pos_val=particle_pos[:] #empty value array
    for j in range(p): #iterating ovre the number of particles
        particle_pos[j]=[rnd.uniform(bounds[i][0],bounds[i][1])\
                    for i in range(d)] #random coordinate within bounds
        particle_pos_val[j]=f(particle_pos[j]) #calculating function value
                                            #at each particle
        particle_velocity[j]=[rnd.uniform(-abs(bounds[i][1]-bounds[i][0])\
                    ,abs(bounds[i][1]-bounds[i][0])) for i in range(d)]
                    #creating random velocity values for each dimension
 
    local_best=local_best_get(particle_pos,particle_pos_val,p)
 
    swarm_best=particle_pos[np.argmin(particle_pos_val)]#getting the lowest particle value
    particle_best=copy.deepcopy(particle_pos)#setting all particles current positions to best
    return d,np.array(particle_pos), np.array(particle_best), \
                 np.array(swarm_best), np.array(particle_velocity), np.array(local_best), \
                     np.array(particle_pos_val)
 
def withinbounds(bounds,particle_pos):
    for i in range(len(bounds)):
        if particle_pos[i]<bounds[i][0]: #if particle is less than lower bound
            particle_pos[i]=bounds[i][0]
        elif particle_pos[i]>bounds[i][1]: #if particle is more than higher bound
            particle_pos[i]=bounds[i][1]
    return
 