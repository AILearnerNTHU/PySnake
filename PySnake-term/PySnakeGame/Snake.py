# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 18:39:20 2018

@author: Computer-User
"""


import queue
#import SnakeDirection
from . import SnakeDirection
class Snake(object):
    
    def __init__(self,Tail,Direction):
        self.q_snake = queue.deque()
        self.q_snake.append([Tail[0],Tail[1]])
        self.direction = Direction
    """
    q_snake:
       [-1] [0] [1] [2]
       Tail         Head
    """
    @property
    def Head(self):
        return self.q_snake[len(self.q_snake)-2]
    
    @property
    def Tail(self):
        return self.q_snake[-1]
    """
        need to be test
    """
    
    @property
    def Direction(self):
        return self.direction
    
    @Direction.setter
    def Direction(self, value):
        self.direction = value
       
    def NextHead(self):
        h = self.Head
        if self.Direction == SnakeDirection.Direction.Up:
            head = [h[0]-1,h[1]]
        elif self.Direction == SnakeDirection.Direction.Down:
            head = [h[0]+1,h[1]]
        elif self.Direction == SnakeDirection.Direction.Right:
            head = [h[0],h[1]+1]
        elif self.Direction == SnakeDirection.Direction.Left:
            head = [h[0],h[1]-1]
        else:
            print("Error!! No such direction")
        return head;
        
    
    def HeadMove(self):
        self.q_snake.append(self.NextHead())
        
    def TailMove(self):
        self.q_snake.popleft()
        
        
        
        
        
        
    
    