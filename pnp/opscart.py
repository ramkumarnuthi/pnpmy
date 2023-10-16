class ShoppingCart:
    def __init__(self) :
        self.cart = []
        self.total_amount = 0

    def add_item(self, item_name, item_price, quantity):
        item = {"name": item_name, "price": item_price, "quantity": quantity}
        self.cart.append(item)
        self.total_amount += item_price * quantity

    def remove_item(self, item_name):
        for item in self.cart:
            if item['name'] == item_name:
                self.total_amount -= item['price'] * item['quantity']
                self.cart.remove(item)
                break
        else:
            print(f"{item_name} is not in the cart.")

    def display_cart(self):
        for item in self.cart:
            print(f"{item['name']} - Price: {item['price']} - Quantity: {item['quantity']}")
        print(f"Total amount: {self.total_amount}")
        print(f"Total number of items in the cart: {len(self.cart)}")

cart = ShoppingCart()
cart.add_item("Laptop", 800, 2)
cart.add_item("Phone", 300, 3)
cart.display_cart()

cart.remove_item("Laptop")  
cart.display_cart()
