import random

from datetime import datetime,timedelta
from datetime import date


import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="mypass", database="restdb")

mycursor = mydb.cursor()
mainmenureturn = ""
credcarddic = {"7819 2506 3324": 776, "0987 7765 6712": 880, "4456 3321 8807": 521}
acseats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
nonacseats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
acseatsres = []
nonacseatsres = []
KingBR = 130
KingBL = 200
QueenBR = 120
QueenBL = 190
CheeseFR = 230
CheeseFL = 270
KingVBR = 100
KingVBL = 190
GTacosV = 175
GTacosNV = 250
CokeR = 120
CokeL = 170
ChocolateSoftie = 200
VanillaSoftie = 200
mycursor.execute('USE restdb')


def userchecker():
    promptch = input("\n DO YOU WISH TO LOGIN?(Y/N): ")
    if promptch != "N":
        while True:
            x = input("\n Enter Username: ")
            y = input("\n Enter Password: ")
            if accountlist[x] == y:
                print("\n YOUR ACCOUNT HAS BEEN VERIFIED")
                print("\n REDIRECTING YOU TO THE MENU PAGE")
                break
            else:
                print("\n THE USERNAME OR PASSWORD YOU HAVE ENTERED IS INCORRECT")
                print("\n PLEASE TRY AGAIN")
    else:
        pass


def customer(username, address, phoneno, order, paymentmethod,date):
    L = []
    uname = username
    L.append(uname)
    add = address
    L.append(add)
    cphone = phoneno
    L.append(cphone)
    o = order
    L.append(o)
    payment = paymentmethod
    L.append(payment)
    cdate = date
    L.append(cdate)
    cust = tuple(L)
    sql = "INSERT INTO delivery(username,address,phonenumber,reciept,methodofpayment,dateoforder) VALUES(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, cust)
    mydb.commit()


def reservation(x, y, z, w, a, b, u):
    L = []
    rname = x
    L.append(rname)
    rphno = y
    L.append(rphno)
    rno = z
    L.append(rno)
    rtype = w
    L.append(rtype)
    rseats = a
    L.append(rseats)
    rday = b
    L.append(rday)
    rtime = u
    L.append(rtime)
    reser = tuple(L)
    sql = "INSERT INTO reservation(Name,phoneno,numberofseats,seattype,seatnumbers,dayofarrival,timeofarrival)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, reser)
    mydb.commit()


def accmaker(x, y):
    accountlist[x] = y
    print("\n WELCOME ", x, "YOU WILL BE REDIRECTED TO OUR MENU PAGE")

def removeitem(c):
    z = {}
    for k in c:
        if c[k] != 0:
            z[k] = c[k]
    for i in z:
        print(i,"Quantity:",z[i])
    while True:
        itemch = input("Enter Item to be removed from the cart(type the exact name of the item): ")
        print("How many",itemch,"do you want to remove from your cart?:")
        qty = int(input())
        if c[itemch]<qty:
            print("Error. Cart items cannot go in negative.")
        else:
            c[itemch]=c[itemch]-qty
            print(qty,itemch,"have been removed from your cart")
            break

def cartshow(x):
    z = {}
    for key in x:
        if x[key] != 0:
            z[key] = x[key]

    print(z)


progch = input("\n DO YOU WISH TO USE THE PROGRAM(Y/N)?: ")

