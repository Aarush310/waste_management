import mysql.connector
import random
con=mysql.connector.connect (host="localhost",user="root",password="1234",database="waste")
cur=con.cursor()
print("Waste Management")
print("1)I want to register")
print("2)I do not want to register")
while True:
        try:
            reg_choice = int(input("Enter your choice:"))
        except ValueError:
            print("please enter a valid number ")
            continue

        if reg_choice<1 or reg_choice>2  :
            print("please enter a valid number")
        else:
            break
if reg_choice==1:
    print("1:Business register")
    print("2:Gated Community register")
    print("3:Individual register")
    reg = int(input("Enter your choice:"))
    while True:
        try:
            reg = int(input("Enter your choice:"))
        except ValueError:
            print("please enter a valid number ")
            continue

        if reg<1 or reg>3  :
            print("please enter a valid number")
        else:
            break
    if reg==1:
        while True:
            try:
                comp = input("Enter Company Username")
            except ValueError:
                print("please enter a valid USERNAME ")
                continue

            if len(comp)<1 or len(comp)>30  :
                print("please enter a valid USERNAME")
            else:
                break
        while True:
            try:
                passwd = input("Create a password")
            except ValueError:
                print("please enter a valid password ")
                continue

            if len(passwd)<1 or len(passwd)>30  :
                print("please enter a valid password")
            else:
                break
        sql = "INSERT INTO busdetails VALUES (%s, %s)"
        val = (comp, passwd)
        cur.execute(sql,val)
        con.commit()
    elif reg==2:
        while True:
            try:
                com = input("Enter Community Username")
            except ValueError:
                print("please enter a valid USERNAME ")
                continue

            if len(com)<1 or len(com)>30  :
                print("please enter a valid USERNAME")
            else:
                break
        while True:
            try:
                passwd = input("Create a password")
            except ValueError:
                print("please enter a valid password ")
                continue

            if len(passwd)<1 or len(passwd)>30  :
                print("please enter a valid password")
            else:
                break
        sql = "INSERT INTO comdetails VALUES (%s, %s)"
        val = (com, passwd)
        cur.execute(sql,val)
        con.commit()
    elif reg==3:
        while True:
            try:
                user = input("Enter Username")
            except ValueError:
                print("please enter a valid USERNAME ")
                continue

            if len(user)<1 or len(user)>30  :
                print("please enter a valid USERNAME")
            else:
                break
        while True:
            try:
                passwd = input("Create a password")
            except ValueError:
                print("please enter a valid password ")
                continue

            if len(passwd)<1 or len(passwd)>30  :
                print("please enter a valid password")
            else:
                break
        sql = "INSERT INTO userdetails VALUES (%s, %s)"
        val = (user, passwd)
        cur.execute(sql,val)
        con.commit()
elif reg_choice==2:
    print("Proceed to login")
print("Choose from the list below to avail our services")
print("1:Business Services")
print("2:Gated Community Services")
print("3:Individual Services")
while True:
        try:
            choice = int(input("Enter your choice:"))
        except ValueError:
            print("please enter a valid number ")
            continue

        if choice<1 or choice>3  :
            print("please enter a valid number")
        else:
            break
