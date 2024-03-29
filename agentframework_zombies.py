# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:37:12 2019

@author: gynjkm
"""
import random
import math

class Agent():
    
#Creates out sheep and gives them acces to the information they 
#need for their behaiviour        

    def __init__ (self, environment, agents):
         
         self.environment = environment
         self.environment_height = len(environment)
         self.environment_width = len(environment)
         self.x = random.randint(0, self.environment_width-1)
         self.y = random.randint(0, self.environment_height-1)         
         self.store = 0 
         self.agents = agents

#allows our agents to move randomly two steps    
         
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300

        if random.random() < 0.5:
            self.x = (self.x + 1) % 300
        else:
            self.x = (self.x - 1) % 300

#this calculate the (euclidian) distance beween agents
            
    def distance_between(self,a):
                
        return math.sqrt( ((self.x - a.x)**2) + ((self.y-a.y)**2))   

#checks the local evirnoment for availability of "food", if there is some it 
#is removed from the environment and added to the sheeps storage
        
    def eat(self):
          if self.environment[self.y][self.x] > 10:
              self.environment[self.y][self.x] -= 10
              self.store += 10

#checks for sheep in the neighborhood, if there are agents "share" their food
              
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                average_store = (self.store + agent.store)/2
                self.store = average_store
                agent.store = average_store
        #this tests to see if sharing has taken place        
        #print("Shared with agent " + str(distance) + " units away, now they both have" + str(average_store))

#Creates our zombies and gives them acces to the information they need                   
class Zombiesheep():

    def __init__(self, environment, zombsheep, agents, spawn_coordinates = None):
        self.environment = environment
        self.environment_height = len(environment)
        self.environment_width = len(environment)
        self.agents = agents
        
#Sets the spawning location for our zombies, randomly for 'original zombies
#and at the location where they were bittenfor newly converted zombies
        
        if spawn_coordinates is None:
            self.x = random.randint(0, self.environment_width-1)
            self.y = random.randint(0, self.environment_height-1)
        else:
            self.x = spawn_coordinates[1]
            self.y = spawn_coordinates[0]
            
#move and distance between_work the same as for our sheep (agents) 
#but faster (these are fast Zombieland style zombies, not slow Dawn 
# of the dead type zombies)
            
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 5) % 300
        else:
            self.y = (self.y - 5) % 300

        if random.random() < 0.5:
            self.x = (self.x + 5) % 300
        else:
            self.x = (self.x - 5) % 300
    
    def distance_between(self,a):
                
        return math.sqrt( ((self.x - a.x)**2) + ((self.y-a.y)**2)) 

#checks if a sheep is in the zombie's neighborhood, if there is it appends it a list
#and returns that list as its output
        
    def bite(self, neighbourhood, agents, zombsheep):
        list_agent = []
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                list_agent.append(agent)
        return list_agent
    
#Adds anti zombie traps which detonate when zombies approach,showering
# the area with holy water, killing any zombies but leaving sheep unaffected
        
class Holy_landmine_of_Antioch():
    
    def __init__(self, environment, zombsheep):
        self.environment = environment
        self.environment_height = len(environment)
        self.environment_width = len(environment)
        self.x = random.randint(0, self.environment_width-1)
        self.y = random.randint(0, self.environment_height-1)
        self.zombsheep = zombsheep
        
    def distance_between(self,a):
                
        return math.sqrt( ((self.x - a.x)**2) + ((self.y-a.y)**2)) 

#checks for the presence of zombies within the detection radius, if there are
#any it adds them to the dead_zombies list
        
    def detonate(self, detection_radius, zombsheep):
        dead_zombies = []
        for zombiesheep in self.zombsheep:
            distance = self.distance_between(zombiesheep)
            if distance <= detection_radius:
                dead_zombies.append(zombiesheep)
        return dead_zombies
                
        
                
        