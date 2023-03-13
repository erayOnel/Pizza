import csv
import datetime
class Pizza:
    def __init__(self, name, cost, desc):
        self.__name = name
        self.__cost = cost
        self.__desc = desc

    def get_name(self):
        return self.__name

    def get_cost(self):
        return self.__cost

    def get_desc(self):
        return self.__desc


class Decorator(Pizza):

    def __init__(self, name, cost, desc):
        super().__init__(name, cost, desc)
        self.__name = name
        self.__cost = cost
        self.__desc = desc

    def get_name(self):
        return self.__name

    def get_cost(self):
        return self.__cost

    def get_desc(self):
        return self.__desc


Classic = Pizza("Classic", 25.00, "Tomato, olive, cheese and basil")
Margherita = Pizza("Margherita", 30.00, "Tomatoes, mozzarella cheese, garlic, fresh basil")
Pepperoni = Pizza("Pepperoni", 40.00, "Oil, beef sauce, pepperoni, black and red pepper, cheese")
Hawaiian = Pizza("Hawaiian", 35.00, "Tomato sauce, pineapple, mozzarella, boiled ham")

f_list = [Classic, Margherita, Pepperoni, Hawaiian]
customerPizza = input("Menu: Classic, Margherita, Pepperoni, Hawaiian\nChoose a pizza from the menu:")

co = []
db_list = []


def engage():
    for q in f_list:
        if q.get_name() == customerPizza:
            co.append(q.get_cost())
            db_list.append(f"Pizza type: {q.get_name()} ")
            return f"Price: {q.get_cost()}, Ingredients: {q.get_desc()}\n"
    raise "Enter a valid choose"


print(engage())

Olive = Decorator("Olive", 5.25, "Olive description")
Mushroom = Decorator("Mushroom", 3.50, "Mushroom description")
Meat = Decorator("Meat", 8.75, "Meat description")
Onion = Decorator("Onion", 4.50, "Onion description")
Sweetcorn = Decorator("Sweetcorn", 6.30, "Sweetcorn description")

customerDecorator = input("Additionals: Olive, Mushroom, Meat, Onion, Sweetcorn or No ingredients\nChoose an additional:")

s_list = [Olive, Mushroom, Meat, Onion, Sweetcorn]


def engage_2():
    for m in s_list:
        if customerDecorator == "No ingredients":
            return f"No ingredients, Total price: {sum(co)}"
        elif m.get_name() == customerDecorator:
            co.append(m.get_cost())
            db_list.append(f"Additional: {m.get_name()} ")
            return f"Price: {m.get_cost()}, Ingredients: {m.get_desc()}, Total price: {sum(co)}\n"
    raise "Enter a valid choose"


print(engage_2())

forDate = datetime.datetime.now()

db_list.append(f'Nickname: {input("Enter a nickname:")} ')
db_list.append(f'Card Owner: {input("Enter the name written on your credit card:")} ')
db_list.append(f'Card Password: {input("Enter the credit card password:")} ')
db_list.append(f"Date: {[forDate.year, forDate.month, forDate.day, forDate.hour]} ")
print(db_list)

myFile = open("Orders_Database.csv", "a")
writer = csv.writer(myFile)
writer.writerow(db_list)
myFile.close()
