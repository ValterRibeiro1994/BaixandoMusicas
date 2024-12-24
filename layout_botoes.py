"""corrigindo importação """

import sys 
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

"""Iniciando codigo"""

from ferramentas.variaveis import COR_BOTOES_FUNDO, COR_BOTOES_TEXTO

from PySide6.QtWidgets import QVBoxLayout, QPushButton
from ferramentas.apenas_executar import apenas_executar

def layout_vertical_botoes():
    # criando botão Gerenciar Lista
    botao_gerenciar_lista = QPushButton("Gerenciar lista de musicas")
    botao_gerenciar_lista.clicked.connect(lambda : print("função qualquer1"))
    botao_gerenciar_lista.setFixedSize(400, 150)
    botao_gerenciar_lista.setStyleSheet(
        f"""

        background-color: {COR_BOTOES_FUNDO};
        color: {COR_BOTOES_TEXTO};
        font-size: 30px;
        font: arial;

        """
    )

    # criando botão executar
    botao_executar = QPushButton("Apenas Executar (sem baixar)")
    botao_executar.clicked.connect(lambda : apenas_executar())
    botao_executar.setFixedSize(400, 150)
    botao_executar.setStyleSheet(
        f"""

        background-color: {COR_BOTOES_FUNDO};
        color: {COR_BOTOES_TEXTO};
        font-size: 30px;
        font: arial;

        """
    )

    # criando botão executar e baixar
    botao_executar_e_baixar = QPushButton("Executar e baixar.")
    botao_executar_e_baixar.clicked.connect(lambda : print("função qualquer3"))
    botao_executar_e_baixar.setFixedSize(400, 150)
    botao_executar_e_baixar.setStyleSheet(
        f"""

        background-color: {COR_BOTOES_FUNDO};
        color: {COR_BOTOES_TEXTO};
        font-size: 30px;
        font: arial;

        """
    )

    # criar o layout dos botoes
    layout_vertical_botoes = QVBoxLayout()

    # adicionando botões no layout
    layout_vertical_botoes.addWidget(botao_gerenciar_lista)
    layout_vertical_botoes.addWidget(botao_executar)
    layout_vertical_botoes.addWidget(botao_executar_e_baixar)
    layout_vertical_botoes.addStretch()

    return layout_vertical_botoes