import math
import random
import sys
import time
from time import sleep

class World(object):
    """docstring forWorld."""

    def __init__(self,index):
        self.nodes = {} #3D map, but the 3rd Dimension acts like the 4th will
        self.worldscale = 5
        self.worldindex = index
        self.energymax = self.worldscale*10
        self.XNRs = 0
        for y in range(self.worldscale):
            placeholder = {}
            for x in range(self.worldscale):
                self.nodes[x,y]=Node(x,y,1+random.randint(0,5),self.worldindex,placeholder)
        for node in self.nodes:
            self.nodes[node].nodes = self.nodes
        #while self.EnergyCheck() > self.energymax:
        #    indexter = self.nodes[random.randint(0,self.worldscale-1),random.randint(0,self.worldscale-1)]
        #    if indexter.energy != 0:
        #        indexter.energy-=1
        print('Equilibrium 100%')
        t = 0
        while t < 5:
            for y in range(self.worldscale):
                line = []
                for x in range(self.worldscale):
                    line.append(self.nodes[x,y].energy)
                print(line)
            for node in self.nodes:
                self.nodes[node].Update()
            for node in self.nodes:
                self.nodes[node].Act()
            print("AFTER ACTION:")
            for y in range(self.worldscale):
                line = []
                for x in range(self.worldscale):
                    line.append(self.nodes[x,y].energy)
                print(line)
            print("DATA|"+str(t))
            print(self.XNRs,self.worldindex,self.EnergyCheck())
            t+=1
            sleep(0.5)

    def EnergyCheck(self):
        energy = 0
        for node in self.nodes:
            if self.nodes[node].energy > 10:
                self.XNRs+=1
                self.nodes[node].Resonance()
            if self.nodes[node].energy < -10:
                self.nodes[node].Dissonance()
            energy+=self.nodes[node].energy
        return(energy)

class Node(object):
    """docstring for Node."""

    def __init__(self,x,y,energy,index,collection):
        self.energy = energy
        self.location = x,y
        self.worldindex = index
        self.nodes = collection
        self.lowest = 0,0
    def Update(self):
        neighbors = []
        for neighbor in self.SenseNeighbors(False):
            neighbors.append(neighbor)
        lowestE = self.energy
        lowestNode = self.nodes[self.location]
        for neighboritem in neighbors: ## BUG: THEY ONLY CHOOSE THEIR WESTERN NEIGHBORS
            for neighborloc in neighbors:
                if self.nodes[neighborloc].energy <= lowestE:
                    if self.nodes[neighborloc].energy <= self.energy:
                        lowestE = self.nodes[neighborloc].energy
                        lowestNode = self.nodes[neighborloc]
        self.lowest = lowestNode.location
    def Act(self):
        self.nodes[self.lowest].energy+=1
        print(self.nodes[self.lowest].location)
        sleep(0.5)
        self.energy-=1
    def Resonance(self):
        for neighbor in self.SenseNeighbors(False):
            self.nodes[neighbor].energy+=1
            self.energy-=1
    def Dissonance(self):
        for neighbor in self.SenseNeighbors(False):
            self.nodes[neighbor].energy-=1
            self.energy+=1
    def SenseNeighbors(self,corners):
        location = self.location
        returners = []

        #NeighborW = location[0]-1, location[1]
        NeighborE = location[0]+1, location[1]
        NeighborS = location[0], location[1]-1
        NeighborN = location[0], location[1]+1
        #if NeighborW in self.nodes:
        #    returners.append(NeighborW)
        if NeighborE in self.nodes:
            returners.append(NeighborE)
        elif NeighborS in self.nodes:
            returners.append(NeighborS)
        elif NeighborN in self.nodes:
            returners.append(NeighborN)
        if corners == True:
            NeighborSW = location[0]-1, location[1]-1
            NeighborNW = location[0]-1, location[1]+1
            NeighborSE = location[0]+1, location[1]-1
            NeighborNE = location[0]+1, location[1]+1
            if NeighborSW in self.nodes:
                returners.append(NeighborSW)
            elif NeighborNW in self.nodes:
                returners.append(NeighborNW)
            elif NeighborSE in self.nodes:
                returners.append(NeighborSE)
            elif NeighborNE in self.nodes:
                returners.append(NeighborNE)

            return returners

        return returners
World(1)
