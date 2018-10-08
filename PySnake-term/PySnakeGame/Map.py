

from enum import Enum
class MapEnum(Enum):
    Wall = 'w'
    Ground = 'g'
    Fruit = 'f'
    Snake = 's'
    

class MapObject(object):
    def __init__(self):
        self._filetype = MapEnum.Ground
    @property
    def FileType(self):
        return self._filetype
    
    @FileType.setter
    def FileType(self, value):
        self._filetype = value

class Map():
    def __init__(self,Height,Width):
        global World 
        World = [[MapObject()]* int(Width) for i in range(int(Height))]
        
    @property
    def World(self):
        global World
        return World
        
    
    
    