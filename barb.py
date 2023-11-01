#Names: Elijah, Micheal
#Purpose: Customer reciept for a Barbecue Buffet
import datetime

### Global Variables
SALES_TAX_RATE=.062
ADULT_PRICE=19.95
CHILD_PRICE=11.95
SERVICE_FEE=.1
subtotal=0
numadult=0
numchild=0
adulttotal=0
childtotal=0
total=0
taxval=0
serviceval=0

### Functions
def main():
    ordermore=True
    while ordermore:
        userinput()
        calc()
        display()
        askinput=input("\nWould you like you order again? (Y/N): ")
        if askinput.upper()=="N" or askinput=="n":
            ordermore=False
            print("Thank you for your order! Please come again soon!")
def userinput():
    global numadult, numchild
    numadult=int(input("Number of Adult Meals: "))
    numchild=int(input("Number of Child Meals: "))


def calc():
    global subtotal, total, taxval, serviceval, adulttotal, childtotal
    adulttotal = numadult * ADULT_PRICE
    childtotal = numchild * CHILD_PRICE
    subtotal = adulttotal + childtotal
    taxval = subtotal * SALES_TAX_RATE
    serviceval = subtotal * SERVICE_FEE
    total = subtotal + taxval + serviceval

def display():
    moneyf = '8.2f'
    print('-----------------------------------')
    print('   ** Branch Barbecue Buffet **    ')
    print('-----------------------------------')
    print('Adults          $ ' + format(adulttotal, moneyf))
    print('Children        $ ' + format(childtotal, moneyf))
    print('___________________________________')
    print('Subtotal        $ ' + format(subtotal, moneyf))
    print('Sales Tax       $ ' + format(taxval, moneyf))
    print('Service Fee     $ ' + format(serviceval, moneyf))
    print('Total           $ ' + format(total, moneyf))
    print('-----------------------------------')
    print(str(datetime.datetime.now()))

#####
main()



