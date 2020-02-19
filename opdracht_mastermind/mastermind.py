import random
from create_func import create_all_answers, create_code
from simple_strat import simple_strategy
from worst_strat import worst_case
from self_made import self_made


def game_menu():
    print("""
Welcome to mastermind
Guess the four number code
Each number in the code is between 1 and 6
B = right number in the right spot
W = right number but in the wrong spot
X = number not in the code

Gamemodes:
1. cpu gives a code player guesses
2. player gives code cpu guesses (algorithm 1)
3. player gives code cpu guesses (algorithm 2)
4. player gives code cpu guesses (self made algorithm 3)
    """)

    game = input('Enter your choice: ')
    if game.isdigit():
        if game == '1':
            game_1()
        elif game == '2':
            game_2()
        elif game == '3':
            game_3()
        elif game == '4':
            game_4()
        else:
            print('choose 1,2,3 or 4')
    else:
        print('choose 1,2,3 or 4')


def game_1():
    lives = 10
    code = create_code()

    while lives > 0:
        guess = input("Guess the code: ")
        if not guess.isdigit():
            print('Enter a code with numbers between one and six')
        else:
            if len(guess) != 4:
                print('Enter a four digit code')
            else:
                if code == guess:
                    print('You guessed the code')
                    exit()

                else:
                    feedback = []
                    for i in range(0, len(guess)):
                        if guess[i] == code[i]:
                            feedback.append('B')
                        # since it's an person that tries to guess the code.. this makes it more fun :)
                        elif guess[i] in code:
                            feedback.append('W')

                        else:
                            feedback.append('X')
                    lives -= 1

                    # shuffle the code so that the player doesn't know which feedback is for which number
                    random.shuffle(feedback)
                    feedback = "-".join(feedback)
                    print(feedback)

    if lives == 0:
        print('GAME OVER...the code was: ', code)
        exit()


def game_2():
    all_answers = create_all_answers()
    simple_strategy(all_answers)


def game_3():
    all_answers = create_all_answers()
    worst_case(all_answers)


def game_4():
    all_answers = create_all_answers()
    self_made(all_answers)


"""
bronvermeldingen:
"""
