def roll():
    import random
    num = random.randint(1, 6)
    return num


while True:
    val = roll()
    a = input('Do you want to Roll a Dice\nY/y or N/n ')
    if a == 'Y' or a == 'y':
        print("you got:", val)

    elif a == 'N' or a == 'n':
        break
    else:
        print('choice wrong')