if choice ==1:
    print("Login")
    user = input("Enter Company Username:")
    passwd = input("Enter password")
    a = (user,passwd)
    cur.execute("SELECT * FROM busdetails;")
    result = cur.fetchall()
    if a in result:
        name = input("Enter Company name:")
        print("1: waste pickup service")
        print("2: cleaners service")
        print("3: electronic waste purchase")
        while True:
            try:
                choice2 = int(input("choose one of the above service:  "))
            except ValueError:
                print("please enter a valid number ")
                continue

            if choice2<1 or choice2>3  :
                print("please enter a valid number")
            else:
                break
        if choice2 == 1:
            print("1: biodegradable waste")
            print("2: non biodegradable waste")
            print("3: mixed waste")
            print("4: chemical waste")
            while True:
                try:
                    choice2_input = int(input("enter choice of waste to be picked:  "))
                except ValueError:
                    print("please enter a valid number ")
                    continue

                if choice2_input<1 or choice2_input>4  :
                    print("please enter a valid number")
                else:
                    break
            no_days = int(input("for how many days do you need the subscription service:  "))
            if choice2_input == 1:
                bb = "Biodegradable"
                qty = int(input ("input the quantity of waste to be collected(in 10KG):  "))
                price = no_days*qty*80  #80 ruppes rate for biodegradable waste
                print(name,"the price for your subscription is: ",price,"₹ for ",no_days," days")
                print("we will get back to your HR on mail")
                cle = "INSERT INTO buswaste VALUES('%s',%s,'%s',%s,%s)"%(name,no_days,bb,qty,price)
                cur.execute(cle)
                con.commit()
            elif choice2_input == 2:
                bb = "Non Biodegradable"
                qty = int(input ("input the quantity of waste to be collected(in 10KG):  "))
                price = no_days*qty*120  #120 ruppes rate for Non-biodegradable waste
                print(name,"the price for your subscription is: ",price,"₹ for ",no_days," days")
                print("we will get back to your HR on mail")
                cle = "INSERT INTO buswaste VALUES('%s',%s,'%s',%s,%s)"%(name,no_days,bb,qty,price)
                cur.execute(cle)
                con.commit()
            elif choice2_input == 3:
                bb = "Mixed"
                qty = int(input ("input the quantity of waste to be collected(in 10KG):  "))
                price = no_days*qty*100  #100 ruppes rate for mixed type of waste
                print(name,"the price for your subscription is: ",price,"₹ for ",no_days," days")
                print("we will get back to your HR on mail")
                cle = "INSERT INTO buswaste VALUES('%s',%s,'%s',%s,%s)"%(name,no_days,bb,qty,price)
                cur.execute(cle)
                con.commit()
            elif choice2_input == 4:
                bb = "Chemical"
                qty = int(input ("input the quantity of waste to be collected(in 10KG):  "))
                price = no_days*qty*150  #150 ruppes rate for chemical waste
                print(name,"the price for your subscription is: ",price,"₹ for ",no_days," days")
                print("we will get back to your HR on mail")
                cle = "INSERT INTO buswaste VALUES('%s',%s,'%s',%s,%s)"%(name,no_days,bb,qty,price)
                cur.execute(cle)
                con.commit()

        elif choice2 == 2:
            print("you have chosen cleaners service ")
            while True:
                try:
                    no_cleaners = int(input("how many cleaners do you require "))
                except ValueError:
                    print("please enter a valid number ")
                    continue

                if no_cleaners<1 or no_cleaners>20  :
                    print("Out of Range")
                else:
                    break
            no_days = int(input("for how many days do you need the cleaners service:  "))
            price = no_cleaners*no_days*600  #cleaner rate 600 ruppe per day
            print(name,"cost of hiring ",no_cleaners,"cleaners is ",price,"₹")
            print("we will get back to your HR on mail")
            cle = "INSERT INTO cleaner VALUES('%s',%s,%s,%s)"%(name,no_cleaners,no_days,price)
            cur.execute(cle)
            con.commit()

        elif choice2 == 3: 
            while True:
                try:
                    qty_waste = int(input("how much electronic waste do you want to purchase (in quintal):  ")) #1 quintal = 100kg
                except ValueError:
                    print("please enter a valid number ")
                    continue

                if qty_waste<1 or qty_waste>20  :
                    print("Out of Range")
                else:
                    break
            qty_price = qty_waste*50000 
            print(name,"the cost to purchase",qty_waste,"quintal of electronic waste is: ",qty_price," ₹")
            print("we will get back to your HR on mail")
            ewa = "INSERT INTO ewaste VALUES('%s',%s,%s)"%(name,qty_waste,qty_price)
            cur.execute(ewa)
            con.commit()
    else:
        print("No account found")
