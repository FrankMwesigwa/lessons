'''write a function to withdraw and show the new balance. the system should validate the amount to be withdrawal'''

def withdraw(): 
        balance = 50000
        amount = float(input("Enter amount to be Withdrawed: ")) 
        if balance >= amount: 
            balance -= amount 
            print("\n You Withdrawed:", amount) 
            print("\n Your Current Balance is:", balance) 
        else: 
            print("\n Sorry !!!! --- Insufficient balance to withdraw --- ") 

withdraw()