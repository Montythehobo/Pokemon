# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 08:41:43 2021

@author: Andrew
"""

class Trainer:
    def __init__(self, name):
        self.name = name
    
    
    
    
class Monster:
    def __init__(self, species, ivs=[0,0,0,0,0,0], moves, evs=[0,0,0,0,0,0], ability):
        self.species = species
        self.ivs = ivs
        self.moves = moves
        self.evs = evs
        self.ability = ability
        
    def attribs(self):
        
        