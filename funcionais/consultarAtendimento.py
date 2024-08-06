from basico.input import Input
import pygame
import sys
pygame.init()
class ConsultarAtendimento:
    def __init__(self,
                 menu,
                 size_button:list[int],
                 coordinates_button:list[int],
                 title_button:str,
                 color_button:str,
                 color_title:str):
        self.menu = menu
        self.size = size_button
        self.coordinates = coordinates_button
        self.backups = menu.copy()
        self.title = title_button
        self.color = color_button
        self.color_title = color_title
    def pack(self):
        self.consulta = Input(window=self.menu,
                        size=self.size,
                        coordinates=self.coordinates,
                        title=self.title,
                        color= self.color,
                        color_title=self.color_title)
        self.consulta.pack()

        self.loop = True
        while self.loop:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    self.pos = pygame.mouse.get_pos()
                    self.retorna = self.consulta.run(self.pos)
                    self.consulta.clear_window()
                    print(self.retorna)
                    self.loop = False
                    self.consultar(self.retorna)
            pygame.display.flip()
    def consultar(self,id:int):
        print(f"consultando {id}")