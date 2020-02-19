from create_func import create_feedback


def calc_worst_case(lst):
    cases = {'0,0': 0, '0,1': 0, '0,2': 0, '0,3': 0, '0,4': 0, '1,0': 0, '1,1': 0, '1,2': 0, '1,3': 0, '2,0': 0, '2,1': 0, '2,2': 0, '3,0': 0, '4,0': 0}

    worst = len(lst)
    guess = ''
    for i in lst:
        # if the list only has one item..return that item
        if len(lst) > 1:
            for x in lst:
                # compare alle items to each other
                feedback = create_feedback(i, x)
                case_feedback = ",".join(feedback)
                for z in cases:
                    # if the feedback is the same as one from the cases dictionary..add one to that key
                    if case_feedback == z:
                        cases[z] += 1

            if max(cases.values()) < worst:
                # every time an item increases the max value..the guess is equal to that item
                guess = i
        else:
            guess = i

    return guess


def worst_case(lst):
    code = input('Enter a 4 digit code with numbers between one and six : ')
    if not code.isdigit() or len(code) != 4:
        print('Enter a 4 digit code with numbers between one and six')
    else:
        if '7' in code or '8' in code or '9' in code or '0' in code:
            print("Don't use 0, 7, 8 of 9")
        else:
            attempts = 0
            lives = 10
            while lives > 0:
                # first guess should always be 1122
                if attempts == 0:
                    guess = '1122'
                else:
                    guess = calc_worst_case(lst)

                feedback = create_feedback(code, guess)

                for i in reversed(lst):
                    item_feedback = create_feedback(guess, i)
                    if feedback != item_feedback:
                        lst.remove(i)

                lives -= 1
                attempts += 1
                if guess == code:
                    print('The computer guessed the code in ', attempts, ' attempts')
                    break
                elif lives == 0:
                    print('GAME OVER')
                    break
