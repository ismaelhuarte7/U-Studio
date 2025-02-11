from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QIntValidator
from database.models.marca import Marca  # Importamos la clase Marca

class BrandForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Registrar Marca")
        self.setGeometry(150, 150, 300, 200)

        layout = QVBoxLayout()

        # Nombre de la marca
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Nombre de la Marca")

        # Teléfono de la marca
        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Teléfono de la Marca")
        self.phone_input.setValidator(QIntValidator())  # Asegura que solo se ingresen números

        # Duración del contrato (en meses)
        self.contract_input = QLineEdit(self)
        self.contract_input.setPlaceholderText("Duración del Contrato (meses)")
        self.contract_input.setValidator(QIntValidator(1, 120))  # Valores entre 1 y 120 meses

        # Botón de guardar
        self.btn_save = QPushButton("Guardar Marca", self)
        self.btn_save.clicked.connect(self.save_brand)

        # Agregar widgets al layout
        layout.addWidget(QLabel("Nombre:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Teléfono:"))
        layout.addWidget(self.phone_input)
        layout.addWidget(QLabel("Duración del Contrato (meses):"))
        layout.addWidget(self.contract_input)
        layout.addWidget(self.btn_save)

        self.setLayout(layout)

    def save_brand(self):
        name = self.name_input.text().strip()
        phone = self.phone_input.text().strip()
        contract_duration = self.contract_input.text().strip()

        # Validaciones
        if not name or not phone or not contract_duration:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return
        if not phone.isdigit():
            QMessageBox.warning(self, "Error", "El teléfono debe ser un número válido.")
            return
        if not contract_duration.isdigit():
            QMessageBox.warning(self, "Error", "La duración del contrato debe ser un número válido.")
            return

        # Crear la marca y guardarla
        marca = Marca(nombre=name, telefono=phone, duracion_contrato=int(contract_duration))
        marca.save()

        QMessageBox.information(self, "Éxito", "Marca registrada correctamente.")
        self.close()
