from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class NavigationBar(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.setStyleSheet("""
            QWidget {
                background-color: #2C3E50;
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

        self.logo_label = QLabel("U-Studio")
        self.logo_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        layout.addWidget(self.logo_label)
        layout.addStretch()

        self.setLayout(layout)
        self.setFixedHeight(60)
