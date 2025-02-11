from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout
from PyQt6.QtGui import QFont, QEnterEvent, QCursor
from PyQt6.QtCore import Qt

class StyledButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.initStyle()
    
    def initStyle(self):
        # Estilo actualizado del botón - gris sin bordes redondeados
        self.setStyleSheet("""
            QPushButton {
                background-color: #808080;
                color: white;
                border: none;
                border-radius: 0px;
                padding: 15px;
                margin: 10px;
                font-size: 14px;
                min-width: 200px;
            }
            QPushButton:hover {
                background-color: #666666;
            }
            QPushButton:pressed {
                background-color: #404040;
            }
        """)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

class NavigationBar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # Sin márgenes
        layout.setSpacing(0)  # Sin espacio entre elementos
        
        # Actualizar estilo a gris y hacer que ocupe todo el ancho
        self.setStyleSheet("""
            QWidget {
                background-color: #808080;
                min-height: 60px;
                width: 100%;
            }
            QLabel {
                color: white;
                font-size: 24px;
                font-weight: bold;
                padding: 10px 20px;
            }
        """)
        
        # Logo y texto "U-Studio"
        self.logo_label = QLabel("U-Studio")
        layout.addWidget(self.logo_label)
        
        # Rellenar el resto del espacio a la derecha
        layout.addStretch()

        # Asignar el layout
        self.setLayout(layout)
        self.setFixedHeight(60)  # Mantener la altura fija
