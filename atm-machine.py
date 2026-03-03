blnc=5000
while True:  
    
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
