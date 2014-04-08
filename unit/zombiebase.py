from unit.base_unit import BaseUnit
import maps, helper
import tiles
import pygame

# Layer of the zombie units for rendering
ZOMBIE_LAYER = 3

class ZombieUnit(BaseUnit):
    """
    This is the base zombie unit that all enemies are determined on.
    This class will contain all the necessary functions to run the zombie
    unit 
    """
    def __init__(self, **keywords):
        #load the base class
        super().__init__(**keywords)
        
        #Give zombies a standard shuffle sound. ***
        self.move_sound = None
        self.hit_sound = None

        #Set unit specific things.
        self.type = "zombie"
        
    def valid_move(self, tile, position):
        """
        Returns if whether or not the unit can pass through the tile.
        """
        # Return default
        if not super().valid_move(tile, pos):
            return False
            
        # We can't pass through enemy units of either Zombie or Survivors
        #if ((u and u.team != self.team and isinstance(u, ZombieUnit))
         #   or (u and u.team != self.team and isinstance(u, unit.survivor_base.SurvivorUnit)):
          #  return False
        
        #Unit can't travel through these default tile sets.
        if (tile.type in {'wl', 'f1', 'wr', 'f2', 'bc'}):
            return False

        return True