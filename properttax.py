# Name: Elijah Allen-Straton
#Program: Personal Property Tax Input Loop

import datetime

#__________________#

PPT = 0.042
PPTR = 0.33


#__________________#

annualtax = 0
bianntax = 0
reliefbuis = 0
reliefplate = 0
carvalue = 0
total = 0


#__________________#

def main():
    more = True
    while more:
        get_data()
        calc()
        show_results()
        reset()
        yesno = input("\n Would you like to process another vehicle? (Yes or No): ")
        if yesno == "n" or yesno == "no" or yesno == "No" or yesno == "NO":
            more = False

def get_data():
    global carvalue, reliefgranted, reliefbuis, reliefplate
    carvalue = int(input("Please enter the current value of your vehicle: $"))
    reliefbuis = input("Is this vehicle used primarily for non-buisness purpposes? (Y/N): ")
    reliefplate = input("Does this vehicle have passenger license plates? (Y/N): ")
    

def calc():
    global carvalue, relief, total, bianndue, bianntax, annualtax, reliefbuis, reliefplate
    annualtax = carvalue * PPT
    bianntax = annualtax / 2
    if reliefbuis =="y" and reliefplate == "y":
        relief = bianntax * PPTR
    else:
        relief = 0
    total = bianntax - relief

def show_results():
    moneyf = '8.2f'
    print("                      ")
    print('-----------------------------------')
    print('           Tax Reciept            ')
    print('-----------------------------------')
    print('Value of Vehicle       $ ' + format(carvalue, moneyf))
    print('Annual Amount Due     +$ ' + format(annualtax, moneyf))
    print('Amount Due This Term  +$ ' + format(bianntax, moneyf))
    print('Relief Amount         -$ ' + format(relief, moneyf))
    print('Total                  $ ' + format(total, moneyf))
    print('-----------------------------------')
    print(str(datetime.datetime.now()))

def reset():
    annualtax = 0
    bianntax = 0
    reliefbuis = 0
    reliefplate = 0
    carvalue = 0
    total = 0
        
    

#__________________#
main()



            
            
    
    



