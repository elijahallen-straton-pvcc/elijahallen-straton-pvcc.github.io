#Name: Elijah
#Program Purpose: Finds the price of pet vaccines and medicines for dogs and cats
#
# Pricing for Vaccination
# Canine:
#---------------------------#
# 1. Bordatella $30.00
# 2. DAPP $35.00
# 3. Influenza $48.00
# 4. Leptopirosis $21.00
# 5. Lyme Disease $41.0
# 6. Rabies $25.00
# 7. Vaccine Package Including All Vaccines 15% Discount
#
#Heart Worm Chew Medication Pricing 
# Small Dogs, (0-25lbs): $9.99
# Medium Dogs, (26-50lbs): $11.99
# Large Dogs, (51-100+lbs): $13.99

import datetime

#--------Static Variables Dogs--------#

PR_BORD = 30
PR_DAPP = 35
PR_FLU = 48
PR_LEP = 21
PR_LYME = 41
PR_RABIES = 25

PR_ALL = 200

PR_SM = 9.99
PR_MED = 11.99
PR_LG = 13.99


#--------Functions--------#

def main():
    more = True
    while more:
        user_data()

        if pet_type.upper() == "D":
            get_dog_data()
            perform_dog_calc()
            display_dog_results()
        else:
            get_cat_data()
            perform_cat_calc()
            display_cat_data()

        askAgain = input("\nWould you like to process another pet? (Y or N): ")
        if askAgain.upper() == "N":
            more = False
            print("Thank you for trusting Woodburry Vetenarians Office with vaccinating and medicating your pet!")

def user_data():
    global pet_name, pet_type, pet_weight
    pet_name = input("What is the name of your pet?: ")
    pet_type = input("Is your pet a dog or a cat? (D or C): ")
    pet_weight = int(input("What is the weight of your pet? (In pounds): "))


#-----------Dog Functions------------#

def get_dog_data():
    global vax_type, num_chews
    dog1 = "\n Dog Vaccines: \n 1. Bordatella \n 2. DAPP \n 3. Influenza \n 4. Leptopirosis"
    dog2 = "\n 5. Lymes Disease \n 6. Rabies \n 7. Full Vaccine Package \n 8. NONE"
    dogmenu = dog1 + dog2
    vax_type = int(input(dogmenu + "\n Enter vaccine number: "))
    print("\nMonthly heart worm preventation medication is reccomended for all dogs")
    heart_yesno = input("\tWould you like to order monthly heartworm medication for " + pet_name + "? (Y or N): ")
    if heart_yesno.upper() == "Y":
        num_chews = int(input("\tHow many heart worm chews would you like to order? "))
    else:
        num_chews = 0

def perform_dog_calc():
    global vax_cost, vax_name, chews_cost, total1

    if vax_type == 1:
        vax_cost = PR_BORD
        vax_name = "Bordatella"

    elif vax_type == 2:
        vax_cost = PR_DAPP
        vax_name = "DAPP"

    elif vax_type == 3:
        vax_cost = PR_FLU
        vax_name = "Influenza"

    elif vax_type == 4:
        vax_cost = PR_LEP
        vax_name = "Leptopirosis"

    elif vax_type == 5:
        vax_cost = PR_LYME
        vax_name = "Lyme Disease"

    elif vax_type == 6:
        vax_cost = PR_RABIES
        vax_name = "Rabies"

    elif vax_type == 7:
        vax_cost = .85 * PR_ALL
        vax_name = "Full Vaccine Package"

    else:
        vax_cost = 0
        vax_name = "NONE"

    if num_chews != 0:
        if pet_weight < 25:
            chews_cost = num_chews * PR_SM
        elif pet_weight >= 26 and pet_weight < 50:
            chews_cost = num_chews * PR_MED

        else:
            chews_cost = num_chews * PR_LG
    else:
        chews_cost = 0

    total1 = vax_cost + chews_cost

def display_dog_results():
    moneyf = '8,.2f'


    
    print("--------------------------------")
    print("  Woodburry Vetenarians Office  ")
    print("       *       *       *        ")
    print(str(pet_type))
    print(str(pet_name) + "'s Visit")
    print(str(pet_name) + " weighed " + str(pet_weight) + "lbs!")
    print("--------------------------------")
    print("             Recipt             ")
    print("                                ")
    print(" Vaccination Selection: " + format(vax_name))
    print(" Vaccination Price:     " + format(vax_cost, moneyf))
    print(" Number of Chews:       " + format(num_chews, moneyf))
    print(" Chews Price:           " + format(chews_cost, moneyf))
    print(" Total:                 " + format(total1, moneyf))
    print("--------------------------------")
# Pricing for Vaccination
# Feline:
#---------------------------#
# 1. Feline Leukemia $35.00
# 2. Feline Viral Rhinotracheitis $30.00
# 3. Rabies $25.00
# 4. Vaccine Package Including All Vaccines 10% Discount
#
# Heart Worm Chew Medication Pricing
# One Size: $8.00



#--------Static Variables Cats--------#
    
PR_LUK = 35
PR_VIR = 30
PR_RAB = 25
PR_FULL = 0

PR_CHEW = 8



#-----------Cat Functions------------#

def get_cat_data():
    
    global type_vax, chews_num
    cat1 = "\n Cat Vaccines: \n 1. Feline Leukemia \n 2. Feline Viral Rhinotracheitis"
    cat2 = "\n 3. Rabies \n 4. Full Vaccine Package \n 5. NONE"
    catmenu = cat1 + cat2
    type_vax = int(input(catmenu + "\n Enter vaccine number: "))
    print("\nMonthly heart worm preventation medication is reccomended for all cats")
    heart_yesno = input("\tWould you like to order monthly heartworm medication for " + pet_name + "? (Y or N): ")
    if heart_yesno.upper() == "Y":
        chews_num = int(input("\tHow many heart worm chews would you like to order? "))
    else:
        chews_num = 0


def perform_cat_calc():
    global type_vax, name_vax, cost_vax, cost_chews, total2

    if type_vax == 1:
        cost_vax = PR_LUK
        name_vax = "Feline Leukemia"

    elif type_vax == 2:
        cost_vax = PR_VIR
        name_vax = "Feline Viral Rhinotracheitis"

    elif type_vax == 3:
        cost_vax = PR_RAB
        name_vax = "Rabies"

    elif type_vax == 4:
        cost_vax = PR_FULL
        name_vax = "Full Vaccine Package"

    else:
        
        cost_vax = 0
        name_vax = "NONE"

    if chews_num != 0:
        cost_chews = chews_num * PR_CHEW

    else:
        cost_chews = 0

    total2 = cost_vax + cost_chews

def display_cat_data():
    moneyf = '8,.2f'

    
    print("---------------------------------------------------")
    print("          Woodburry Vetenarians Office             ")
    print("                *       *       *                  ")
    print(str(pet_type))
    print(str(pet_name) + "'s Visit")
    print(str(pet_name) + " weighed " + str(pet_weight) + "lbs!")
    print("---------------------------------------------------")
    print("                       Recipt                      ")
    print("                                                   ")
    print(" Vaccination Selection: " + format(name_vax))
    print(" Vaccination Price:     " + format(cost_vax, moneyf))
    print(" Number of Chews:       " + format(chews_num, moneyf))
    print(" Chews Price:           " + format(cost_chews, moneyf))
    print(" Total:                 " + format(total2, moneyf))
    

#------ Run ------#
main()
    
    
