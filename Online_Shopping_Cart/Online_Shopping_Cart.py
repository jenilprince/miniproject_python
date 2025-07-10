class Item:
    def __init__(self, name, price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ₹{self.price} x {self.quantity}"
class Cart:
    def __init__(self):
        self.cart=[]
    def add_items(self,item):
        self.item=item
        self.cart.append(item)

    def show_items(self):
        for item in self.cart:
            print(item)
    def total_price(self):
        total=0
        for item in self.cart:
            total += item.price*item.quantity
        print("Total price is ",total)
    def remove_items(self,name):
        found=False
        for item in self.cart:
            if item.name == name:
                self.cart.remove(item)
                print("Item removed from cart")
                found=True
                break

item1=Item("Snacks",150,2)
item2=Item("puffs",10,2)
cart=Cart()
cart.add_items(item2)
cart.add_items(item1)

cart.remove_items("Snacks")
cart.show_items()
cart.add_items(item1)
