"""corrigindo importação """

import sys 
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

"""Iniciando codigo"""

from ferramentas.variaveis import COR_BOTOES_FUNDO, COR_BOTOES_TEXTO

from PySide6.QtWidgets import QLabel, QHBoxLayout
from PySide6.QtCore import Qt

def layout_cabecalho_inicial():
    titulo_da_janela = QLabel("Reprodutor de musica do Tio ;) ")
    titulo_da_janela.setAlignment(Qt.AlignCenter)
    titulo_da_janela.setFixedSize(800, 100)
    titulo_da_janela.setStyleSheet(
            f"""

            background-color: {COR_BOTOES_FUNDO};
            color: {COR_BOTOES_TEXTO};
            font-size: 50px;
            font-family: Arial;

            """
    )

    layout_cabecalho = QHBoxLayout()
    layout_cabecalho.addWidget(titulo_da_janela)
    layout_cabecalho.addStretch()
    return layout_cabecalho