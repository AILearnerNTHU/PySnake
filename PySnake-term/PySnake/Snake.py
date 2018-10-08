# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 18:39:20 2018

@author: Computer-User
"""


import queue

class Snake(object):
    
    def __init__(self,Tail,Direction):
        self.q_snake = queue.deque(maxsuze = 0)
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
        
    def HeadMove(self):
        head = [self.Head()[0],self.Head()[1]]
        self.q_snake.append(head)
        
        
    def TailMove(self):
        self.q_snake.popleft()
        
        
        
        
        
        
    
    