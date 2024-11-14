#        Project:-Banking-System
print("====================================")

customernames=['Sai','Rahul','Ram','balaji','kohli']
customerpins=['523001','523001','523001','523001','523002']
customerbalance=[10000,20000,30000,40000,15000]
deposit=0
withdrawal=0
balance=0
customer_1=1
customer_2=5
i=0

while True:
    print("--------WELCOME TO IDFC BANK--------")
    print("************************************")
    print("=<<  1.Open a bank account       >>=")
    print("=<<  2.Withdrawal                >>=")
    print("=<<  3.Deposit                   >>=")
    print("=<<  4.Check customer & balance  >>=")
    print("=<<  5.Exit/Quit                 >>=")
    print("************************************")
    open=input("enter the number you want to choose:")
    if open=="1":
        print("customer is selected the option 1")
        a=eval(input("Enter no.of accounts you want to create:"))
        i=i+a
        if i>5:
            print("account exceed limit")
            i=i-a
        else:
            while customer_1<=i:
                name=input("Enter Full Name:")
                customernames.append(name)
                pin=str(input("Enter Pin Number:"))
                customerpins.append(pin)
                balance=0
                Deposit=eval(input("Enter Deposit Amount:"))
                balance=balance+Deposit
                customerbalance.append(balance)
                print("name=",end=" ")
                print(customernames[customer_2])
                print("pin=",end=" ")
                print(customerpins[customer_2])
                print("balance=",end=" ")
                print(customerbalance[customer_2],end="")
                print("-/Rs")
                customer_1=customer_1+1
                customer_2=customer_2+1
                print("Your Name is added to the customer system")
                print("Your pin is added to the customer system")
                print("Your balance is added to the customer system")
                print("Your new account is created successfully")
                print("\n")
                print("your name is available in the  customers list:")
                print(customernames)
                print("\n")
                print("Note!-Do not forgot name and pin")
                print("======================================")
        mainmenu=input("press key to enter to next operation or exit:")
    elif open=='2':
        print("customer  is selected the option 2")
        j=0
        while j<1:
            k=-1
            name=input("Enter name: ")
            pin=input("Enter pin:")
            while k < len(customernames) -1:
                k=k+1
                if name==customernames[k]:
                    if pin==customerpins[k]:
                        j=j+1
                        print("Your  current balance:",end="")
                        print(customerbalance[k],end="")
                        print("-/Rs\n")
                        balance=customerbalance[k]
                        withdraw=int(input("enter amount to be withdrawal:"))
                        if withdraw > balance:
                            print("there is insufficient money in your account.deposit money in  account")
                            deposited=int(input("Enter deposit ammount:"))
                            balance=balance+deposited
                            print("Your current balance:",end=" ")
                            print(balance,end="")
                            print("-Rs/n")
                            balance=balance-withdraw
                            print("--Withdrawal Successful--")
                            customerbalance[k]=balance
                            print("Your current balance:",end=" ")
                            print(balance,end="")
                            print("-Rs\n")
                        else:
                            balance=balance-withdraw
                            print("Withdrawal Successful")
                            customerbalance[k]=balance
                            print("Your current balance:",end=" ")
                            print(balance,end="")
                            print("-/Rs\n")
            if j < 1:
                print("name and pin does not match \n")
        mainmenu=input("press key to next operation or exit:")
    elif open=='3':
        print("customer is  selected the option 3")
        n=0
        while n<1:
            k=-1
            name=input("Enter name:")
            pin=input("Enter pin:")
            while k < len(customernames) -1:
                k=k+1
                if name==customernames[k]:
                   if pin==customerpins[k]:
                       n=n+1
                       print("Your balance:",end=" ")
                       print(customerbalance[k],end="")
                       print("-/Rs")
                       balance=(customerbalance[k])
                       depositamount=eval(input("Enter Deposited Amount:"))
                       balance=balance + depositamount
                       customerbalance[k]=balance
                       print("\n")
                       print("---Deposited Successfully---")
                       print("Your balance :",balance,end="")
                       print("-/Rs\n\n")
            if n<1:
                print("name and pin does not match!")
                break
        mainmenu=input("press any key to next operation or exit:")
    elif open=='4':
        print("customer is  selected the option 4")
        k=0
        print("customers name and balance is mentioned below")
        print("\n")
        while k<= len(customernames)-1:
            print("->.Customer=",customernames[k])
            print("->.balance=",customerbalance[k],end="")
            print("-/Rs")
            print("\n")
            k=k+1
        mainmenu=input("press any key to next operation or exit:")
    elif open=='5':
        print("Customer is selected the option 5")
        print("Thanks for using our banking system")
        print("Come again")
        print("Bye Bye")
        break
    else:
        print("Selected Invalid Option")
        print("Try again!")
        mainmenu=input("press any key to go mainmenu and perform operation or exit:")
        
        
        
        
                       
                    
            
    
                
                            
                            
                        
                        
                
            
    
                
                
        
