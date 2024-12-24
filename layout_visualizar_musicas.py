"""corrigindo importação """

import sys 
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

"""Iniciando codigo"""

from ferramentas.variaveis import COR_BOTOES_FUNDO, COR_BOTOES_TEXTO
from ferramentas.controle_de_dados import GerenciarDados
from PySide6.QtWidgets import QVBoxLayout, QListWidget
from PySide6.QtCore import Qt

def layout_vertical_lista():
    # Criando representação da lista
    lista_view = QListWidget()
    resgistros_de_musicas = GerenciarDados()
    dados = resgistros_de_musicas.lista_de_musicas
    # passando registro para a representação da lista
    for registro in dados:# type: ignore
        musica_do_dicionario = f'{registro["artista"]} {registro["musica"]}'
        lista_view.addItem(musica_do_dicionario)

    # moldando o tamanho da representaçao da lista
    lista_view.setFixedSize(400, 470)

    # moldando estilo da represenção da lista
    lista_view.setStyleSheet(
            f"""

            background-color: {COR_BOTOES_FUNDO};
            color: {COR_BOTOES_TEXTO};
            font-size: 30px;
            font: arial;

            """
        )

    # criar o layout vertical para receber a representação da lista
    layout_vertical_lista = QVBoxLayout()

    # alinhando ele a direita
    layout_vertical_lista.addWidget(lista_view, alignment=Qt.AlignLeft)

    # adicionando espaço apos a lista para centralizar
    layout_vertical_lista.addStretch()
    return layout_vertical_lista

