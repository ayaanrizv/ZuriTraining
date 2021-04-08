#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
database = {}
def generateAccountNumber():
    print("******************Generating account number!****************** ")
    return random.randrange(1111111111,9999999999)
def withdrawal(accountNumber):
    print("******************Making a withdrawal:****************** ")
    isSelected = False
    while isSelected == False:
        moneyToWithdraw = int(input("Please enter the amount you would like to withdraw: "))
        if moneyToWithdraw> 0:
            for account, userDetails in database.items():
                if account == accountNumber:
                    isSelected = True
                    if moneyToWithdraw <= userDetails[4]:
                        print("Here is your amount $ {}".format(moneyToWithdraw))
                        break
                    else:
                        print("Insufficient Balance")
                        break
        else:
            print("Please enter a valid amount")
def deposit(accountNumber):
    print("******************Making a deposit!******************")
    isSelected = False
    while isSelected == False:
        moneyToDeposit = int(input("Please enter the amount you would like to deposit: "))
        if moneyToDeposit > 0:
            for account, userDetails in database.items():
                if account == accountNumber:
                    isSelected = True
                    userDetails[4] += moneyToDeposit
                    print("Amount deposited successfully!")
                    break
        else:
            print("Please enter a valid amount")
def checkBalance(accountNumber):
    for account, userDetails in database.items():
            if account == accountNumber:
                print("Your current Balance is $ {}".format(userDetails[4]))
def logout():
    login()
def bankOperations(user,accountNumber):
    print("******************Welcome {} {}******************".format(user[1],user[2]))
    isOperating = False
    while isOperating == False:
        option = int(input("What would you like to do? (1) Deposit (2) Withdrawal (3) Check Balance (4) Logout (5) Exit "))
        if option == 1:
            isOperating = True
            deposit(accountNumber)
        elif option == 2:
            isOperating = True
            withdrawal(accountNumber)
        elif option == 3:
            isOperating = True
            checkBalance(accountNumber)
        elif option == 4:
            isOperating = True
            logout()
        elif option == 5:
            isOperating = True
            print("Please visit us again!")
            exit()
        else:
            print("Incorrect Option! Please try again!")
    
def login():
    print("******************Welcome! Please enter your details to login!******************")
    isLoginSuccessful = False
    while isLoginSuccessful == False:
        accountNumberFromUser = int(input("Enter your account number: "))
        passwordFromUser = int(input("Enter your password"))
        for accountNumber,userDetails in database.items():
            if accountNumber == accountNumberFromUser:
                if userDetails[3] == passwordFromUser:
                    isLoginSuccessful = True
                    print("You have successfully logged in!")
                    bankOperations(userDetails,accountNumber)
                    break
        else:
            print("Your credentials do not exist!")
            option = int(input("Would you like to register? (1)Yes (2) No"))
            if option == 1:
                register()
                break
            else:
                pass        
def register():
    print("******************Register Here for a zero balance account!******************")
    email = input("What is your email address? ")
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    password = int(input("Create your password: "))
    accountNumber = generateAccountNumber()
    balance = 0
    database[accountNumber] = [email,first_name,last_name,password,balance]
    print("Your account has been created with account number - {}".format(accountNumber))
    print("Please note it down carefully!")
    option = int(input("Would you like to deposit money in your new account? (1) Yes (2) No "))
    if option == 1:
        deposit(accountNumber)
    else:
        pass
    login()
def main():
    isValidOptionSelected = False
    print("******************Welcome to Bank of Python!******************")
    while isValidOptionSelected == False:
        haveAccount = int(input("Do you have an account with us: 1(yes) 2(No) "))
        if haveAccount == 1:
            isValidOptionSelected = True
            login()
        elif haveAccount == 2:
            isValidOptionSelected = True
            register()
        else:
            print("Please select a valid option!")
main()


# In[ ]:




