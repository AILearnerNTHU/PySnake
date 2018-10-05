import wpf

from System.Windows import Application, Window , MessageBox
from GameSetting import *

class MyWindow(Window):
    global IsStartGame
    def __init__(self):
        wpf.LoadComponent(self, 'PySnake.xaml')
        
    def MenuItem_Click(self, sender, e):
        gs =  GameSetting()  
        gs.ShowDialog()
        if gs.DialogResult == True :
            MessageBox.Show("Game Start")
        else:
            MessageBox.Show("Cancel")


if __name__ == '__main__':
    Application().Run(MyWindow())
