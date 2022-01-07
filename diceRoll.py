def roll():
    import random
    num=random.randint(1,6)
    print(num)
while True:
    a=input('Do you want to Roll a Dice\nY/y or N/n')
    if a=='Y' or a=='y':
        print("you got")
        roll()
    elif a=='N' or a=='n':
        break
    else:
        print('choice wrong')