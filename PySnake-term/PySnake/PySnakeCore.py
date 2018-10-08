# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 17:40:33 2018

@author: Computer-User
"""

import SnakeDirection
import Map
import Snake


class PySnakeCore:
   
    
        
        
    class GamePad:
         def __init__(self,GamePad,SnakeTail,SnakeLength,Direction):
             global snake
             snake = Snake.Snake(SnakeTail,Direction)
             global world
             world = GamePad
             for i in range(SnakeLength):
                 world.World[SnakeTail[0],SnakeTail[1]].FileType = Map.MapEnum.Snake
                 snake.HeadMove()
             
             
             global IfNewTail
             IfNewTail = False
         #New Body
         def NewTail():
             global IfNewTail
             IfNewTail = True
            
         #Gameloop
         def Next():
            global snake
            snake.HeadMove()
            global IfNewTail
            if IfNewTail :
                pass
            else :
#                global snake
                snake.TailMove()
#                global IfNewTail
                IfNewTail = False
         #Snake Direction
         def GoUp():
             global snake
             snake.Direction = SnakeDirection.Direction.Up
         def GoDown():
             global snake
             snake.Direction = SnakeDirection.Direction.Down
         def GoRight():
             global snake
             snake.Direction = SnakeDirection.Direction.Right
         def GoLeft():
             global snake
             snake.Direction = SnakeDirection.Direction.Left
            
            
        #Game Info
         def HeadInfo():
            pass
         
         """
         HeadInfo:
             TODO:
                 1.Get information for 8 direction about Snake's head
                 2.direction between snake and fruit
         """
         def Head():
             global snake
             return snake.Head()
         def Tail():
             global snake
             return snake.Tail()
         
