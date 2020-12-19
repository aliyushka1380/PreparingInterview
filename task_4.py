"""
4. Реализовать возможность переустановки значения цены товара.

Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
Следует проверить это, вызвав соответствующий метод родительского класса
и функцию дочернего (функция,
отвечающая за отображение информации о товаре в одной строке).
"""
class ItemDiscount:  # объявляем родительский класс
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


    def name(self):
        return self.__name


    def price(self):
        return self.__price


    def new_price(self, price):
        self.__price = price


class ItemDiscountReport(ItemDiscount):  # объявляем класс наследник
    def get_parent_data(self):
        return f'Наименование товара: {self.name()}. Цена: {self.price()}'


Item = ItemDiscountReport("Брюки", 1000)
print(Item.get_parent_data())
Item.new_price(30)
print(Item.get_parent_data())
