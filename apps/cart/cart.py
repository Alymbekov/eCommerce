from decimal import Decimal
from django.conf import settings
from apps.ecommerce.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
            self.cart = cart

    def __len__(self):
        """
        Подсчет товаров в корзине
        """
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        """
        Обход товаров в корзине и получение их из базы
        """

        product_ids = self.cart.keys()
        # получение объектов товара и добавление их в корзину
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
        item['total_price'] = item['price'] * item['quantity']
        yield item

    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавление товара в корзину
            """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        """
        Удаление товара из корзины
        """

        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def save(self):

        # обновление корзины
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def clear(self):

        # очистка корзины
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
