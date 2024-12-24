"""corrigindo importação """

import sys 
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

"""Iniciando codigo"""

"""unir o layout central com o cabeçalho em um layout vertical"""

from interface.layout_central import layout_central
from interface.layout_cabecalho import layout_cabecalho_inicial
from PySide6.QtWidgets import QVBoxLayout

def layout_principal():
    cabecalho = layout_cabecalho_inicial()
    central = layout_central()#type: ignore

    layout_principal = QVBoxLayout()
    layout_principal.addLayout(cabecalho)
    layout_principal.addLayout(central)
    layout_principal.addStretch()
    return layout_principal