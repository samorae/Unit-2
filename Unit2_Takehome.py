class Pizza: 
    def __init__(self, sauce, topping, crust):
        self.sauce = sauce
        self.topping = topping
        self.crust = crust
    def __repr__(self):
        return f'This is a {self.topping} pizza, with {self.crust} crust and {self.sauce} sauce.'
menu = ('''           __________________________________________
           |   Sauce    |   Crust   |   Topping's   |
           |Marinara    |Normal     |None(Cheese)   |
           |Alfredo     |Cheesy     |Pepperoni      |
           |Garlic Parm |Garlic     |Sausage        |
           |Buffalo     |Deep Dish  |Mushroom       |
''')
print(menu)
pizza = Pizza('Marinara', 'Pepperoni', 'Cheesy')
print(pizza)