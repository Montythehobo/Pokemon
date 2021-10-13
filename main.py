# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 08:41:43 2021

@author: Andrew
"""

import math

class Trainer: #defines the trainer and their attributes
    def __init__(self, name):
        self.name = name
    
    
    
    
class Monster: #Defines the pokémon class and their attributes
    def __init__(self, species, ivs, evs, level, status):#, moves, #ability,\
                 #stats, #backslash tells program to carry to next line (for readability)\
                 #current_health, level, status, name, accuracy): #Defines important values needed
        
        self.species = species  #Species and related attributes will be given in a separate file
        self.ivs = ivs
#        self.moves = moves  #Moves will be related to species
        self.evs = evs
        #self.ability = ability  #Ability will be related to species
#        self.current_health = 1
        self.level = level
        self.status = status
#        self.name = species
#        self.accuracy = 100
        
        #stat order is Health, Attack, Defence, Special Attack, Special Defence, Speed
        #final ev spot is for max EVs, if total of other EVs = 256, will become 1 and no more EVs will be added
        
    def pk_stats(self): #declares a list which will find base stats
        base_stats = []
        stats = [1,1,1,1,1,1]
        f = open('mon_stats.txt') #opens the file with details about mons' stats
        
        for line in f:  #iterates through lines in the file
            if(line.strip() == self.species):  #until it finds the species it's looking for, strip() takes away new line
                for stat in range (0,6):
                    base_stats.append(int(next(f)))  #inserts the required stats into the list
                break
        #print(base_stats)
        stats[0] = (math.floor(((math.floor(self.evs[0]/4)+self.ivs[0]+(2*base_stats[0]))*self.level)/100) + self.level + 10)
        for i in range (1,6):
            stats[i] = math.floor(math.floor(((math.floor(self.evs[i]/4)+self.ivs[i]+(2*base_stats[i]))*self.level)/100)+5)
        print(stats)
        
    def pk_type(self):
        type = []
        f = open('mon_type.txt') #opens the file with details about mons' types
        
        for line in f:
            if(line.strip() == self.species):
                for ty in range (0,2):
                    temp_type = next(f)
                    if temp_type != '\n':
                        type.append(temp_type.strip())
                    else:
                        break
                break
        print(type)
        
monster1 = Monster(species="Pikachu", ivs = [0,0,0,0,0,0], evs = [0,0,0,0,0,0], level = 100, status = '')        
monster2 = Monster(species="Caterpie", ivs = [0,0,0,0,0,0], evs = [0,0,0,0,0,0], level = 50, status = '')        
monster3 = Monster(species="Garchomp", ivs = [24,12,30,16,23,5], evs = [74,190,91,48,84,23], level = 78, status = '')        
monster4 = Monster(species="Pikachu", ivs = [20,10,7,14,30,1], evs = [10,20,30,40,50,60], level = 83, status = '')
monster1.pk_stats()
monster1.pk_type()
monster2.pk_stats()
monster2.pk_type()
monster3.pk_stats()
monster3.pk_type()
monster4.pk_stats()
monster4.pk_type()


