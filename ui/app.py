from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFrame, QLabel
from PyQt6.QtGui import QFont, QCursor
from PyQt6.QtCore import Qt, QPropertyAnimation, QSize
from ui.product_form import ProductForm
from ui.sales_form import SalesForm
from ui.view_products import ViewProducts
from ui.brand_form import BrandForm
from ui.view_brands import ViewBrands


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gestión de Stock")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # Título
        title = QLabel("Gestión de Stock")
        title.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        # Contenedor de las tarjetas
        cards_layout = QHBoxLayout()

        self.cards = [
            ("Registrar Producto", self.show_product_form),
            ("Ver mis Productos", self.show_view_products),
            ("Registrar Venta", self.show_sales_form),
            ("Registrar Marca", self.show_brand_form),
            ("Ver Marcas", self.show_view_brands),
        ]

        for text, action in self.cards:
            card = self.create_card(text, action)
            cards_layout.addWidget(card)

        layout.addLayout(cards_layout)
        self.setLayout(layout)

    def create_card(self, text, action):
        card = QFrame(self)
        card.setFixedSize(150, 150)
        card.setStyleSheet("""
            QFrame {
                background-color: #F5F5F5;
                border-radius: 10px;
                border: 1px solid #CCCCCC;
            }
            QFrame:hover {
                background-color: #E0E0E0;
            }
        """)

        label = QLabel(text, card)
        label.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setWordWrap(True)
        label.setGeometry(10, 50, 130, 50)

        card.mousePressEvent = lambda event: action()
        card.enterEvent = lambda event: self.animate_card(card, 170, 170)
        card.leaveEvent = lambda event: self.animate_card(card, 150, 150)
        card.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        return card

    def animate_card(self, card, width, height):
        animation = QPropertyAnimation(card, b"size")
        animation.setDuration(200)
        animation.setEndValue(QSize(width, height))
        animation.start()

    def show_product_form(self):
        self.product_form = ProductForm()
        self.product_form.show()

    def show_view_products(self):
        self.view_products = ViewProducts()
        self.view_products.show()

    def show_sales_form(self):
        self.sales_form = SalesForm()
        self.sales_form.show()

    def show_brand_form(self):
        self.brand_form = BrandForm()
        self.brand_form.show()

    def show_view_brands(self):
        self.view_brands = ViewBrands()
        self.view_brands.show()
