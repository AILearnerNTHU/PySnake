# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 17:39:38 2018

@author: Computer-User
"""


from pynput import keyboard

import numpy as np
import PySnakeCore 
import GameMode 
import GameScreen as gs

class PySnakeGUI:
    
    
    #Select mode of game
    mode = input("Which mode would you prefer?\n\ta)Classic\n\tb)Customize\nInput a or b:\t")
    if str(mode) == "a" : 
        GameMode.Classic_Mode()
    else :
        GameMode.Customize_Mode()
          
    
    
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
   
    
    
    
    