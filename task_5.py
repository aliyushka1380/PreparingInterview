"""
5. Реализовать расчет цены товара со скидкой.

Величина скидки должна передаваться в качестве аргумента в дочерний класс.

Выполнить перегрузку методов конструктора дочернего класса
(метод init, в который должна передаваться переменная — скидка),
и перегрузку метода str дочернего класса.

В этом методе должна пересчитываться цена и возвращаться результат —
цена товара со скидкой.

Чтобы все работало корректно, не забудьте инициализировать дочерний
и родительский классы
(вторая и третья строка после объявления дочернего класса).
"""
class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


    def name(self):
        return self.__name


    def price(self):
        return self.__price


    def new_price(self, price):
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount


    def get_parent_data(self):
        return f'Наименование товара: {self.name()}. Цена: {self.price()}'


    def __str__(self):
        return f'Наименование товара: {self.name()}, ' \
            f'Цена товара со скидкой: {self.price() - self.discount}'


Item = ItemDiscountReport("Брюки", 1000, 5)
print(Item.get_parent_data())
print(Item)
