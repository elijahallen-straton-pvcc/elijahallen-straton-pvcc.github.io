#Name: Elijah-Allen-Straton
#Prog Purpose: This program reads in a hotel data file, performs calculations, and creates an HTML file for the results

import datetime

############ define rate tuples ############

#             SR  DR  SU
#              0   1   2
ROOM_RATES = (195,250,350)

#            s-tax occ-tax
#              0      1
TAX_RATES = (0.065,0.1125)
 
########### define files and list ############
infile = "emerald.csv"
outfile = "emerald-web-page.html"

guest = [] 

############ define program functions ############
def main():
    read_in_guest_file()
    perform_calculations()
    open_out_file()
    create_output_html()
            
def read_in_guest_file():
    guest_data = open(infile, "r")
    guest_in = guest_data.readlines()
    guest_data.close()

    for i in guest_in:
        guest.append(i.strip().split(","))



# In the split list (guest) the columns are as follows
#        0           1          2            3
#    Last Name   First Name  Room Type  Nights Stayed
#EX.  [['Allen',  'Elijah,'    'SR,'        '4\n'],    [etc.]
#(ignoring the spaces)

       

def perform_calculations():
    global grandtotal, i, subtotal, salestax, occupancy, total
    grandtotal=0
    
    for i in range(len(guest)):
            room_type = str(guest[i][2])
            num_nights = int(guest[i][3])

            if room_type == "SR":
                subtotal = ROOM_RATES[0] * num_nights

            elif room_type == "DR":
                subtotal = ROOM_RATES[1] * num_nights

            else:
                subtotal = ROOM_RATES[2] * num_nights

                    
            salestax  = subtotal * TAX_RATES[0]
            occupancy = subtotal * TAX_RATES[1]
            total = subtotal + occupancy + salestax
             
            grandtotal += total
        
      
            guest[i].append(subtotal)
            guest[i].append(salestax)
            guest[i].append(occupancy)
            guest[i].append(total)


def open_out_file():        
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style = "background-color: #39A15A; background-image: url(emeraldbg.jpg); " color: #000000;">\n')

    
def create_output_html():
    global f
    
    moneyf = '8.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "7"; style = "text-align: center;">'
    sp = " "

    f.write('\n<table border="3"   style ="background-color: #39A15A;  font-family: georgia; margin: auto;">\n')            
    f.write(colsp + '\n')
    f.write('<h2 style: "text-align: center;"> Emerald Beach Hotel and Resort </h2></td></tr>')
    f.write(tr + 'Last Name' + endtd + 'First Name' + endtd + 'Number of Nights' + endtd + 'Subtotal' + endtd + 'Sales Tax' + endtd + 'Occ. Tax' + endtd + 'Total' + endtr)

    for g in guest:
        f.write(tr + g[1] + endtd + g[0] + endtd + g[3] + endtd + format(g[4], moneyf) + endtd + format(g[5], moneyf) + endtd + format(g[6], moneyf) + endtd + format(g[7], moneyf) + endtr) 

    f.write(colsp + 'Grand Total $' + format(grandtotal, moneyf))
    f.write(colsp + 'Date/Time: '+ day_time + endtr)

    f.write('</table><br />')
    f.write("</body></html>")
    f.close()

    print('Open ' + outfile + ' to view data.')

    
    








##call on main program to execute##


    
main()
