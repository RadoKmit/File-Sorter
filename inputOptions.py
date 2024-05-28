import os

def option_choice(text):
    choice = input(text + " >>")
    os.system("cls")
    return choice

def multiple_par_choice(text):
    answer = option_choice(text)
    return [str(x) for x in answer.split(" ")]