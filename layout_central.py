"""corrigindo importação """

import sys 
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

"""Iniciando codigo"""

"""unir o layout de botoes com a lista em um layout horizontal"""

from interface.layout_botoes import layout_vertical_botoes
from interface.layout_visualizar_musicas import layout_vertical_lista

from PySide6.QtWidgets import QHBoxLayout

def layout_central():
    botoes = layout_vertical_botoes()
    lista = layout_vertical_lista()

    # criar layout hotizontal
    layout_central = QHBoxLayout()
    layout_central.addLayout(botoes)
    layout_central.addLayout(lista)
    layout_central.addStretch()

    return layout_central