'''write a function to deposit money and print out the balance after deposit'''

def deposit(): 
        balance = 20000
        amount = float(input("Enter amount to be Deposited: ")) 
        balance += amount 
        print("\n Amount Deposited:", amount) 
        print("\n Current Balance After Deposit:", balance) 

deposit()