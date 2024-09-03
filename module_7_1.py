class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop(Product):
    def __init__(self, name, weight, category):
        super().__init__(name, weight, category)
        self.__file_name = 'products.txt'
    def get_products(self):
        list1 = open("__file_name", "r")
        print(list1.read())
        list1.close()

    def add(self, *products):
        list1 = open("__file_name", "w")
        if self.Product.category in list1.read():
            print(f'Продукт {products} уже есть в магазине')
        else:
           list1.write(self)
        print(list1)
        list1.close()




s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())