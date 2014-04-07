import pygame
from pygame import *
from collections import namedtuple

# Assign a Parent Image 
parent_image = pygame.image.load('asset/tiles.png')

# A container class which stores information about a tile.
Tile = namedtuple('Tile', ['area',
                           'passable'])
                           
# Dictionary of tile types and associated information.
TILES = {
    'cs':  Tile(pygame.Rect(256,   0, 32, 32), 'TRUE'),  # CobbleStone
    'wl':  Tile(pygame.Rect(320,   0, 32, 32), 'FALSE'), # Wall
    'gs':  Tile(pygame.Rect(384,   0, 32, 32), 'TRUE'),  # Grass
    'ib':  Tile(pygame.Rect(448,   0, 32, 32), 'TRUE'),  # Ice Brick
    'pf':  Tile(pygame.Rect( 32, 160, 32, 32), 'TRUE'),  # Planked Floor
    'gb':  Tile(pygame.Rect(320,  96, 32, 32), 'TRUE'),  # Grey Brick
    'hf':  Tile(pygame.Rect(128, 160, 32, 32), 'TRUE'),  # Hardwood Floor
    'dt':  Tile(pygame.Rect(256, 160, 32, 32), 'TRUE'),  # Dirt
    'sf':  Tile(pygame.Rect(448, 160, 32, 32), 'TRUE'),  # Steel Floor
    'wf':  Tile(pygame.Rect( 32, 320, 32, 32), 'TRUE'),  # Wheat Field
    'sp':  Tile(pygame.Rect( 96, 320, 32, 32), 'TRUE'),  # Steel Planking
    'f1':  Tile(pygame.Rect(160, 320, 32, 32), 'FALSE'), # Fire1
    'wr':  Tile(pygame.Rect(192, 320, 32, 32), 'FALSE'), # Water
    'ws':  Tile(pygame.Rect(256, 320, 32, 32), 'TRUE'),  # Weeds
    'bc':  Tile(pygame.Rect(352, 320, 32, 32), 'FALSE'), # Blue Crystal 
    'f2':  Tile(pygame.Rect(384, 320, 32, 32), 'FALSE'), # Fire2
    'pc':  Tile(pygame.Rect(448, 320, 32, 32), 'FALSE')  # Purple Crystal
}

# Matrix mapping tiles to background.
MAP_node1 = [['wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','gs','gs','gs','gs','gs','wl'],\
             ['wl','ws','gb','gb','dt','dt','dt','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gs','gs','gs','gs','gs','wl'],\
             ['wl','ws','gb','gb','dt','dt','dt','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gb','gs','gs','gs','gs','gs','wl'],\
             ['wl','ws','gb','gb','dt','dt','dt','gb','gb','ws','ws','ws','ws','ws','ws','ws','ws','ws','ws','ws','ws','ws','gb','gb','gs','gs','gs','gs','gs','wl'],\
             ['wl','ws','gb','gb','dt','dt','dt','gb','gb','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','gb','gb','gs','gs','gs','gs','gs','wl'],\
             ['wl','ws','gb','gb','dt','dt','dt','gb','gb','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','gb','gb','gs','gs','gs','gs','gs','wl'],\
             ['wl','ws','gb','gb','dt','dt','dt','gb','gb','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','gb','gb','gs','gs','gs','gs','gs','wl'],\
             ['wl','ws','gb','gb','dt','dt','dt','gb','gb','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','wr','gb','gb','gs','gs','gs','gs','gs','wl'],\
             ['wl','ws','gb','gb','dt','dt','dt','gb','gb','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','gb','gb','gs','gs','gs','gs','gs','wl'],\
             ['wl','ws','gb','gb','dt','dt','dt','gb','gb','wl','pc','pc','pc','pc','pc','pc','pc','pc','pc','pc','pc','wl','gb','gb','gs','gs','gs','gs','gs','wl'],\
             ['wl','ws','gb','gb','dt','dt','dt','gb','gb','wl','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','wl','gb','gb','gs','gs','gs','gs','gs','wl'],\
             ['wl','ws','gb','gb','dt','dt','dt','gb','gb','wl','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','wl','gb','gb','gs','gs','gs','gs','gs','wl'],\
             ['wl','ws','gb','gb','dt','dt','dt','gb','gb','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','wl','gb','gb','gs','gs','gs','gs','gs','wl'],\
             ['wl','ws','gb','gb','dt','dt','dt','gb','gb','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','wl','gb','gb','gs','gs','gs','gs','gs','wl'],\
             ['wl','ws','gb','gb','dt','dt','dt','gb','gb','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','wl','gb','gb','gs','gs','gs','gs','gs','wl'],\
             ['wl','ws','gb','gb','dt','dt','dt','gb','gb','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','wl','gb','gb','gs','gs','gs','gs','gs','wl'],\
             ['wl','ws','gb','gb','dt','dt','dt','gb','gb','wl','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','wl','gb','gb','gs','gs','gs','gs','gs','wl'],\
             ['wl','ws','gb','gb','gb','gb','gb','gb','gb','wl','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','pf','wl','gb','gb','gs','gs','gs','gs','gs','wl'],\
             ['wl','ws','gb','gb','gb','gb','gb','gb','gb','wl','pc','pc','pc','pc','pc','pc','pc','pc','pc','pc','pc','wl','gb','gb','gs','gs','gs','gs','gs','wl'],\
             ['wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','wl','gb','gb','gs','gs','gs','gs','gs','wl']] 
             

