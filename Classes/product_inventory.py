"""
Product Inventory Project - Create an application which manages
an inventory of products. Create a product class which has a
price, id, and quantity on hand. Then create an inventory class
which keeps track of various products and can sum up the inventory
value.
"""

class Product:
    def __init__(self, pid, price, qty):
        self.pid = pid
        self.price = price
        self.qty = qty

    def print_product(self):
        print "%d  %s  Rs.%.02f each" %(self.pid, self.price, self.qty)

class Inventory:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def print_inventory(self):
        value = 0

        for product in self.products:
            print "%d\t%s\tRs%.02f each" %(product.pid, product.price, product.qty)
            value += (product.price * product.qty)
        print "\nTotal Value : Rs. %.02f" %value

if __name__ == "__main__":
    p1 = Product(1, 100, 5)
    p2 = Product(2, 10, 100)

    i1 = Inventory()
    i1.add(p1)
    i1.add(p2)

    i1.print_inventory()
