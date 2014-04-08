import pygame, unit, maps, helperfunctions

from unit.base_unit import BaseUnit
from unit.zombiebase import ZombieUnit
from pygame.sprite import Sprite

class BasicZombie(ZombieUnit):
    """
    This is the standard zombie unit. Since the zombie is not significant
    the stats of this unit are pretty low. But with huge groups of them they
    can swarm the player.
    """

    sprite = pygame.image.load("asset/units/zombiefront.png")

    def __init__(self, **keywords):
        #load the image for the base class.
        self._base_image = BasicZombie.sprite

        #load the base class
        super(BasicZombie, self).__init__(**keywords)

        #set unit specific things.
        self.type = "BasicZombie"
        self.speed = 1
        self.damage = 2
        self.defense = 1
        self.health = 3
        self.max_health = 3

    def valid_move(self, tile, position):
        """
        Returns if whether or not the unit can pass through the tile.
        """
        # Return default
        if not super().valid_move(tile, pos):
            return False
            
        # We can't pass through enemy units of either Zombie or Survivors
        #if ((u and u.team != self.team and isinstance(u, ZombieUnit)) or (u and u.team != self.team and isinstance(u, unit.survivor_base.SurvivorUnit)):
         #   return False
        
        #Unit can't travel through these default tile sets.
        if (tile.type in {'wl', 'f1', 'wr', 'f2', 'bc'}):
            return False

        return True
        
unit.unit_types["BasicZombie"] = BasicZombie
