blnc=float(input("Enter balance amount"))
while True:  
    choice=int(input("Enter choice:\n1. withdrawal\n2.deposite\n="))
    if choice==1:
        if blnc<=0:
            print("_insufficient_balance_")
            break
        else:
            withdr=float(input("ENTER WITHDRAWL AMOUNT:"))
            if withdr<=0:
                print("_WITHDRAWL_AMOUNT_CANNOT_BE_ZERO_")
            else:
                if withdr>blnc:
                    print("_AMOUNT_EXCEEDING_BALANCE_")
                else:
                    blnc=blnc-withdr
                    print("_WITHDRAWL_DONE_SUCCESSFULLY_")
                    print("NEW BALANCE=",blnc)
                    if blnc==0:
                        print("ACCOUNT IS EMPTY.")
                        break
    elif choice==2:
        dep=float(input("ENTER AMOUNT TO DEPOSITE: "))
        if dep>0:
            blnc=blnc+dep
            print("new balance:",blnc)
        else:
            print("enter valid amount.")
    else:
        print("invalid choice")
