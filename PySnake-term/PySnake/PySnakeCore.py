# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 17:40:33 2018

@author: Computer-User
"""

import queue
import numpy as np
import SnakeDirection
import Map


class PySnakeCore:
   
    
        
        
    class GamePad:
         global game_pad
         global h
         global w
         global snake
         global q_snake
         q_snake = queue.Queue(maxsize = 0)
         global snake_direction
         snake_direction = SnakeDirection.Direction.Left
         """
         SnakeTail => [x of tail,y of tail]
         game_pad => Numpy.Array
         
         """
#         """
#         GamePad define:
#             1 : wall
#             2 : Food
#             3 : Snake
#         """
         def __init__(self,Width,Height,GamePad,SnakeTail,SnakeLength,Direction):
             global h
             h = Height
             
             global w
             w = Width
             
             global game_pad
             game_pad = GamePad
             
             
             if Direction == SnakeDirection.Direction.Up:
                 i = 0
                 while (game_pad[SnakeTail[0]][SnakeTail[1]+i] == 3):
                     
             elif Direction == SnakeDirection.Direction.Down:
                 pass
             elif Direction == SnakeDirection.Direction.Right:
                 pass
             elif Direction == SnakeDirection.Direction.Left:
                 pass
             
             
             
             
         #New Body
         def NewTail():
             pass
            
         #Gameloop
         def Next():
            pass
            
            
        #Game Info
         def Head():
            pass
         
         
         
