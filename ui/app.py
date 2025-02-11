from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton
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
        self.setGeometry(100, 100, 400, 300)
        
        layout = QVBoxLayout()
        
        self.btn_registrar_producto = QPushButton("Registrar Producto")
        self.btn_ver_productos = QPushButton("Ver mis Productos")
        self.btn_registrar_venta = QPushButton("Registrar Venta")
        self.btn_registrar_marca = QPushButton("Registrar Marca")
        self.btn_ver_marcas = QPushButton("Ver Marcas")
        
        self.btn_registrar_producto.clicked.connect(self.show_product_form)
        self.btn_ver_productos.clicked.connect(self.show_view_products)
        self.btn_registrar_venta.clicked.connect(self.show_sales_form)
        self.btn_registrar_marca.clicked.connect(self.show_brand_form)
        self.btn_ver_marcas.clicked.connect(self.show_view_brands)
        
        layout.addWidget(self.btn_registrar_producto)
        layout.addWidget(self.btn_ver_productos)
        layout.addWidget(self.btn_registrar_venta)
        layout.addWidget(self.btn_registrar_marca)
        layout.addWidget(self.btn_ver_marcas)
        
        self.setLayout(layout)


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
