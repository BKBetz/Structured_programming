import random


def create_code():
    code = ''
    for i in range(0, 4):
        number = random.randint(1, 6)
        code_num = str(number)
        code += code_num

    return code


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
            print(game_4())


def create_all_answers():
    all_answers = []
    for i in range(1111, 6667):
        answer = str(i)
        if '7' in answer or '8' in answer or '9' in answer or '0' in answer:
            continue
        else:
            all_answers.append(answer)

    return all_answers


def create_feedback(code, guess):
    feedback = [0, 0]
    lst = []

    for i in range(0, 4):
        if code[i] == guess[i]:
            feedback[0] += 1
            lst.append(guess[i])

    for i in range(0, 4):
        if guess[i] in code:
            num = guess[i]
            num_count = guess.count(num)
            num2_count = code.count(num)
            if lst.count(guess[i]) < num_count and lst.count(guess[i]) < num2_count:
                lst.append(num)
                feedback[1] += 1

    feedback = [str(feedback[0]), str(feedback[1])]
    return feedback


def calc_worst_case(lst):
    # nog niet af
    cases = ['0,0', '0,1', '0,2', '0,3', '0,4', '1,0', '1,1', '1,2', '1,3', '2,0', '2,1', '2,2', '3,0', '4,0']

    worst_case = len(lst)
    guess = ''
    for i in lst:
        if len(lst) > 1:
            cases_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for x in lst:
                feedback = create_feedback(i, x)
                case_feedback = ",".join(feedback)
                for j in range(0, len(cases_count)):
                    if case_feedback == cases[j]:
                        cases_count[j] += 1

            if max(cases_count) < worst_case:
                guess = i
        else:
            guess = i

    return guess


def simple_strategy(lst):
    # af
    code = input('Enter a code: ')
    if not code.isdigit():
        print('Enter a code with numbers between one and six')
    else:
        attempts = 0
        lives = 10
        while lives > 0:
            guess = lst[0]
            feedback = create_feedback(code, guess)
            print(guess)
            print(feedback)
            for i in reversed(lst):
                item_feedback = create_feedback(guess, i)
                if feedback != item_feedback:
                    lst.remove(i)
            print(lst)
            lives -= 1
            attempts += 1
            if guess == code:
                print('De computer heeft de code geraden in ', attempts, ' pogingen')
                break
            elif lives == 0:
                print('GAME OVER')


def worst_case(lst):
    # nog niet af
    code = input('Enter a code: ')
    if not code.isdigit():
        print('Enter a code with numbers between one and six')
    else:
        attempts = 0
        lives = 10
        while lives > 0:
            if attempts == 0:
                guess = '1122'
            else:
                guess = calc_worst_case(lst)

            feedback = create_feedback(code, guess)

            print(guess)
            print(feedback)
            for i in reversed(lst):
                item_feedback = create_feedback(guess, i)
                if feedback != item_feedback:
                    lst.remove(i)

            print(lst)
            lives -= 1
            attempts += 1
            if guess == code:
                print('De computer heeft de code geraden in ', attempts, ' pogingen')
                break
            elif lives == 0:
                print('GAME OVER')


def best_case(lst):
    # nog niet af
    code = input('Enter a code: ')
    if not code.isdigit():
        print('Enter a code with numbers between one and six')
    else:
        attempts = 0
        lives = 10
        while lives > 0:
            if attempts == 0:
                guess = '1122'
            else:
                guess = calc_worst_case(code, lst)

            print(guess)
            feedback = create_feedback(code, guess)
            print(feedback)
            for i in reversed(lst):
                item_feedback = create_feedback(guess, i)
                if item_feedback != feedback:
                    lst.remove(i)

            print(len(lst))
            print(lst)
            attempts += 1
            lives -= 1

            if lives == 0:
                print('De computer heeft de code niet geraden')
                break

            elif code == guess:
                print('De computer heeft de code geraden in ', attempts, ' pogingen')
                break
def game_1():
    # af

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

                        elif guess[i] in code:
                            feedback.append('W')

                        else:
                            feedback.append('X')
                    lives -= 1

                    random.shuffle(feedback)
                    feedback = "-".join(feedback)
                    print(feedback)

    if lives == 0:
        print('GAME OVER')
        exit()


def game_2():
    all_answers = create_all_answers()
    simple_strategy(all_answers)


def game_3():
    all_answers = create_all_answers()
    worst_case(all_answers)


def game_4():
    all_answers = create_all_answers()
    best_case(all_answers)


game_menu()
"""
bronvermeldingen:
"""
