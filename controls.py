import store
import products

prod1 = products.Product('carrot', 3, "veggie")
prod2 = products.Product('apple', 1, 'fruit')

store1 = store.Store('Fast Shop')


prod1.update_price(.50 , False)

store1.add_product(prod1)\
    .add_product(prod2)

# print(prod1.price, prod2.price)

store1.inflation(.50)

# print(prod1.price, prod2.price)

store1.set_clearance('fruit', .10)

# print(prod1.price, prod2.price)

store1.sell_product(1)
print(store1.products)