class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                "product_id": product.id,
                "name": product.name,
                "price": float(product.price),  # Convertir Decimal a float
                "quantity": 1,
                "image": product.image.url if product.image else ''
            }
        else:
            self.cart[product_id]["quantity"] += 1
        self.save()

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def decrement(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]["quantity"] -= 1
            if self.cart[product_id]["quantity"] < 1:
                self.remove(product)
            else:
                self.save()

    def clear(self):
        self.session['cart'] = {}
        self.session.modified = True

    def get_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.cart.values())

