import wpf

from System.Windows import Window,MessageBox
from System.Windows.Controls import TextBox


class GameSetting(Window):
    #global IsStartGame 
    #IsStartGame = False
    def __init__(self):
        wpf.LoadComponent(self, 'GameSetting.xaml')

    
    def btnOK_Click(self, sender, e):
        tW = False
        tH = False

        if tW and tH :
            MessageBox.Show("Please enter the value")
        else:
            self.DialogResult  = True
            self.Close()
        
    def txtWidth_TextChanged(self, sender, e):
        pass

    
    


