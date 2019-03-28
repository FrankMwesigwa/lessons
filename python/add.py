
while 1:
    print('Enter a number:')
    s = input()
    s = int(s) 
    print ("hello")
    if s in range(1, 7):
        if s == 1:
            print ('Go to ...1')
        elif s == 2:
            print ('Go to ...2')
        elif s == 3:
            print ('Go to ...3')
        else:
            print('party time')
    else:
        print('(:-')