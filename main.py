import random


def guess(x):
    random_number = random.randint(1, x)
    answer = 0
    chance = 0
    y = 5
    while answer != random_number:
        answer = input(f'you have {y} chance.\n enter the number from 1 to {x} :')
        chance += 1
        y -= 1
        if answer.isdigit():
            answer = float(answer)
            if answer > random_number:
                print(' your number is high')
            elif answer < random_number:
                print(' your number is law')
            else:
                print(f'Congratulations you won, your number is {answer}')
        else:
            print("I can only read numbers, it is'not number.")
            break
        if chance == 5:
            print('Unfortunately you have exhausted your number of attempts, try again.')
            break


guess(20)






