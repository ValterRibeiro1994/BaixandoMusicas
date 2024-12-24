"""corrigindo importação """

import sys 
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

"""Iniciando codigo"""
from ferramentas.layout_principal import layout_principal
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

app = QApplication(sys.argv)
janela_superior = QMainWindow()

"""Configurações basicas da janela"""
# Definindo o título da janela
janela_superior.setWindowTitle("Baixador de músicas do tio...")
janela_superior.setStyleSheet("background-color: black;")

# Definindo o tamanho da janela
janela_superior.resize(800, 400)

widget_central = QWidget()
widget_central.setLayout(layout_principal())#type:ignore

janela_superior.setCentralWidget(widget_central)

janela_superior.show()

app.exec()