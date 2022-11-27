from Tema_2 import *

def user_input_f():
    control_list = ['Inchide']

    while True:
        user_input = input('Alege un numar intreg')

        if user_input.isdigit():
            return {
                'is_palindrome': palindrome(user_input),
                'is_prime': is_prime(user_input),
                'div': div(user_input),
                'max_div': max_div(user_input),
                'digits': digits(user_input)
            }

        else user_input.lower() in control_list[]

            print('Final')
            break

print(user_input_f())