import random


def create_code():
    code = ''
    for i in range(0, 4):
        number = random.randint(1, 6)
        code_num = str(number)
        code += code_num

    return code


def create_all_answers():
    all_answers = []
    for i in range(1111, 6667):
        answer = str(i)
        # ignores all possibilities with 0, 7, 8 or 9 in it
        if '7' in answer or '8' in answer or '9' in answer or '0' in answer:
            continue
        else:
            all_answers.append(answer)

    return all_answers


"""
    Deze functie is gemaakt in samenwerking met Storm Joannes
    Dit is omdat ik en Storm steeds op hetzelfde probleem kwamen
    We hebben beide een andere versie, maar er zitten nog wel gelijke delen in
"""


def create_feedback(code, guess):
    feedback = [0, 0]
    lst = []

    # this one checks if the numbers are in the same spot
    for i in range(0, 4):
        if code[i] == guess[i]:
            feedback[0] += 1
            lst.append(guess[i])

    # this checks if it is in the code
    for i in range(0, 4):
        if guess[i] in code:
            num = guess[i]
            guess_count = guess.count(num)
            answer_count = code.count(num)

            # if an numbers appears more in answer than in the list and it appears more in guess than in the list
            # only then can u can increase the feedback
            if lst.count(guess[i]) < guess_count and lst.count(guess[i]) < answer_count:
                lst.append(num)
                feedback[1] += 1

    feedback = [str(feedback[0]), str(feedback[1])]
    return feedback
