import basico.button as button
from basico.button import Button
from basico.input import Input
import basico.tools as tools
import pygame
import sys
pygame.init()
class Login():
    def __init__(self,
                 window,
                 matriculas):
        self.window = window
        self.backups_origin = self.window.copy()
        self.matriculas = matriculas
    def pack(self):
        self.matricula = Input(window=self.window,
                        size=[400,50],
                        coordinates=[300,275],
                        title="LOGIN")
        self.matricula.pack()
        self.loop=True
        while self.loop:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    verify =self.matricula.run(pos=pos)
                    if verify in self.matriculas:
                        print("esta na matricula")
                        self.matricula.clear_window()
                        return True
                    
            pygame.display.flip()