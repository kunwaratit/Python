
maxGuess = 5
guessCount = 0
chance = maxGuess
while guessCount < maxGuess:
    import random
    comp_num = random.randint(1, 10)
    guessCount = guessCount+1

    print(f'You have {chance} chances to guess:')
    user_num = int(input(f'{guessCount}. enter your guess:'))
    print(f'Your guess:', user_num)
    print('Computer Guess:', comp_num)

    if user_num <= 10:
        chance -= 1
        if comp_num == user_num:
            print('Congratulation! You Won The Game')
            break
        elif guessCount == maxGuess:
            print('Not Matched, You Lose The Game!')
        else:
            print('Not Matched')
    else:
        guessCount = guessCount-1
        print('Out of Range')
