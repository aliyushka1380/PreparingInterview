"""
3. Усовершенствовать родительский класс таким образом,
чтобы получить доступ к защищенным переменным.
"""
class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


    def name(self):
        return self.__name


    def price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'Наименование товара: {self.name()}. Цена: {self.price()}'


Item = ItemDiscountReport("Брюки", 1000)
print(Item.get_parent_data())
