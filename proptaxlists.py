#Name: Elijah Allen-Straton
#Program: Personal Property Tax using lists

#PPT in cville is $4.20 per $100 of vehicle value (4.2% per year)
#               --Paid every six months
#PPTR (Relif)
#Relief for qualified vehicles in 33%

import datetime


PPT = 0.042
PPTR = 0.33


#--List Data--#

vehicle = ["2019 Volvo  ",
           "2018 Toyota",
           "2022 Kia   ",
           "2020 Ford  ",
           "2023 Honda ",
           "2019 Lexus "]

vehicle_value = [13000, 10200, 17000, 21000, 28000, 16700]

pptr_eligible = ["Y", "Y", "N", "Y", "N", "Y"]

owner_names = ["Brand, Debra      ",
               "Smith, Carter     ",
               "Johnson, Bradley  ",
               "Garcia Jennifer   ",
               "Henderson, Leticia",
               "White, Danielle   "]

ppt_owed = []

num_vehicles = len(vehicle)
tax_due = 0
total = 0


#--Program Functions--#

def main():
    calc()
    results()

def calc():
    global total

    for i in range(num_vehicles):
        tax_due = (vehicle_value[i] * PPT) / 2

        if pptr_eligible[i].upper() == "Y":
            tax_due = tax_due * .67

        ppt_owed.append(tax_due)

        total = total + tax_due
     
def results():
    moneyf = '8,.2f'
    tab = "\t"

    print("------------------------------------------------------------")
    print("                Personal Property Tax Report                ")
    print("                  Charlottesville, Virginia                 ")

    print("\n\tRUN DATE/TIME: " + str(datetime.datetime.now()))
    print("------------------------------------------------------------")
    print("  NAME" + "                   "  "VEHICLE" + "          " + "VALUE" + "       " + "RELIEF" + "      " + "TAX DUE")
    for i in range(num_vehicles):
        dataline1 = owner_names[i] + tab + vehicle[i] + tab + format(vehicle_value[i],moneyf) + tab
        dataline2 = pptr_eligible[i] + tab + " " + format(ppt_owed[i],moneyf)
        print(dataline1 + dataline2)

    print("------------------------------------------------------------")
    print("***********************************TOTAL TAX DUE: $" + format(total,moneyf))

main()





        
