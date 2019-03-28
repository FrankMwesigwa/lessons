'''Control Flow: conditional statements
“If” uses an expression to evaluate whether a statement is True or False. 
If it is True, it executes what is inside the “if” statement. For example:'''

if True:
    print("Hello Python If")

if 2 > 1:
    print("2 is greater than 1")

# The “else” statement will be executed if the “if” expression is false.
if 1 > 2:
      print("1 is greater than 2")
else:
  print("1 is not greater than 2")

# You can also use an “elif” statement:
if 1 > 2:
      print("1 is greater than 2")
elif 2 > 1:
  print("1 is not greater than 2")
else:
  print("1 is equal to 2")