if progch == "Y":
    cost=0
    accountlist = {'rajesh123': 'coolraj123', 'user_12': 'wertpo12', 'bingbing12': "loipiuy125"}
    cartname = {"Regular Veg King Burger": 0, "Regular Queen Burger": 0, "Large Veg King Burger": 0,
                "Large Queen Burger": 0, "Non Veg King Burger": 0, "Large Non Veg King Burger": 0,
                "Regular Cheesy Fries": 0, "Large Cheesy Fries": 0, "Veg Grandeur Tacos": 0,
                "Non Veg Grandeur Tacos": 0,
                "Regular Coke": 0, "Large Coke": 0, "Chocolate Softie": 0, "Vanilla Softie": 0}
    while True:
        print('''                                           WELCOME TO KINGS FAST FOOD RESTARAUNT''')
        usech = int(input('''
 1: HOME DELIVERY
 2: RESERVATION

 PLEASE SELECT ONE OF THE CHOICES:'''))

        if usech == 1:
            while True:

                y = input("\n DOES YOUR ACCOUNT EXIST? (Y/N)?: ")
                if y == "Y":
                    while True:
                        userchecker()
                        break
                else:
                    z = input("\n DO YOU WANT TO CREATE AN ACCOUNT (Y/N)?:  ")
                    if z == "Y":
                        while True:
                            user = input("\n ENTER YOUR USERNAME:  ")
                            pas = input('\n ENTER YOUR PASSWORD:  ')
                            accmaker(user, pas)
                            break
                menuch = input("\n ARE YOU READY TO GET SOME DELICIOUS FOOD (Y/N)?:  ")
                if menuch == "Y":
                    while True:

                        menu = int(input('''
                           * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * *  * * * * * * * * * * * * * * * * * * * * * * * * * * **
                           *                                                        MENU                                                          *
                           *                                                                                      Size        Type         Price  *  
                           * 1) King Burger                                                                                                       *
                           *    The best veg burger in town                                                      Regular      Veg         ₹ 100   *
                           *                                                                                                                      *
                           * 2) Queen Burger                                                                                                      *
                           *    The second best non-veg burger in town                                           Regular     Non-Veg       ₹120   *
                           *                                                                                                                      *
                           * 3) King Burger                                                                                                       *
                           *    The best veg burger in town,but larger                                            Large        Veg         ₹190   *
                           *                                                                                                                      *
                           * 4) Queen Burger                                                                                                      *
                           *    The second best non veg burger in town,but larger                                 Large      Non-Veg       ₹190   *   
                           *                                                                                                                      *
                           * 5) King Burger                                                                                                       *
                           *    The best non-veg burger in town                                                   Regular    Non-Veg       ₹130   *                               
                           *                                                                                                                      *
                           * 6) King Burger                                                                                                       *
                           *    the best non-veg burger in town,but larger                                         Large     Non-Veg       ₹200   *
                           *                                                                                                                      *
                           * 7) Cheesy Fries                                                                                                      *
                           *    The cheesiest fries in town                                                       Regular      Veg         ₹230   *
                           *                                                                                                                      *
                           * 8) Cheesy Fries                                                                                                      *
                           *    The cheesiest fries in town , but larger                                           Large       Veg         ₹270   *
                           *                                                                                                                      *
                           * 9) Grandeur Tacos                                                                                                    *
                           *    the best veg tacos in town                                                        Regular      Veg         ₹175   *
                           *                                                                                                                      *
                           * 10) Grandeur Tacos                                                                   Regular     Non-Veg      ₹250   *
                           *                                                                                                                      *
                           * 11) Coke                                                                             Regular                  ₹120   *
                           *                                                                                                                      *
                           * 12) Coke                                                                              Large                   ₹170   *
                           *                                                                                                                      *
                           * 13) Chocolate Softie                                                                 Regular                  ₹200   *
                           *                                                                                                                      *
                           * 14) Vanilla Softie                                                                   Regular                  ₹200   *
                           * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ** 
                           \n ENTER YOUR CHOICE :   '''))

                        if menu == 1:
                            amt1 = int(input("\n ENTER THE NUMBER OF REGULAR VEG KING BURGERS TO BE ORDERED:    "))
                            print(amt1, "REGULAR VEG KING BURGER HAVE BEEN ADDED TO YOUR FOOD CART")
                            cartname["Regular Veg King Burger"] += amt1
                            cost += amt1 * KingVBR

                        elif menu == 2:
                            amt2 = int(input("\n ENTER THE NUMBER OF REGULAR QUEEN BURGERS TO BE ORDERED:   "))
                            print(amt2, "REGULAR QUEEN BURGER HAVE BEEN ADDED TO YOUR FOOD CART ")

                            cartname["Regular Queen Burger"] += amt2
                            cost += amt2 * QueenBR
                        elif menu == 3:
                            amt3 = int(input("\n ENTER THE NUMBER OF LARGE VEG KING BURGERS TO BE ORDERED:   "))
                            print(amt3, "LARGE VEG KING BURGERS ARE ADDED TO YOUR FOOD CART  ")

                            cartname["Large Veg King Burger"] += amt3
                            cost += amt3 * KingVBL
                        elif menu == 4:
                            amt4 = int(input("\n ENTER THE NUMBER OF REGULAR QUEEN BURGERS TO BE ORDERED:  "))
                            print(amt4, "LARGE QUEEN BURGERS ARE ADDED TO YOUR FOOD CART")

                            cartname["Large Queen Burger"] += amt4
                            cost += amt4 * QueenBL
                        elif menu == 5:
                            amt5 = int(input("\n ENTER THE NUMBER OF REGULAR NON VEG KING BURGERS TO BE ORDERED:  "))
                            print(amt5, "REGULAR NON VEG KING BURGERS ARE ADDED TO YOUR FOOD CART")

                            cartname["Non Veg King Burger"] += amt5
                            cost += amt5 * KingBR
                        elif menu == 6:
                            amt6 = int(input("\n ENTER THE NUMBER OF LARGE NON VEG KING BURGERS TO BE ORDERED:  "))
                            print(amt6, "LARGE NON VEG KING BURGERS ARE ADDED TO YOUR FOOD CART")
                            cartname["Large Non Veg King Burger"] += amt6
                            cost += amt6 * KingBL
                        elif menu == 7:
                            amt7 = int(input("\n ENTER THE NUMBER OF REGULAR CHEESE FRIES TO BE ORDERED:  "))
                            print(amt7, "REGULAR CHEESE FRIES ARE ADDED TO YOUR FOOD CART")
                            cartname["Regular Cheesy Fries"] += amt7
                            cost += amt7 * CheeseFR
                        elif menu == 8:
                            amt8 = int(input("\n ENTER THE NUMBER OF LARGE CHEESE FRIES TO BE ORDERED:  "))
                            print(amt8, "LARGE CHEESE FRIES ARE ADDED TO YOUR FOOD CART ")
                            cartname["Large Cheesy Fries"] += amt8
                            cost += amt8 * CheeseFL
                        elif menu == 9:
                            amt9 = int(input("\n ENTER THE NUMBER OF VEG GRANDEUR TACOS TO BE ORDERED:  "))
                            print(amt9, "VEG GRANDEUR TACOS ARE ADDED TO YOUR FOOD CART")
                            cartname["Veg Grandeur Tacos"] += amt9
                            cost += amt9 * GTacosV
                        elif menu == 10:
                            amt10 = int(input("\n ENTER THE NUMBER OF NON VEG GRANDEUR TACOS TO BE ORDERED:  "))
                            print(amt10, "NON VEG GRANDEUR TACOS HAVE BEEN ADDED TO YOUR FOOD CART ")
                            cartname["Non Veg Grandeur Tacos"] += amt10
                            cost += amt10 * GTacosNV
                        elif menu == 11:
                            amt11 = int(input("\n ENTER THE NUMBER OF REGULAR COKE(s) TO BE ORDERED:  "))
                            print(amt11, "REGULAR COKE(s) HAVE BEEN ADDED TO YOUR FOOD CART")
                            cartname["Regular Coke"] += amt11
                            cost += amt11 * CokeR
                        elif menu == 12:
                            amt12 = int(input("\n ENTER THE NUMBER OF LARGE COKE(s) TO BE ORDERED:    "))
                            print(amt12, "LARGE COKE(s) HAVE BEEN ADDED TO YOUR CART")
                            cartname["Large Coke"] += amt12
                            cost += amt12 * CokeL
                        elif menu == 13:
                            amt13 = int(input("\n ENTER THE NUMBER OF CHOCOLATE SOFTIE(s) TO BE ORDERED: "))
                            print(amt13, "CHOCOLATE SOFTIE(s) HAVE BEEN ADDED TO YOUR CART")
                            cartname["Chocolate Softie"] += amt13
                            cost += amt13 * ChocolateSoftie
                        elif menu == 14:
                            amt14 = int(input("\n ENTER THE NUMBER OF VANILLA SOFTIE(s) TO BE ORDERED:  "))
                            print(amt14, "VANILLA SOFTIE(s) HAVE BEEN ADDED TO YOUR CART")
                            cartname["Vanilla Softie"] += amt14
                            cost += amt14 * VanillaSoftie
                        else:
                            print("\nENTER A VALID NUMBER")
                        totcost = cost + (0.18 * cost)
                        w = input("\nDO YOU WANT TO SEE YOUR CART(Y/N): ")
                        if w == "Y":
                            cartshow(cartname)
                        removeask = input("DO YOU WISH TO REMOVE ANY ITEM FROM YOUR CART(Y/N)?: ")
                        if removeask=="Y":
                            removeitem(cartname)
                        u = input("\nDO YOU WISH TO CHECKOUT(Y/N)?: ")
                        if u == "Y":
                            username = input("\nENTER YOUR USERNAME(TYPE N/A IF YOU AREN'T LOGGED IN): ")
                            address = input("\nENTER YOUR ADDRESS:")
                            while True:
                                phonen0 = int(input("\nENTER YOUR PHONE NUMBER FOR NOTIFICATION UPDATES ON YOUR ORDER:"))
                                if len(str(phonen0))!=10:
                                    print('\nINVALID PHONE NUMBER, TRY AGAIN')
                                else:
                                    break
                            date1 = str(date.today())
                            print("YOUR ORDER:")
                            for key in cartname:
                                if cartname[key] > 0:
                                    print(key, "  ", cartname[key])
                            order = ""
                            for k in cartname:
                                if cartname[k] > 0:
                                    order = order + str(k) + ":" + str(cartname[k]) + ","
                            order = order[0:len(order)-1]
                            curtime = datetime.now()
                            etar = curtime + timedelta(minutes = 30)
                            print("YOUR GRAND TOTAL IS: ", totcost)
                            v = int(input('''
                            1) Cash On Delivery
                            2) Credit Card
                            Select one of the options: '''))
                            paymentmethod = ""
                            if v == 1:
                                paymentmethod = "Cash On Delivery"
                                print("YOUR ORDER WILL BE DELIVERED AT", address, "ON", etar)
                                print(
                                    '''Our Delivery Boy will collect the cash remember not to give any tip since service tax is also included''')

                                break
                            if v == 2:
                                while True:
                                    paymentmethod = "Credit Card"
                                    credcard = input("Please enter your 15/16 Digit Credit Card Number: ")
                                    pin = int(input("Enter CVV(Card Verification Value): "))
                                    if credcarddic[credcard] != pin:
                                        print("Invalid Card Number Or CVV, try again")
                                    else:
                                        print("CVV Confirmed!!!!")
                                        print("\nTransaction Successful!!!!")
                                        print("YOUR ORDER WILL BE DELIVERED AT", address, "AT AROUND", etar)
                                        break
                                break
                    customer(username, address, phonen0, order, paymentmethod,date1)

                mainmenureturn = input("\n DO YOU WISH TO RETURN TO THE HOME PAGE? (Y/N)? :   ")
                if mainmenureturn == "N":
                    print("\n LOGGING YOU OUT!!!!")
                    print("\n THANK YOU FROM ORDERING FROM THE KINGS RESTAURANT ")
                    print("\n HOPE TO SEE YOU AGAIN!! ")
                    break
                break
        if mainmenureturn == "N":
            break

        elif usech == 2:
            print("KEEP IN MIND: RESERVATIONS ARE TO BE MADE ONE DAY IN ADVANCE")
            A = input("\nENTER THE NAME UNDER WHICH THE BOOKING HAS TO BE DONE: ")
            while True:
                day = input("\nENTER THE DAY OF YOUR ARRIVAL(YYYY-MM-DD): ")
                f = "%Y-%m-%d"
                a = datetime.strptime(day, f)
                r = datetime.now()
                if a<r:
                    print("\nINVALID DATE.PLEASE TRY AGAIN")
                else:
                    break
            while True:
                phoneno = int(input("\nENTER YOUR PHONE NUMBER: "))
                if len(str(phoneno))!=10:
                    print('\nINVALID PHONE NUMBER, TRY AGAIN')
                else:
                    break
            ppl = int(input("\nTOTAL NUMBER OF PEOPLE?: "))
            acch = input("\nAC OR NON AC?: ")
            if acch == "AC":
                for lop in range(ppl):
                    acrand = random.randint(1, 20)
                    while True:
                        if acrand in acseats:
                            acseats.remove(acrand)
                            acseatsres.append(acrand)
                            break
            if acch == "NON AC":
                for pol in range(ppl):
                    nonacrand = random.randint(1, 25)
                    while True:
                        if nonacrand in nonacseats:
                            nonacseats.remove(nonacrand)
                            nonacseatsres.append(nonacrand)
                            break
            timech = input("\nARRIVAL AT WHAT TIME IN THE RESTAURANT?(24 HRS FORMAT)?:")
            f1 = "%H:%M"
            lnlk = datetime.strptime(timech, f1)
            timech = lnlk.strftime("%H:%M")
            print("\nYOUR RECIEPT")
            print("\nKINGS FASTFOOD RESTAURANT")
            print("\nRESERVATION DETAILS:")
            print("\nNAME UNDER TABLES RESERVED:", A)
            print("\nPHONE NO.:", phoneno)
            print("\nNO. OF SEATS RESERVED:", ppl)
            print("\nTYPE OF SEATS:", acch)
            print("\nDAY OF ARRIVAL:", day)
            print("\nTIME OF ARRIVAL:", timech)
            seatnos = ""
            if acch == "AC":
                print("\nSEAT NUMBERS:", acseatsres)
                for ik in range(len(acseatsres)):
                    seatnos = seatnos + str(acseatsres[ik]) + ","
            else:
                print("\nSEAT NUMBERS:", nonacseatsres)
                for lk in range(len(nonacseatsres)):
                    seatnos = seatnos + str(nonacseatsres[lk]) + ","
            seatnos = seatnos[0:len(seatnos) - 1]
            print("\nTHANK YOU FOR RESERVING SEATS AT THE KING RESTAURANT HOPE YOU WILL HAVE A FINE TIME WITH US! ")
            reservation(A, phoneno, ppl, acch, seatnos, day, timech)
            break
