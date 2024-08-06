import pygame 
import basico.tools as tools
from typing import Union,List,Tuple


class Button:
    def __init__(self,
                 window,
                 title:str,
                 size:Union[list[int],Tuple[int,int,int]],
                 color:Union[str,Tuple[int,int,int]],
                 coordinates:List = [0,0],
                 command:callable = None,
                 background:str = None,
                 tags:str = "elipse",
                 color_title:str="white",
                 size_title:int = None,
                 color2_title:str = None):
        self.window = window
        self.title = title
        self.size = size
        self.color = tools.get_color(color)
        self.coordinates = coordinates
        self.command = command
        self.background = background
        self.tags = tags
        self.color2 = color2_title
        self.COLOR_TITLE:str = color_title
        self.backup_window = window.copy()
        self.draw = False
        self.fora = False
        if size_title is not None:
            self.SIZE_TITLE = size_title
        else:
            self.SIZE_TITLE = int(20/100*self.size[0])
        self.title_surface = tools.insert_text(text=title.upper(),
                                       color=self.COLOR_TITLE,
                                       size=self.SIZE_TITLE,
                                       color2=self.color2)
        self.GRID_TITLE = self.title_surface.get_size()
        self.COORDINATE_TITLE_X = int(self.coordinates[0] + self.size[0]/2 - self.GRID_TITLE[0]/2)
        self.COORDINATE_TITLE_Y = int(self.coordinates[1] + self.size[1]/2 - self.GRID_TITLE[1]/2)
        self.COORDINATE_TITLE = (self.COORDINATE_TITLE_X,self.COORDINATE_TITLE_Y)
        
        
    def pack(self):
        self.COORDINATE_TITLE_X = int(self.coordinates[0] + self.size[0]/2 - self.GRID_TITLE[0]/2)
        self.COORDINATE_TITLE_Y = int(self.coordinates[1] + self.size[1]/2 - self.GRID_TITLE[1]/2)
        self.COORDINATE_TITLE = (self.COORDINATE_TITLE_X,self.COORDINATE_TITLE_Y)
        self.rect = tools.draw_rect(window=self.window,
                                    size=self.size,
                                    color=self.color,
                                    coordinates=self.coordinates,
                                    background=self.background,
                                    tags=self.tags)
        self.window.blit(self.title_surface,(self.COORDINATE_TITLE))
        self.backup_window = self.window.copy()
        return(self)
    def run(self,pos:pygame.mouse):
        self.pos = pos
        self.press = tools.verify_click(self.rect, pos)
        if self.press == True:
            if self.command is not None:
                self.command()
            else:
                pass
    def tags_run(self,pos):
        self.pos_tg = pos
        #self.backup_window = window.copy()
        #self.backup_window_ori = self.window.copy()
    
        if self.tags == "elipse":
            if self.draw == False and self.fora == False:
                self.backup_window = self.window.copy()
            if self.pos_tg[0] >= self.coordinates[0] and self.pos_tg[0] <= self.coordinates[0]+self.size[0] and self.pos_tg[1] >= self.coordinates[1] and self.pos_tg[1] <= self.coordinates[1]+self.size[1]:
                tools.draw_rect(window=self.window,
                                size=[10,10],
                                color="green",
                                coordinates=self.coordinates,
                                background=None,
                                tags=None)
                self.draw = True
            else:
                self.fora = True
            if self.draw == True and self.fora == True:
                self.draw = False
                self.fora = False
                self.window.blit(self.backup_window,(0,0))

'''
    def motion(self,tags:str = "x"):
        if tags == "x":
            self.motion_coordinates = int(self.coordinates[0]-self.size[0])
'''
def alight_buttons(start_coordinates:list,
                   orientation:str,
                   space:int,
                   buttons:List[Button]):
    start_coordinate = [start_coordinates[0],start_coordinates[1]]
    if orientation == "x":
        for new_but in buttons:
            new_but.coordinates[0] = start_coordinate[0]
            start_coordinate[0] = start_coordinate[0] + space + new_but.size[0]
            new_but.coordinates[1] = start_coordinate[1]
    if orientation == "y":
        for new_but in buttons:
            new_but.coordinates[1] = start_coordinate[1]
            start_coordinate[1] = start_coordinate[1] + space + new_but.size[1]
            new_but.coordinates[0] = start_coordinate[0]

def get_center_button(size_window:Union[List[int],Tuple[int,int]],
                      button:Button,
                      tags:str = "j"):
    if tags == "x":
        center = (int(size_window[0]/2 - button.size[0]/2), button.coordinates[1])
        return center
    if tags == "y":
        center = (button.coordinates[0],int(size_window[1]/2 - button.size[1]/2))
        return center
    if tags == "j":
        center = (int(size_window[0]/2 - button.size[0]/2),int(size_window[1]/2 - button.size[1]/2))
        return center
    
