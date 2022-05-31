#Start by creating a Store class that has 2 attributes: a name and a list of products. 
# The name must be provided upon creation, but the products list should be empty.
class Store:

    def __init__(self, store_name):
        self.store_name = store_name
        self.products = []

#takes a product and adds it to the store
    def add_product(self, new_product):
        self.products.append(new_product)
        return self

#remove the product from the store's list of products given the id 
# (assume id is the index of the product in the list) and print its info.
    def sell_product(self, id):
        for item in self.products:
            if item.id == id:
                self.products.pop(item.id)
        return self

# increases the price of each product by the percent_increase given
    def inflation(self, percent_increase):
        for price in self.products:
            price.update_price(percent_increase, True)

#updates all the products matching the given category by reducing 
# the price by the percent_discount given
    def set_clearance(self, category, percent_discount):
        for category in self.products:
            category.update_price(percent_discount, False)