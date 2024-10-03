
from gridworld import Grid
import random
import pygame

class Model:
    def __init__(self, grid:Grid,k):
        self.__width = grid.height  # Width and height in number of cells
        self.__height = grid.width
        self.grid = grid
        self.sim_runs=0
        self.upLeftRightDown= [    [0,-1],
                               [-1,0],     [1,0],
                                    [0,1]
                              ]
        self.k=k
        self.T=100
        self.state = [0 for x in range(self.T)]
        self.c=[random.random()*self.T for x in range(self.T)]
        a=1
     
     
    def setup(self):
        for y in range(self.__height):        
            for x in range(self.__width):
                self.grid[x,y]='O'
        self.printStats()

    def printStats(self):    
        xCount=0
        oCount=0
        total=0
        for y in range(self.__height):        
            for x in range(self.__width):
                total+=1
                if self.grid[x,y]=='X':
                    xCount+=1
                if self.grid[x,y]=='O':
                    oCount+=1
        print("total:",total)
        print("X %:",xCount/total*100)

        print("O %:",oCount/total*100)

                    
    
    def isNeighborOn(self,x,y):
        isOn = False
        for x_delta,y_delta in self.upLeftRightDown:
            index = (y+y_delta)*10+(x+x_delta)
            if index>=0 and index <self.T:
                if self.state[index]==1:
                    isOn = True
                    return isOn
        
    def run_sim(self):
        BLACK = (0, 0, 0)

        # if self.sim_runs==self.T:
        #     return
  
        for y in range(self.__height):        
            for x in range(self.__width):
                index = y*10+x
                self.c[index]=self.c[index]+1
                if self.isNeighborOn(x,y):
                    #self.c[index]=self.c[index]+(self.k*self.c[index])
                    self.c[index]=self.c[index]+self.k*self.c[index]
                if self.c[index]>=self.T:
                    self.grid[x,y]="X"
                    self.state[index]=1
                    self.c[index]=0
                else:
                    self.grid[x,y]="O"
                    self.state[index]=0
        

        self.sim_runs+=1

        print("Simulation:",self.sim_runs)

        if self.sim_runs==self.T:
            self.printStats()
    
    
