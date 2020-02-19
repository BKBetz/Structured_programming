from create_func import create_feedback


def simple_strategy(lst):
    code = input('Enter a code: ')
    if not code.isdigit() or len(code) != 4:
        print('Enter a 4 number code with numbers between one and six')
    else:
        if '7' in code or '8' in code or '9' in code or '0' in code:
            print("Don't use 0, 7, 8 of 9")
        else:
            attempts = 0
            lives = 10
            while lives > 0:
                guess = lst[0]
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