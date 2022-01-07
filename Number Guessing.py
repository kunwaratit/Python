
while True:
    import random
    comp_num=random.randint(1,10)
    user_num=int(input('enter your guess:'))
    print('Your guess:',user_num)
    print('Computer Guess:',comp_num)
    if user_num<=10:    
        if comp_num==user_num:
            print('You won')
        else :
            print('you lose')
    else:
        print('Out of Range')