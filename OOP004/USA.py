class Item():
    def __init__(self,name, price, category):
        self.name=name
        self.price=price
        self.category=category
item = Item(name="Oreo milkshake", price=10, category="Food")

item = Item(name="Oreo", price=3, category="Food")
print(item.__dict__)


