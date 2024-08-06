import basico.button as button
from basico.button import Button
from basico.input import Input
import basico.window as window
from basico.window import Window
import basico.tools as tools
import pygame
import sys
import atendimento
import armario
import nada_consta
import usuario
pygame.init()

class MainMenu:
    def __init__(self):
        self.__title = tools.insert_text(text="menu",
                                       color = "white",
                                       size= 75,
                                       color2=None,
                                       background="images/placa.webp",
                                       percent_background=20)
        
        self.__menu = Window(size=[1000, 600], color="black", background="images/pantano.jpg").pack()
        self.__center_title = tools.get_obj_center([1000,600],self.__title[0].get_size())
        self.__center_background = tools.get_obj_center([1000,600],self.__title[1].get_size())
        self.__menu.blit(self.__title[1],[self.__center_background[0],0])
        self.__menu.blit(self.__title[0],[self.__center_title[0],0])
        self.__backups_origin = self.__menu.copy()
        self.__botoes = self.__tela_botoes()
        
    def __atendimento(self):
        run = atendimento.AtendimentoTela()
        run.run()
    def __armario(self):
        run = armario.ArmarioTela()
        run.run()
    def __nadaConsta(self):
        run = nada_consta.NadaConstaTela()
        run.run()
    def __usuario(self):
        run = usuario.UsuarioTela()
        run.run()
        
    def __tela_botoes(self):
        but_atendimento = Button(window=self.__menu,
                             title="atendimento",
                             size=[400, 50],
                             color=None,
                             coordinates=[0, 0],
                             command=self.__atendimento,
                             color_title="black",
                             background="images/placa.webp",
                             size_title=50)
        but_armario = Button(window=self.__menu,
                             title="armario",
                             size=[400, 50],
                             color= None,
                             coordinates=[0, 0],
                             command=self.__armario,
                             color_title="black",
                             background="images/placa.webp",
                             size_title=50)
        but_nadaconsta = Button(window=self.__menu,
                             title="n/d consta",
                             size=[400, 50],
                             color = None,
                             coordinates=[0, 0],
                             command=self.__nadaConsta,
                             color_title="black",
                             background="images/placa.webp",
                             size_title=50)
        but_usuario = Button(window=self.__menu,
                                           title="usuario",
                                           size=[400, 50],
                                           color = None,
                                           coordinates=[0, 0],
                                           command=self.__usuario,
                                           color_title="black",
                                           background="images/placa.webp",
                                           size_title=50)

        botoes = [but_atendimento, but_armario, but_nadaconsta, but_usuario]
        centro_x = button.get_center_button([1000, 600], but_atendimento, "j")
        button.alight_buttons([centro_x[0],150], "y", 10, botoes)
        for botao in botoes:
            botao.pack()
        return botoes
    
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
                for tg in self.__botoes:
                    pos_tg = pygame.mouse.get_pos()
                    tg.tags_run(pos=pos_tg)
            pygame.display.flip()

if __name__ == "__main__":
    app = MainMenu()
    app.run()