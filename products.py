#create a Product class that has 3 attributes: a name, a price, and a category. 
# All of these should be provided upon creation.


class Product:
    count = 0

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        Product.count += 1
        self.id = Product.count

#print product info
    def print_info(self):
        print({'id': self.id, 'name': self.name, 'price': self.price, 'category': self.category})
        return self

#updates the product's price. 
# If is_increased is True, the price should increase by the percent_change provided. 
# If False, the price should decrease by the percent_change provided.
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += (self.price * percent_change)
        else:
            self.price -= (self.price * percent_change)
        return self



