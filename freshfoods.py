# Name: your name here
# Prog Purpose: This program creates a payroll report
import datetime
############## LISTS of data ############
emp = [
    "Smith, James      ",
    "Johnson, Patricia ",
    "Williams, John    ",
    "Brown, Michael    ",
    "Jones, Elizabeth  ",
    "Garcia, Brian     ",
    "Miller, Deborah   ",
    "Davis, Timothy    ",
    "Rodriguez, Ronald ",
    "Martinez, Karen   ",
    "Hernandez, Lisa   ",
    "Lopez, Nancy      ",
    "Gonzales, Betty   ",
    "Wilson, Sandra    ",
    "Anderson, Margie  ",
    "Thomas, Daniel    ",
    "Taylor, Steven    ",
    "Moore, Andrew     ",
    "Jackson, Donna    ",
    "Martin, Yolanda   ",
    "Lee, Carolina     ",
    "Perez, Kevin      ",
    "Thompson, Brian   ",
    "White, Deborah    ",]
job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
       "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M",]

hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
         28, 31, 37, 32, 36, 22, 28, 29, 21, 31]

num_emps = len(emp)

#-------lists------#

total_gross = 0
total_net = 0

gross_pay = []
net_pay = []
fed_tax = []
state_tax = []
ssamt = []
medicare = []
retirement = []

#------static tuples------#
#             C      S      J      M
PAY_RATE = (16.50, 15.75, 15.75, 19.50)

#           fed   state   ss     med  retire
DED_RATE = (0.12, 0.03, 0.062, 0.0145, 0.04)


#-----program functions-----#

def main():
    calc()
    results()

def calc():
    global total_gross, total_net

    for i in range(num_emps):
        if job[i] == "C":
            pay = hours[i] * PAY_RATE[0]
        elif job[i] == "S":
            pay = hours[i] * PAY_RATE[1]
        elif job[i] == "J":
            pay = hours[i] * PAY_RATE[2]
        else:
            pay = hours[i] * PAY_RATE[3]

        fed = pay * DED_RATE[0]
        state = pay * DED_RATE[1]
        ss = pay * DED_RATE[2]
        med = pay * DED_RATE[3]
        retire = pay * DED_RATE[4]

        net = pay - fed - state - ss - med - retire

        total_gross += pay
        total_net += net

        gross_pay.append(pay)
        net_pay.append(net)
        fed_tax.append(fed)
        state_tax.append(state)
        ssamt.append(ss)
        medicare.append(med)
        retirement.append(retire)


def results():
    moneyf = '8,.2f'
    moneyf2 = '12,.2f'
    tab = "\t"

    print("--------------------------------------------")
    print("           Fresh Food Supermarket      ")
    print("           -Weekly Payroll Report-     ")
    print(tab + str(datetime.datetime.now()))
    print("--------------------------------------------")
    titles1 = "Emp Name" + tab + "Code" + tab + "Gross" + tab
    titles2 = "Fed Inc Tax" + tab + "State Inc Tax" + tab + "Soc Sec" + tab + " " + "Medicare" + "   " + "Net"
    print( titles1 + titles2)
    print("---------------------------------------------------------------------------------------------")

    for i in range(num_emps):
        data1 = emp[i]+ " " + job[i] + "  " + format(gross_pay[i], moneyf)
        data2 = "  " + format(fed_tax[i],moneyf) + "         " + format(state_tax[i], moneyf) + "     " + format(ssamt[i], moneyf)
        data3 = " " + format(medicare[i],moneyf) + "  " + format(retirement[i], moneyf)
        print(data1 + data2 + data3)
    print("----------------------------------------")
    print("             Total Gross: $" + format(total_gross, moneyf2))
    print("             Total Net  : $" + format(total_net, moneyf2))
    print("----------------------------------------")

######
main()
        

    
