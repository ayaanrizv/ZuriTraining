#!/usr/bin/env python
# coding: utf-8

# In[24]:


class Budget:
    def __init__(self,name,bal):
        self.name = name
        self.bal = bal
    def deposit(self,deposit):
        self.bal += deposit
        return ("Amount deposited successfully")
    def withdraw(self,wthdraw):
        if wthdraw <= self.bal:
            self.bal -= wthdraw
            return ("Here is your money: ${}".format(wthdraw))
        else:
            return ("Insufficient Balance")
    def balance(self):
        return ("Your balance is: ${}".format(self.bal))
    def transfer_from(self,amount):
        if amount <= self.bal:
            self.bal -= amount
            return amount
        else:
            print("Insufficient Balance")
            return 0
    def transfer_to(self,amount):
        self.bal += amount
        return ("Amount transferred successfully!")


# In[25]:


#instantiation
Food = Budget("Food",300)
Clothing = Budget("Clothing",200)
Entertainment = Budget("Entertainment",500)


# In[26]:


#checking balance
print(Food.balance())
print(Clothing.balance())
print(Entertainment.balance())


# In[27]:


#depositing
print(Food.deposit(200))
print(Food.balance())


# In[28]:


#withdrawing
print(Clothing.withdraw(75))
print(Clothing.balance())


# In[29]:


#transferring from food to clothing
amount_to_transfer = Food.transfer_from(100)
amount_to_transfer


# In[30]:


print(Food.balance())


# In[31]:


print(Clothing.transfer_to(amount_to_transfer))


# In[32]:


print(Clothing.balance())


# In[ ]:




