# List is a collection that can be used to store a list of values 
# (like these integers that you want). So let’s use it:

# List has a concept called index. The first element gets the index 0 (zero). 
# The second gets 1, and so on. You get the idea.

my_integers = [5, 7, 1, 3, 4]
print(my_integers[0]) 
print(my_integers[1]) 
print(my_integers[4]) 

relatives_names = ["Toshiaki","Juliana","Yuji","Bruno","Kaio"]
print(relatives_names[4])

#The most common method to add a new value to a List is append. Let’s see how it works:
bookshelf = []
bookshelf.append("The Effective Engineer")
bookshelf.append("The 4 Hour Work Week")
print(bookshelf[0]) # The Effective Engineer
print(bookshelf[1]) # The 4 Hour Work Week