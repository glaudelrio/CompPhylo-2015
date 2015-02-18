# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 14:39:59 2015

@author: Glaucia
"""

import scipy as sp  
def discSamp(events,probs):
    ranNum = sp.random.random()
    cumulProbs = []
    cumulProbs.extend([probs[0]])
    for i in range(1,len(probs)):
        cumulProbs.extend([probs[i]+cumulProbs[-1]])
    for i in range(0,len(probs)):
        if ranNum < cumulProbs[i]:
            return events[i]
    return None


class MarkovObj(object):
    state=("a","b")
    Probabs=[[0.5,0.5],[0.5,0.5]]
    num=25

    def dmcSim(self):

    # Define list to hold chain's states
        chain = []    

    # Draw a state to initiate the chain
        currState = discSamp(events=self.state,probs=[1.0/len(self.state) for x in self.state])
        chain.extend(currState)

    # Simulate the chain over n-1 steps following the initial state
        for step in range(1,self.num):
            probs1 = self.Probabs[self.state.index(currState)] # Grabbing row associated with currState
            currState = discSamp(self.state,probs1) # Sample new state
            chain.extend(currState)        
        
        return chain
d=MarkovObj()
print d.state
print d.Probabs
print d.dmcSim()