class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        content = file.read()
        file.close()
        return content

    def add(self, *products: Product):
        str1 = self.get_products().split('\n')
        for product in products:
            if str(product) in str1:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(str(product) + '\n')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
