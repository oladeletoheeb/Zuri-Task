import datetime
Today= datetime.datetime.now()
print(Today)
name = input ("What is your name? \n")
allowedUsers = ['Toheeb', 'John', 'Ade']
allowedPassword = ['passwordToheeb', 'passwordJohn', 'passwordAde']

if (name in allowedUsers):
    password = input ("Your Password? \n")
    userId = allowedUsers.index(name)
    if (password == allowedPassword[userId]):
        
        print ('Welcome %s' % name)
        print ('These are the available options:')
        print ('1. Withdrawal')
        print ('2. Cash Deposit')
        print ('3. Complaint')

        selected_option = int(input("please slect an option:"))

        if (selected_option == 1):
            withdraw = int(input("How much would you like to withdraw"))
            print ("Take your cash")
        
        elif (selected_option == 2):
            deposit = int(input("How much would you like to deposit"))
            print (deposit)
        elif (selected_option == 3):
            issue = input("What issue would you like to report?:")
            print ("Thank you for contacting us")
        
    else:
        print ('Password Incorrect, please try again')

else:
    print ('Name not found, please try again')