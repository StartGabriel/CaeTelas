import sys
import pygame
from typing import List
from basico.input import Input
import bdpython.user
from funcionais import aviso
from usuario import UsuarioTela

pygame.init()

class Excluir:
    def __init__(self,
                 menu,
                 size_button: List[int],
                 coordinates_button: List[int],
                 title_button: str,
                 color_button: str,
                 color_title: str):
        """
        Inicializa a classe Excluir com os parâmetros fornecidos.
        
        :param menu: A janela do menu.
        :param size_button: Tamanho do botão.
        :param coordinates_button: Coordenadas do botão.
        :param title_button: Título do botão.
        :param color_button: Cor do botão.
        :param color_title: Cor do título do botão.
        """
        self.menu = menu
        self.size = size_button
        self.coordinates = coordinates_button
        self.backups = menu.copy()
        self.title = title_button
        self.color = color_button
        self.color_title = color_title

    def pack(self) -> None:
        """
        Configura o botão de entrada e inicia o loop do evento.
        """
        self.consulta = Input(window=self.menu,
                              size=self.size,
                              coordinates=self.coordinates,
                              title="id",
                              color=self.color,
                              color_title=self.color_title)
        self.consulta.pack()

        self.loop = True
        while self.loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_button_down()
            pygame.display.flip()

    def handle_mouse_button_down(self) -> None:
        """
        Manipula eventos de clique do mouse.
        """
        self.pos = pygame.mouse.get_pos()
        self.retorna = self.consulta.run(self.pos)
        self.consulta.clear_window()
        self.loop = False
        self.excluir(self.retorna)

    def excluir(self, user_id: int, db_path: str = "bdpython/user.db") -> None:
        """
        Exclui um usuário do banco de dados.

        :param user_id: O ID do usuário a ser excluído.
        :param db_path: O caminho do banco de dados.
        """
        try:
            conn = bdpython.user.conectar(db_path)
            user_data = bdpython.user.consultar_user(conn, user_id)
            if not user_data:
                self.show_message(f"'{user_id}' User não encontrado")
                return

            user_name = user_data[1]
            confirmacao = aviso.Avisos([300, 50], [275, 0], "AVISO!", "black", "white")
            confirmed = confirmacao.excluir(user_name, "Deseja excluir")

            if confirmed:
                self.deletar_usuario(conn, user_id, user_name)
            else:
                self.show_message("Operação de exclusão cancelada.")
        except Exception as e:
            self.show_message(f"Erro ao excluir o usuário: {e}")
        finally:
            self.voltar_usuario()

    def deletar_usuario(self, conn, user_id: int, user_name: str) -> None:
        """
        Deleta um usuário do banco de dados e exibe uma mensagem de confirmação.

        :param conn: A conexão com o banco de dados.
        :param user_id: O ID do usuário a ser excluído.
        :param user_name: O nome do usuário a ser excluído.
        """
        bdpython.user.deletar_user(conn, user_id)
        self.show_message(f"user '{user_name}' deletado")

    def show_message(self, message: str) -> None:
        """
        Exibe uma mensagem de aviso.

        :param message: A mensagem a ser exibida.
        """
        aviso_mensagem = aviso.Avisos([300, 50], [275, 0], "AVISO!", "black", "white")
        aviso_mensagem.mensagem(message)

    def voltar_usuario(self) -> None:
        """
        Retorna à tela de usuário.
        """
        usuario_tela = UsuarioTela()
        usuario_tela.run()


