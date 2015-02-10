# -*- coding: utf-8 -*-
"""
Created on Mon Feb 09 23:11:37 2015

@author: Glaucia
"""

import random

mat = [[0.1,0.9],[0.1,0.9]]

import scipy       
def discSamp(events,probs):
    ranNum = scipy.random.random()
    cumulProbs = []
    cumulProbs.extend([probs[0]])
    for i in range(1,len(probs)):
        cumulProbs.extend([probs[i]+cumulProbs[-1]])
    for i in range(0,len(probs)):
        if ranNum < cumulProbs[i]:
            return events[i]
    return None
##############################################################################
def MarkovChain (x,matrix):
    currState=discSamp(events=[0,1,2,3,4],probs=[0.25,0.25,0.25,0.25])
    list1=[currState]    
    for i in range (x):
        currState=discSamp(events=[currState],probs=[0.5])
        list1.append(currState)
    return list1

MarkovChain (40,matrix=mat)

###############################################################################
# ----> Try to finish the above lines before Tues, Feb. 10th <----
# Now try running 100 simulations of 100 steps each. How often does the chain
# end in each state? How does this change as you change the transition matrix?
mat1 = [[0.1,0.9],[0.1,0.9]] ###### 0 and 1 have similar frequencies

sim=[]
for i in range(100):
    r=MarkovChain (100,matrix=mat1)
    p=r[99]
    sim.append(p)
print sim

sim.count(0)
sim.count(1)

mat2 = [[0.9,0.1],[0.1,0.9]] #### Repetitions of 0 have a large probability here,
sim=[]
for i in range(100):
    r=MarkovChain (100,matrix=mat2)
    p=r[99]
    sim.append(p)
print sim

sim.count(0)
sim.count(1)

mat3 = [[0.1,0.9],[0.9,0.1]] #### Repetitions of 1 have a large probability here,
sim=[]
for i in range(100):
    r=MarkovChain (100,matrix=mat3)
    p=r[99]
    sim.append(p)
print sim

sim.count(0)
sim.count(1)
###############################################################################
# Try defining a state space for nucleotides: A, C, G, and T. Now define a
# transition matrix with equal probabilities of change between states.
tup=("A","C","T","G")
######Matrix with equal probabilities for each transition
matNucl1=[[0.25,0.25,0.25,0.25],[0.25,0.25,0.25,0.25],[0.25,0.25,0.25,0.25],[0.25,0.25,0.25,0.25]]

######Defining a new function to run Markov Chain using state space with length equal to 4
def MarkovChainNucl (x,matrix,Event):
    tup=tuple(Event)
    currState=random.choice(tup)
    list1=[currState]    
    for i in range (x):
        if currState == Event[0]:
                currState=discSamp(events=Event,probs=matrix[0])
        elif currState == Event[1]:
            currState=discSamp(events=Event,probs=matrix[1])
        elif currState == Event[2]:
            currState=discSamp(events=Event,probs=matrix[2])
        else:
            currState=discSamp(events=Event,probs=matrix[3])
        list1.append(currState)
    return list1
#######Testing the function
MarkovChainNucl (10,matrix=matNucl1,Event=["A","C","T","G"])
###############################################################################
# Again, run 100 simulations of 100 steps and look at the ending states. Then
# try changing the transition matrix.
simNucl1=[]
for y in range(100):
    w=MarkovChainNucl (100,matrix=matNucl1,Event=["A","C","T","G"])
    z=w[99]
    simNucl1.append(z)
print simNucl1

simNucl1.count("A")
simNucl1.count("C")
simNucl1.count("T")
simNucl1.count("G")

#######Changing the matrix and getting far more repetitions of C
matNucl2=[[0.25,0.25,0.25,0.25],[0.05,0.85,0.05,0.05],[0.25,0.25,0.25,0.25],[0.25,0.25,0.25,0.25]]

simNucl2=[]
for y in range(100):
    w=MarkovChainNucl (100,matrix=matNucl2,Event=["A","C","T","G"])
    z=w[99]
    simNucl2.append(z)
print simNucl2

#######And also a high frequency of Cs
simNucl2.count("A")
simNucl2.count("C")
simNucl2.count("T")
simNucl2.count("G")