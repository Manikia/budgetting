import data

value = input("Insert name, product name, category, and price in order: \n")
(name, product, category, price) = value.split(' ')

print(name)
print(product)
print(category)
print(price)

data.creatingData()