elif choice ==2:
    print("Login")
    user = input("Enter Community Username:")
    passwd = input("Enter password")
    a = (user,passwd)
    cur.execute("SELECT * FROM comdetails;")
    result = cur.fetchall()
    if a in result:
            print("1) Bulk Trash Pickup (heavy items like sofas)")
            print("2) Everyday waste(only for residental complexes )")
            print("3) Composters")
            while True:
                try:
                    type_waste=int(input("Enter your choice  "))
                except ValueError:
                    print("please enter a valid number ")
                    continue

                if type_waste<1 or type_waste>3  :
                    print("please enter a valid choice")
                else:
                    break
            if type_waste==1:
                name=input("Enter name of apartment:  ")
                days = int(input("Enter number of days the service is required:"))
                trucks=int(input("No of trucks needed to carry waste:  "))
                print("Choose the type of waste for pickup: ")
                print("1:Biodegradable waste(eg:wooden..etc)")
                print("2:Non biodegradable waste(eg:polyster/steel..)")
                print("3:Both types of waste")
                while True:
                    try:
                        waste =int(input("Enter the type of waste to be picked up:  "))
                    except ValueError:
                        print("please enter a valid number ")
                        continue

                    if waste<1 or waste>3  :
                        print("please enter a valid choice")
                    else:
                        break
                if waste==1:
                    a=trucks*1000*days
                    a1 = "Biodegradable"
                    print("Cost for pickup and disposal is ",a,"₹")
                    print("we will get back to your apartments manager in a while. ")
                    bk = "INSERT INTO bulk_pick VALUES('%s',%s,%s,'%s',%s)"%(name,days,trucks,a1,a)
                    cur.execute(bk)
                    con.commit()
                elif waste==2:
                    a=trucks*2500*days
                    print("Cost for pickup and disposal is ",a,"₹")
                    a1 = "Non Biodegradable"
                    print("we will get back to your apartments manager in a while. ")
                    bk = "INSERT INTO bulk_pick VALUES('%s',%s,%s,'%s',%s)"%(name,days,trucks,a1,a)
                    cur.execute(bk)
                    con.commit()
                elif waste==3:
                    a=trucks*1500*days
                    print("Cost for pickup and disposal is ",a,"₹")
                    a1 = "Mixed"
                    print("we will get back to your apartments manager in a while. ")
                    bk = "INSERT INTO bulk_pick VALUES('%s',%s,%s,'%s',%s)"%(name,days,trucks,a1,a)
                    cur.execute(bk)
                    con.commit()
                else:
                    print(" Please enter a valid number ")
            elif type_waste==2:
                name=input("Enter name of apartment:  ")
                days=int(input("How many days do you want to use this serivce per month:  "))
                amt=int(input("Enter amount of kgs(x10) of waste:  "))
                print("1:Biodegradable waste")
                print("2:Non biodegradable waste")
                print("3:Both types of waste")
                while True:
                    try:
                        waste1 =int(input("Enter the type of waste to be picked up:  "))
                    except ValueError:
                        print("please enter a valid number ")
                        continue

                    if waste1<1 or waste1>3  :
                        print("please enter a valid choice")
                    else:
                        break
                if waste1==1:
                    d=60*amt*days
                    d1 = "Biodegradable"
                    print("Cost for pickup and disposal is",d,"₹")
                    print("we will get back to your apartments manager in a while. ")
                    ev = "INSERT INTO everyday_waste VALUES('%s',%s,%s,'%s',%s)"%(name,days,amt,d1,d)
                    cur.execute(ev)
                    con.commit()
                elif waste1==2:
                    d=100*amt*days
                    d1 = "Non biodegradable"
                    print("Cost for pickup and disposal is",d,"₹")
                    print("we will get back to your apartments manager in a while. ")
                    ev = "INSERT INTO everyday_waste VALUES('%s',%s,%s,'%s',%s)"%(name,days,amt,d1,d)
                    cur.execute(ev)
                    con.commit()
                elif waste1==3:
                    d=80*amt*days
                    d1 = "mixed"
                    print("Cost for pickup and disposal is",d,"₹")
                    print("we will get back to your apartments manager in a while. ")
                    ev = "INSERT INTO everyday_waste VALUES('%s',%s,%s,'%s',%s)"%(name,days,amt,d1,d)
                    cur.execute(ev)
                    con.commit()
                else:
                    print(" Please enter a valid number ")
            elif type_waste==3:
                name=input("Enter name of apartment:  ")
                print("Different types of composters are below please select\
                particular choice to order")
                print("1)Price of small scale composter(1kg of fertiliser/10kg of waste)5000rs(inclusive gst)")
                print("2)Price of big scale composter(80kg of fertiliser/100kg of waste)20000rs(inclusive gst)")
                while True:
                    try:
                        choice=int(input("Enter choice:  "))
                    except ValueError:
                        print("please enter a valid number ")
                        continue

                    if choice<1 or choice>2  :
                        print("please enter a valid choice")
                    else:
                        break
                qty = int(input("Enter the Quantity:"))
                if choice == 1:
                    total = qty*5000
                    print("Small composter order placed ",total," ₹ (inclusive gst) to be paid")
                    print("we will get back to your apartments manager in a while. ")
                    comp = "SMALL"
                    compo = "INSERT INTO composter VALUES('%s','%s',%s,%s)"%(name,comp,qty,total)
                    cur.execute(compo)
                    con.commit()
       
                elif choice == 2:
                    total = qty*20000
                    print("Large composter order placed ",total,"₹ (inclusive gst)to be paid ")
                    print("we will get back to your apartments manager in a while. ")
                    comp = "BIG"
                    compo = "INSERT INTO composter VALUES('%s','%s',%s,%s)"%(name,comp,qty,total)
                    cur.execute(compo)
                    con.commit()
    else:
        print("No account found")
