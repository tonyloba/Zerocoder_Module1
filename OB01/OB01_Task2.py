class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}
    def add_item(self, name, price):
        self.items[name] = price
    def remove_item(self, name):
        if name not in self.items:
            return
        del self.items[name]
    def get_items(self):
        return f'{self.items}'
    def get_item_price(self, name):
        if name not in self.items:
            return None
        return self.items[name]
    def update_item_price(self, name, new_price):
        if name not in self.items:
            return None
        self.items[name] = new_price

if __name__ == "__main__":

    store1 = Store("My Store1", "123 Main St")
    store1.add_item("Shoes", 10)
    store1.add_item("T-Shirt", 20)

    store2 = Store("My Store2", "3 New St")
    store2.add_item("Shoes", 1)
    store2.add_item("T-Shirt", 2)
    store2.add_item("Jeans", 5)

    store3 = Store("My Store3", "45 baker street")
    store3.add_item("Shoes", 1000)
    store3.add_item("T-Shirt", 2000)
    store3.add_item("Jeans", 5000)

    print(f'For store : {store3.name} actual items are {store3.get_items()}')
    print(f'Price of Shoes: {store3.get_item_price("Shoes")}')
    store3.add_item("Jacket", 80)
    store3.update_item_price("Shoes", 12000)
    store3.remove_item("T-Shirt")

    print("After changes:")
    print(f'For store : {store3.name} actual items are {store3.get_items()}')
    print("Another stores:")
    print(f'For store : {store1.name} actual items are {store1.get_items()}')
    print(f'For store : {store2.name} actual items are {store2.get_items()}')
