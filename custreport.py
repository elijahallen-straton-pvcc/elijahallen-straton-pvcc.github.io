#Name: Elijah Allen-Straton
#Prog Purpose: Read in a list of customers and display a report that will increase the amount owed by 10%


cust = []

def main():
    read_in_cust_file()
    display_cust_list()

def read_in_cust_file():
    cust_data = open("customer_data_file.csv", "r")
    cust_in = cust_data.readlines()
    cust_data.close()

    for i in cust_in:
        cust.append(i.split(","))

def display_cust_list():

    total = 0
    moneyf = "8,.2f"

    print("---------------------------------------")
    print("         Customer Sales Report         ")
    print(" ")

    for i in range(len(cust)):
        amt_owed = float(cust[i][2]) * 1.10
        total += amt_owed
        print(cust[i][1] + "     \t" + cust[i][0] + "  \t" + format(amt_owed, moneyf))
    print("---------------------------------------")
    print("Total Amount: \t$" + format(total, moneyf))

main()
