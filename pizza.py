#Name: Elijah Allen-Straton
#Program: Palmero Pizza

import datetime
#Static Variables


DRINK = 3.99
BREAD = 6.99
SALESTR = 0.055


#Dynamic Variables

num_pizza = 0
num_drink = 0
num_bread = 0
pizza_size = 0
pizza_cost = 0
drink_cost = 0
bread_cost = 0
subtotal = 0
taxamt = 0
total = 0

#functions

def reset():
    num_pizza = 0
    num_drink = 0
    num_bread = 0
    pizza_size = 0
    pizza_cost = 0
    drink_cost = 0
    bread_cost = 0
    subtotal = 0
    taxamt = 0
    total = 0


def main():

    another_order = True
    while another_order:
        userdata()
        calc()
        results()
        reset()

        askAgain = input("\nWould you like to make another purchase? (Yes or No): ")
        if askAgain.upper() == "No" or askAgain == "no" or askAgain == "n":
            another_order = False
            print("\nThank you for your order!")

def userdata():
    global num_drinks, num_bread, num_pizza, pizza_sizes, pizza_cost, drink_cost, bread_cost, pizza_prices, pizza_code
    pizza_sizes = []
    pizza_code = ["S", "M", "L", "XL", "none"]
    pizza_prices = [9.99, 12.99, 17.99, 21.99, 0]
    pizza_loop = True
    while pizza_loop:
        ask_pizza = input("\nWhat size pizza would you like? (S, M, L, XL, or none): ")
        if ask_pizza == "S" or ask_pizza == "M" or ask_pizza == "L" or ask_pizza == "XL" or ask_pizza == "none":
            pizza_sizes.append(ask_pizza)
            redo_pizza = True
            while redo_pizza:
                ask_again = input("\nWould you like another pizza? (Y or N): ")
                if ask_again == "Y" or ask_again == "y":
                    redo_pizza = False
                else:
                    print("\nOk, got it!")
                    redo_pizza = False
                    pizza_loop = False
        else:
            print("\nINVALID INPUT")
    for i in range(len(pizza_sizes)):
        if pizza_sizes[i] == pizza_code[0]:
            pizza_cost += pizza_prices[0]
        elif pizza_sizes[i] == pizza_code[1]:
            pizza_cost += pizza_prices[1]
        elif pizza_sizes[i] == pizza_code[2]:
            pizza_cost += pizza_prices[2]
        elif pizza_sizes[i] == pizza_code[3]:
            pizza_cost += pizza_prices[3]
        else:
            pizza_sizes[i] == pizza_code[4]
            pizza_cost += pizza_prices[4]
    ask_drinks = input("\nWould you like any drinks? (Y or N): ")
    if ask_drinks == "Y" or ask_drinks == "y":
        num_drinks = int(input("\nHow many drinks would you like to order?: "))
        print("\nOk, got it!")
    else:
        num_drinks = 0
        print("\nNone this time, thats fine!")
    ask_bread = input("\nWould you like any breadsticks? (Y or N): ")
    if ask_bread == "Y" or ask_bread == "y":
        num_bread = int(input("\nHow many orders of breadsticks would you like to place?: "))
        print("\nOk, got it!")
    else:
        num_bread = 0
        print("\nNone this time, thats fine!")
        
def calc():
    global num_drinks, num_bread, num_pizza, pizza_cost, drink_cost, bread_cost, taxamt, subtotal, total
    drink_cost = num_drinks * DRINK
    bread_cost = num_bread * BREAD
    subtotal = pizza_cost + drink_cost + bread_cost
    taxamt = subtotal * SALESTR
    total = subtotal + taxamt

def results():
    moneyf = '8.2f'
    print('-----------------------------------')
    print('        ** Palmero Pizza **        ')
    print('    Bringing You Classic Pizza     ')
    print('            Since 1939             ')
    print('-----------------------------------')
    print('Pizza            $ ' + format(pizza_cost, moneyf))
    print('Breadsticks      $ ' + format(bread_cost, moneyf))
    print('Drinks           $ ' + format(drink_cost, moneyf))
    print('___________________________________')
    print('Sales Tax        $ ' + format(taxamt, moneyf))
    print('Subtotal         $ ' + format(subtotal, moneyf))
    print('Total            $ ' + format(total, moneyf))
    print('-----------------------------------')
    print(str(datetime.datetime.now()))
    

main()
    
              
    
    
                    
    



