import wpf

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'PySnake.xaml')
        
    def MenuItem_Click(self, sender, e):
        pass


if __name__ == '__main__':
    Application().Run(MyWindow())
