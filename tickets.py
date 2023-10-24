#Name: Elijah Allen-Straton
#Prog Pourpose: This Program finds the cost of movie tickets
# Price for one ticket: $10.99
# Price for one ticket: $4.99
# Sales tax rate: 5.5%
# Price for one bucket of popcorn; $12.99

import datetime

###### define global vairiables #######
#Pythonic coding dictates that it is understood that...
#uppercase variables should dont change 
SALES_TAX_RATE = .055
PR_TICKET = 10.99
PR_POPCORN = 12.99
PR_DRINK = 4.99

# define global variable
num_tickets = 0
num_pop = 0
num_drinks = 0
cost_tickets = 0
cost_pop = 0
cost_drinks = 0
subtotal = 0
sales_tax = 0
total = 0

#### define program function ####
def main():

    more_tickets = True

    while more_tickets:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nWould you like to make another purchase? (Yes or No):")
        if askAgain.upper() == "No" or askAgain == "no" or askAgain == "n":
            more_tickets = False
            print("\nThank you for your order!")

def get_user_data():
    global num_tickets, num_pop, num_drinks
    num_tickets = int(input("Number of Movie Tickets:"))
    num_pop = int(input("Number of Popcorn Buckets:"))
    num_drinks = int(input("Number of Drinks:"))

def perform_calculations():
    global subtotal, sales_tax, total, cost_pop, cost_tickets, cost_drinks
    cost_tickets = num_tickets * PR_TICKET
    cost_pop = num_pop * PR_POPCORN
    cost_drinks = num_drinks * PR_DRINK
    subtotal = cost_tickets + cost_pop + cost_drinks
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
#the "f" in moneyf stands for floating point, therefor this variable
# serves the pourpose of definining the floating point
    moneyf = '8.2f'
    print('-----------------------------------')
    print('     **  Old School Theatre **     ')
    print('   Showing for "Old Timey Movie"   ')
    print('            at 7:30pm              ')
    print('-----------------------------------')
    print('Tickets         $ ' + format(cost_tickets, moneyf))
    print('Popcorn         $ ' + format(cost_pop, moneyf))
    print('Drinks          $ ' + format(cost_drinks, moneyf))
    print('___________________________________')
    print('Subtotal        $ ' + format(subtotal, moneyf))
    print('Sales Tax       $ ' + format(sales_tax, moneyf))
    print('Total           $ ' + format(total, moneyf))
    print('-----------------------------------')
    print(str(datetime.datetime.now()))

#### call on main program to execute ####
main()




