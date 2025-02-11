from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox
from PyQt6.QtGui import QDoubleValidator, QIntValidator
from database.models.producto import Producto, TipoProducto
from database.models.marca import Marca  # Asegúrate de importar la clase Marca

class ProductForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Registrar Producto")
        self.setGeometry(150, 150, 300, 300)

        layout = QVBoxLayout()

        # Nombre del producto
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Nombre del Producto")

        # Tipo de producto
        self.type_input = QComboBox(self)
        self.load_product_types()  # Cargar los tipos de producto desde el Enum

        # Marca del producto
        self.brand_input = QComboBox(self)  
        self.load_brands()  

        # Precio del producto
        self.price_input = QLineEdit(self)
        self.price_input.setPlaceholderText("Precio del Producto")
        self.price_input.setValidator(QDoubleValidator(0.01, 999999.99, 2))

        # Stock del producto
        self.stock_input = QLineEdit(self)
        self.stock_input.setPlaceholderText("Stock Inicial")
        self.stock_input.setValidator(QIntValidator(0, 999999))

        # Botón de guardar
        self.btn_save = QPushButton("Guardar Producto", self)
        self.btn_save.clicked.connect(self.save_product)

        # Agregar widgets al layout
        layout.addWidget(QLabel("Nombre:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Tipo:"))
        layout.addWidget(self.type_input)
        layout.addWidget(QLabel("Marca:"))
        layout.addWidget(self.brand_input)
        layout.addWidget(QLabel("Precio:"))
        layout.addWidget(self.price_input)
        layout.addWidget(QLabel("Stock:"))
        layout.addWidget(self.stock_input)
        layout.addWidget(self.btn_save)

        self.setLayout(layout)

    def load_product_types(self):
        """Carga los valores del Enum TipoProducto en el QComboBox."""
        self.type_input.clear()
        for tipo in TipoProducto:
            self.type_input.addItem(tipo.value, userData=tipo)  # Agregar el Enum como userData

    def load_brands(self):
        """Carga todas las marcas en el QComboBox."""
        self.brand_input.clear()
        marcas = Marca.get_all()
        for marca in marcas:
            self.brand_input.addItem(marca.nombre, userData=marca.id)  

    def save_product(self):
        name = self.name_input.text().strip()
        brand_id = self.brand_input.currentData()  
        product_type = self.type_input.currentData()  # Obtener el tipo seleccionado
        price = self.price_input.text().strip()
        stock = self.stock_input.text().strip()

        # Validaciones
        if not name or not brand_id or not product_type or not price or not stock:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return
        if not price.replace(".", "", 1).isdigit():
            QMessageBox.warning(self, "Error", "El precio debe ser un número válido.")
            return
        if not stock.isdigit():
            QMessageBox.warning(self, "Error", "El stock debe ser un número entero.")
            return

        # Obtener la marca correspondiente al ID
        marca = Marca(id=brand_id)

        # Crear el producto y guardarlo
        producto = Producto(nombre=name, marca=marca, precio=float(price), stock=int(stock), tipo=product_type)
        producto.save()

        QMessageBox.information(self, "Éxito", "Producto registrado correctamente.")
        self.close()
