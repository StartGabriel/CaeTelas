from basico.input import Input
import pygame
import sys
import bdpython
import bdpython.user
import basico.tools
import basico.window
from basico import button
from basico.button import Button
from usuario import UsuarioTela
pygame.init()
class Avisos:
    def __init__(self,
                 size_button:list[int],
                 coordinates_button:list[int],
                 title_button:str,
                 color_button:str,
                 color_title:str):
        self.menu = basico.window.Window([1000,600],"black","images/pantano.jpg").pack()
        self.size = size_button
        self.coordinates = coordinates_button
        self.backups = self.menu.copy()
        self.title = title_button
        self.color = color_button
        self.color_title = color_title
        self.loops = True
        self.text_title= basico.tools.insert_text(text=self.title,
                                 color=self.color_title,
                                 size=self.size[1],
                                 color2=self.color)
        self.coordinates_title = basico.tools.get_obj_center([1000,600],self.text_title.get_size())
        self.menu.blit(self.text_title,[self.coordinates_title[0],0])
        
    def excluir(self,nome,text):
        self.excluindo = nome
        self.__text_aviso= basico.tools.insert_text(text=f"{text} {nome}?",
                                 color=self.color_title,
                                 size=self.size[1],
                                 color2=self.color)
        
        self.coordinates_text = basico.tools.get_obj_center(coordinate_size=[1000,600],size_objt=self.__text_aviso.get_size())
        self.menu.blit(self.__text_aviso,self.coordinates_text)
        self.buttons()
        return self.verify
    def mensagem(self,text):
        self.__text_aviso = basico.tools.insert_text(text=text,
                                                     color=self.color_title,
                                                     size=self.size[1],
                                                     color2=self.color)
        self.coordinates_text = basico.tools.get_obj_center(coordinate_size=[1000,600],size_objt=self.__text_aviso.get_size())
        self.size_text_aviso = self.__text_aviso.get_size()
        self.menu.blit(self.__text_aviso,self.coordinates_text)
        self.coordinates_return = [self.coordinates_text[0]+self.size_text_aviso[0]/2-150,self.coordinates_text[1]+70]
        self.but_return = Button(window=self.menu,
                                 title="RETORNAR",
                                 size=[300,50],
                                 color="red",
                                 coordinates=self.coordinates_return,
                                 command=self.note)
        self.but_return.pack()
        self.botao =[self.but_return]
        self.loop(self.botao)
        
    def buttons(self):
        self.but_yes = Button(window=self.menu,
                              title="SIM",
                              size=[100,50],
                              color="red",
                              coordinates=[self.coordinates_text[0],self.coordinates_text[1]+70],
                              command=self.yes,
                              size_title=50)
        self.size_text_aviso = self.__text_aviso.get_size()
        self.coordinates_not_but = self.size_text_aviso[0] + self.coordinates_text[0] - 100
        self.but_not = Button(window=self.menu,
                              title="NAO",
                              size=[100,50],
                              color="green",
                              coordinates=[self.coordinates_not_but,self.coordinates_text[1]+70],
                              command=self.note,
                              size_title=50)
        self.botoes = [self.but_yes,self.but_not]
        self.but_yes.pack()
        self.but_not.pack()
        self.loop(self.botoes)
    def loop(self,buts):
        while self.loops:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for run in buts:
                        run.run(pos)
            pygame.display.flip()
    def yes(self):
        print("excluiu")
        self.loops = False
        self.verify = True
    def note(self):
        self.loops = False
        self.verify = False
    
