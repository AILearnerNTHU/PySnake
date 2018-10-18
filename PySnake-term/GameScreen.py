# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 10:14:43 2018

@author: Computer-User
"""
from PySnakeGame import Map , GamePad , Snake , SnakeDirection
import sys

class GameScreen:
    
    global color
    color = {Map.MapEnum.Wall : "\u001b[44;1m",Map.MapEnum.Ground : "\u001b[47m" , Map.MapEnum.Snake : "\u001b[40m", Map.MapEnum.Fruit :"\u001b[41;1m"}
    """
                                    blue                                white                               black                           Red
    """
    global symbol
    symbol = {Map.MapEnum.Wall : "+",Map.MapEnum.Ground : " " , Map.MapEnum.Snake : "#", Map.MapEnum.Fruit :"*"}
    def DrawPixel(self,x,y,Type):
        #curse move
        if x >= self.last_x :
            sys.stdout.write("\u001b[" + str(x) + "B" + "\u001b[" + str(y) + "C")
        #print
        sys.stdout.write("\u001b[" + str(x) + "B" + "\u001b[" + str(y) + "C" + color[Type] + symbol[Type].ljust(1))
    """
    TODO:move curse
    """
        
    
    def __init__(self,Gamepad):
        sys.stdout.flush()
        global gamepad
      #  gamepad = GamePad
        gamepad = Gamepad
        for i in range(gamepad.Height):
            for j in range(gamepad.Width):
                w = gamepad.Map.World[i][j].FileType
                self.DrawPixel(i,j,w)
        global LastTail
#        global gamepad
        LastTail = gamepad.Tail()
        
        self.last_x = 0
        self.last_y = 0
        
    def NextScreen(self):
        global gamepad
        gamepad.Next()
        if gamepad.Life :
            global LastTail
            self.DrawPixel(LastTail[0],LastTail[1],Map.MapEnum.Ground)
            presentTail = gamepad.Tail()
            self.DrawPixel(presentTail[0],presentTail[1],Map.MapEnum.Snake)
            LastTail = presentTail
        else :
            sys.stdout.flush()
            print("GameOver")
        """
        TODO: GameOver Screen        
        """
        
    def DrawScore(self,score):  
        #curse move back to origin
        sys.stdout.write("\u001b[1000A\u001b[1000C")
        print("Score:" + str(score))
    #Snake Direction
    def GoUp(self):
        global gamepad
        gamepad.GoUp()
        self.NextScreen()
    def GoDown(self):
        global gamepad
        gamepad.GoDown()
        self.NextScreen()
    def GoRight(self):
        global gamepad
        gamepad.GoRight()
        self.NextScreen()
    def GoLeft(self):
        global gamepad
        gamepad.GoLeft()
        self.NextScreen()