elif choice ==3:
    print("Login")
    user = input("Enter Username:")
    passwd = input("Enter password")
    a = (user,passwd)
    cur.execute("SELECT * FROM userdetails;")
    result = cur.fetchall()
    if a in result:
        name = input("enter your name: ")
        phone_no = int(input("Enter your phone number: "))
        p = str(phone_no)
        print("we are providing a residential waste pickup service and a recycled items shop")
        print("1) Residential Waste Pickup")
        print("2) Recycled items shop")      
        while True:
                    try:
                        option_select = int(input("choose from the above option: "))
                    except ValueError:
                        print("please enter a valid number ")
                        continue

                    if option_select<1 or option_select>2  :
                        print("please enter a valid choice")
                    else:
                        break
        if option_select == 1:
            print("choose the type of waste for pickup: ")
            print("1) Biodegradable waste")
            print("2) Non-Biodegradable waste")
            print("3) BOTH biodegradable and non-biodegradable waste pickup")
            while True:
                    try:
                        option_select_1 = int(input("enter the option no: "))
                    except ValueError:
                        print("please enter a valid number ")
                        continue

                    if option_select_1<1 or option_select_1>3  :
                        print("please enter a valid choice")
                    else:
                        break
            if option_select_1 == 1:
                no_days = int(input("for how many days do you need the subscription service:  "))
                qty = int(input ("input the quantity of waste to be collected(in KG):  "))
                price = no_days*qty*2  #2 ruppes rate for biodegradable waste
                print("Price Structure - ₹2 per KG")
                print(name,"the price for your subscription is: ",price,"₹ for ",no_days," days")
                print("we will get back to you on whatsapp ")
                st = "INSERT INTO us_waste VALUES('%s','%s',%s,%s,%s)"%(name,p,no_days,qty,price)
                cur.execute(st)
                con.commit()
            elif option_select_1 == 2:
                no_days = int(input("for how many days do you need the subscription service:  "))
                qty = int(input ("input the quantity of waste to be collected(in KG):  "))
                price = no_days*qty*4  #4 ruppes rate for Non-biodegradable waste
                print("Price Structure - ₹4 per KG")
                print(name,"the price for your subscription is: ",price,"₹ for ",no_days," days")
                print("we will get back to you on whatsapp ")
                st = "INSERT INTO us_waste VALUES('%s','%s',%s,%s,%s)"%(name,p,no_days,qty,price)
                cur.execute(st)
                con.commit()
            elif option_select_1 == 3:
                no_days = int(input("for how many days do you need the subscription service:  "))
                qty = int(input ("input the quantity of waste to be collected(in KG):  "))
                price = no_days*qty*3  #3 ruppes rate for BOTH type of waste
                print("Price Structure - ₹3 per KG")
                print(name,"the price for your subscription is: ",price,"₹ for ",no_days," days")
                print("we will get back to you on whatsapp ")
                st = "INSERT INTO us_waste VALUES('%s','%s',%s,%s,%s)"%(name,p,no_days,qty,price)
                cur.execute(st)
                con.commit()

        elif option_select == 2:
            print("here are the recycled products available in the shop to buy from: ")
            items = [("1) Recycled paper pencils", 5),("2) Recycled plastic water bottles", 7),("3) Recycled greeting cards", 5),("4) Recycled cotton t-shirts", 30),("5) Recycled aluminum cans", 10), ("6) Recycled glass bottles", 20)]
            for item in items:
                print(item[0], "₹" + str(item[1]))
            item_select = 1
            total = 0
            while item_select>0:
                while True:
                    try:
                        item_select = int(input("please select the item you want to buy from our shop:  "))
                    except ValueError:
                        print("please enter a valid number ")
                        continue

                    if item_select<0 or item_select>6  :
                        print("please enter a valid choice")
                    else:
                        break
                if item_select==0:
                    break
                item_qty = int(input("input the qty of item:  "))
                selected_item = items[item_select - 1] 
                item_price = selected_item[1] * item_qty
                total = total+item_price
                print("price for the selected item(s): ₹" + str(item_price))
                print("Enter 0 if finished ordering")
            print("Total price for the selected item(s): ₹" + str(total))
            gst_tax = 0.12
            item_price_with_tax = total + (total * gst_tax)
            print("Total price for the selected item(s) including GST: ₹" + str(item_price_with_tax))  #including gst 3
            print(random.randint(1,1000), " is your order ID")
            print("Msg us on 9036XXXXXX to proceed with payment ")
    else:
        print("No account found")