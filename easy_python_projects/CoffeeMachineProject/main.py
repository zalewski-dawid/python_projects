#Coffee Machine in OOP
import coffee_maker
#Program requirements
#1.Print report
#2.Check resources sufficient?
#3.Process coins
#4.Check transition successful?
#5.Make Coffee


#IF YOU WANT TO EXIT TYPE 'off'

from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
menu=Menu()



my_coffee_maker.report()
my_money_machine.report()


is_on=True
while is_on:
    options=menu.get_items()
    choice=input(f"What would you like {options}: ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        my_coffee_maker.report()
        my_money_machine.report
    else:
        drink=menu.find_items(choice)
        if my_coffee_maker.is_resources_sufficient(drink):
            #Take payment from the user


            if my_money_machine.make_payment(drink.cost):
                my_coffee_maker.make_coffee(drink)