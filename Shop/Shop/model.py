from datetime import datetime

from pony.orm import Database, Required, Optional, Set, PrimaryKey, db_session, sql_debug

db = Database()


class Product(db.Entity):
    """Товар"""
    category = Optional('Category')
    title = Required(str)
    description = Optional(str)
    unit = Required(str)
    price = Required(float)
    # alt_category = Set('Category')
    # amount = int # количество товара в магазине сейчас
    history = Set('ProductHistory')
    cart_item = Optional('CartItem')
    order_item = Optional('OrderItem')


class ProductHistory(db.Entity):
    product = Required('Product')
    created = Optional(datetime, default=datetime.now)
    price = Required(float)


class Category(db.Entity):
    """Категория товара"""
    parent = Optional('Category', reverse='parent')
    title = Required(str)
    products = Set(Product)


class Customer(db.Entity):
    """Покупатель"""
    email = Optional(str)
    phone = Optional(str)
    name = Required(str)
    address = Set('Address')
    cart = Required('Cart')
    order = Required('Order')


class Address(db.Entity):
    """Адресс"""
    customer = Required('Customer')
    country = Required(str)
    city = Required(str)
    street = Required(str)
    zip_code = Required(str)
    house = Required(int)


class Cart(db.Entity):
    """Корзина с товарами"""
    customer = Optional('Customer' or None)
    product = Set('CartItem')


class CartItem(db.Entity):
    """Элемент корзины"""
    cart = Required('Cart')
    product = Required('Product')
    amount = Required(int)    # 1 еденица товара


class Order(db.Entity):
    """Заказ"""
    customer = Optional('Customer')
    created = Required(datetime)
    products = Set('OrderItem')
    status = Required('Status')


class Status(db.Entity):
    """Статус"""
    name = Required(str)
    order = Optional('Order')


class OrderItem(db.Entity):
    """Товар (одна позиция) в заказе"""
    order = Required("Order")
    product = Optional('Product')
    amount = Required(int)    # 1 единица товара


class Menu:
    """Меню"""


db.bind(provider='sqlite', filename='shop.sqlite', create_db=True)
db.generate_mapping(create_tables=True)
sql_debug(True)


@db_session
def add_product():
    product_1 = Product(title='M200 "Intervention"',
                        description='Make your self a long joy',
                        price=11850,
                        unit='1'
                        )
    product_2 = Product(title='Mossberg 500',
                        description='For close relationships',
                        price=370.34,
                        unit='1'
                        )
    product_3 = Product(title='Ammo .408 Cheyenne Tactical',
                        price=10,
                        unit='200'
                        )
    product_4 = Product(title='Ammo 12/70 Shells',
                        price=5,
                        unit='150'
                        )
    category_1 = Category(title='Entertainment', products=(product_1, product_2))
    category_2 = Category(title='Ammo', products=(product_3, product_4))


add_product()
