from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QDateEdit
from PyQt6.QtGui import QIntValidator
from PyQt6.QtCore import QDate
from database.models.marca import Marca  # Importamos la clase Marca

class BrandForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Registrar Marca")
        self.setGeometry(150, 150, 350, 250)

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

        # Fecha de inicio del contrato
        self.start_date_input = QDateEdit(self)
        self.start_date_input.setCalendarPopup(True)
        self.start_date_input.setDate(QDate.currentDate())

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
        layout.addWidget(QLabel("Fecha de Inicio del Contrato:"))
        layout.addWidget(self.start_date_input)
        layout.addWidget(self.btn_save)

        self.setLayout(layout)

    def save_brand(self):
        name = self.name_input.text().strip()
        phone = self.phone_input.text().strip()
        contract_duration = self.contract_input.text().strip()
        start_date = self.start_date_input.date().toString("yyyy-MM-dd")

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
        marca = Marca(nombre=name, telefono=phone, duracion_contrato=int(contract_duration), fecha_inicio_contrato=start_date)
        marca.save()

        QMessageBox.information(self, "Éxito", "Marca registrada correctamente.")
        self.close()
