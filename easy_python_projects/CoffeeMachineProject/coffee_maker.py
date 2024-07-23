class CoffeeMaker:
    def __init__(self):
        #resources of coffee machine
        self.resources={
            "water":300,
            "milk":200,
            "coffee":100,
        }
    def report(self):
        #Prints a report of all resources
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml ")
        print(f"Coffee: {self.resources['coffee']}ml")

    def is_resources_sufficient(self,drink):
        #Returns the boolean value if the drink can be made
        can_make=True
        for item in drink.ingredients:
            if drink.ingredients[item]>self.resources[item]:
                can_make=False
                print(f"Sorry there is not enough {item}")

        return can_make

    def make_coffee(self,order):
        #make coffee form avaible indgredients
        for item in order.ingredients:
            self.resources[item]-=order.ingredients[item]
        print(f"Here is your {order.name}. Enjoy!")
