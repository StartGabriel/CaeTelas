import basico.button as button
from basico.button import Button
from basico.input import Input
import basico.window as window
from basico.window import Window
import basico.tools as tools
import pygame
import sys
import funcionais.consultarAtendimento
import main_menu

class NadaConstaTela:
    def __init__(self):
        self.__title = tools.insert_text(text="N/D CONSTA",
                                       color="white",
                                       size= 75,
                                       color2="black")
        self.__menu = Window(size=[1000, 600], color="black", background="images/pantano.jpg").pack()
        self.__center_title = tools.get_obj_center([1000,600],self.__title.get_size())
        self.__menu.blit(self.__title,[self.__center_title[0],0])
        self.__backups_origin = self.__menu.copy()
        self.__botoes = self.__tela_botoes()
    def __consultar(self):
        self.consultar = funcionais.consultarAtendimento.ConsultarAtendimento(menu=self.__menu,
                                                                              size_button=[400,50],
                                                                              coordinates_button=[300, 450],
                                                                              title_button="MATRICULA",
                                                                              color_button="black",
                                                                              color_title="white")
        self.consultar.pack()
    def __voltar(self):
        run = main_menu.MainMenu()
        run.run()
    def __tela_botoes(self):
        but_consultar = Button(window=self.__menu,
                             title="consultar",
                             size=[400, 50],
                             color=None,
                             coordinates=[300, 275],
                             command=self.__consultar,
                             color_title="black",
                             background="images/placa.webp",
                                            size_title=50)
        but_voltar = Button(window=self.__menu,
                                     title="voltar",
                                     size=[400, 50],
                                     color=None,
                                     coordinates=[300, 335],
                                     command=self.__voltar,
                                     color_title="black",
                                     background="images/placa.webp",
                                            size_title=50)
        but_voltar.pack()
        but_consultar.pack()
        self.botoes = [but_consultar,but_voltar]
        
        return self.botoes
    def run(self):
        loop = True
        while loop:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for run in self.__botoes:
                        run.run(pos)
            pygame.display.flip()
if __name__ == "__main__":
    app = NadaConstaTela()
    app.run()