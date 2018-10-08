# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 17:39:38 2018

@author: Computer-User
"""


from pynput import keyboard

from PySnakeGame import Map  , Snake , SnakeDirection ,GamePad
#import GameMode 
import GameScreen as gs

class PySnakeGUI:
    
    
    #Select mode of game
#    mode = input("Which mode would you prefer?\n\ta)Classic\n\tb)Customize\nInput a or b:\t")
#    if str(mode) == "a" : 
#        GameMode.Classic_Mode()
#    else :
#        GameMode.Customize_Mode()
          
    h = input("Height:\t")
    w = input("Width:\t")
    h = int(h)
    w = int(w)
    m = Map.Map(h,w)
    for i in range(0,int(h)):
        for j in range(0,int(w)):
            if i == 0 or j == 0 or i ==h-1 or j ==w-1:
                m.World[i][j].FileType = Map.MapEnum.Wall
    gp = GamePad(m,h,w,[int(h/2),int((w*2)/3)],3,SnakeDirection.Direction.Left)
    global gamescreen
    gamescreen = gs.GameScreen(gp)
    
    
    #Keyboard Controller
    global Gameloop
    Gameloop = True
    
    
    def on_press(key):
        if key == keyboard.Key.esc :
            global Gameloop
            Gameloop = False
        elif key == keyboard.Key.up:
            pass
        elif key == keyboard.Key.down:
            pass
        elif key == keyboard.Key.right:
            pass
        elif key == keyboard.Key.left:
            pass
        else :
            pass
            """
            TODO:
                1.Keyboard Up,Down .... function
                2.when people press no defined key
                
            """
                
            
                
            
    def on_release(key):
        if key == keyboard.Key.esc:
            return False
    
    

    while Gameloop:
        with keyboard.Listener(
            on_press = on_press,
            on_release = on_release) as listener:
            listener.join()
   
    
    
    
    