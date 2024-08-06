import pygame
from typing import Union,List,Tuple
import basico.tools as tools

class Window:
    def __init__(self,
                 size:Union[List[int],Tuple[int,int,int]],
                 color:Union[str,Tuple[int,int,int]],
                 background:str = None):

        self.size = size
        self.color = tools.get_color(color)
        self.background = background
        self.START_COORDINATES = (0,0)
        self.window = pygame.display.set_mode((self.size))
    def pack(self):
        self.window.fill(self.color)
        if self.background is not None:
            self.background = tools.get_image(self.background)
            self.background = pygame.transform.scale(self.background,self.size)
            self.window.blit(self.background,self.START_COORDINATES)
        return self.window
