


from decimal import Decimal


CART_SESSION_ID = "cart"

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if cart is None:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                "nombre": getattr(product, "nombre_producto", str(product)),
                "precio": str(product.precio),
                "imagen": product.imagen.url if getattr(product, "imagen", None) else "",
                "quantity": 0,
            }
        if override_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity
        self.save()

    def remove(self, product):
        pid = str(product.id)
        if pid in self.cart:
            del self.cart[pid]
            self.save()

    def clear(self):
        self.session[CART_SESSION_ID] = {}
        self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        for pid, item in self.cart.items():
            item = item.copy()
            item["precio"] = Decimal(item["precio"])
            item["total"] = item["precio"] * item["quantity"]
            item["id"] = pid
            yield item

    def __len__(self):
        return sum(i["quantity"] for i in self.cart.values())

    def total(self):
        return sum(Decimal(i["precio"]) * i["quantity"] for i in self.cart.values())
