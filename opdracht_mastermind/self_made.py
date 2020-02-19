import random
from create_func import create_feedback


def self_made(lst):
    # not the fastest...but it works ;)

    code = input('Enter a 4 digit code with numbers between one and six : ')
    if not code.isdigit() or len(code) != 4:
        print('Enter a 4 digit code with numbers between one and six')
    else:
        if '7' in code or '8' in code or '9' in code or '0' in code:
            print("Don't use 0, 7, 8 of 9")
        else:
            code_numbers = []
            lives = 20
            attempts = 0

            # make the first 6 attempts with each only consisting the same number...1111,2222,3333, etc
            for i in range(1, 7):
                guess = str(i) * 4
                attempts += 1
                lives -= 1

                if code == guess:
                    print('The computer guessed the code in ', attempts, ' attempts')
                    exit()
                else:
                    # if the guess is not the code, but the number is in the code... append to code numbers
                    if guess[0] in code:
                        code_numbers.append(guess[0])

            while lives > 0:
                # check if the list has four items... if not..it means the same digit appears more than once
                # for example 2213 or 4445
                if len(code_numbers) != 4 and attempts == 6:
                    difference = 4 - len(code_numbers)
                    # this is just to make the guess an 4 character long string
                    # since all the numbers in the list are in the code..it doesn't matter which one we multiply
                    guess = "".join(code_numbers) + (code[0] * difference)

                elif len(code_numbers) == 4 and attempts == 6:
                    guess = "".join(code_numbers)

                # after we made the first REAL attempt to guess the code.. we will just pick random possible answers
                # from the all possible answers list
                else:
                    guess = random.choice(lst)

                # from here on we implement the simple strategy
                feedback = create_feedback(code, guess)

                for i in lst:
                    item_feedback = create_feedback(guess, i)

                    if feedback != item_feedback:
                        lst.remove(i)

                attempts += 1
                lives -= 1

                if guess == code:
                    print('The computer guessed the code in ', attempts, ' attempts')
                    break
                elif lives == 0:
                    print('GAME OVER')
                    break
