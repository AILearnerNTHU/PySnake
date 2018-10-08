# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 16:29:30 2018

@author: Computer-User
"""
from . import SnakeDirection , Map , Snake
class GamePad:
       def __init__(self,GameWorld,Height,Width,SnakeTail,SnakeLength,Direction):
           #global h 
           self.h = Height
           #global w
           self.w = Width           
           global snake
           snake = Snake(SnakeTail,Direction)
           global world
           world = GameWorld
           for i in range(SnakeLength):
               world.World[SnakeTail[0]][SnakeTail[1]].FileType = Map.MapEnum.Snake
               snake.HeadMove()           
             
           global IfNewTail
           IfNewTail = False
             
           self.iflife = True
             
       @property
       def Map(self):
           global world
           return world
       @property
       def Life(self):
           return self.iflife               

       @property
       def Height(self):
           return self.h
       @property
       def Width(self):
           return self.w
        #New Body
       def NewTail():
           global IfNewTail
           IfNewTail = True          
       #Gameloop
       def Next(self):
          global snake
          
          hd = self.Snake.NextHead()
          if self.Map()[hd[0]][hd[1]] == Map.MapEnum.Snake or self.Map()[hd[0]][hd[1]] == Map.MapEnum.Wall:
              self.iflife = False
          if self.Map()[hd[0]][hd[1]] == Map.MapEnum.Fruit:
              IfNewTail = True
          snake.HeadMove()
          if IfNewTail :
              pass
          else :
              global snake
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
         