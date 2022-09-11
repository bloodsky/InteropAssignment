import assignments
import logging

def get_user_input():
    user_input = input('Enter your selection : ')
    try:
        res = int(user_input.split(' ')[0])
        filename1 = user_input.split(' ')[1]
        try:
            filename2 = user_input.split(' ')[2]
        except IndexError:
            filename2 = None
        return res, filename1, filename2
    except ValueError as e:
        logging.error(f' The input you provided is not valid: {e}.\nPlease try again!')


def display_prompt():  # OK
    print("Please enter one of the following commands to execute an assigment:\n"
          "'1 <CSV filename>' to compute the richest and poorest people from the specified CSV file;\n"
          "")


if __name__ == "__main__":
    while True:
        display_prompt()
        (assignment_number, filename1, filename2) = get_user_input()
        match assignment_number:
            case 1:
                assignments.assignment1(filename1)
            case 2:
                assignments.assignment2(filename1)
            case 3:
                assignments.assignment3(filename1)
            case 4:
                assignments.assignment4(filename1)
            case 5:
                assignments.assignment5(filename1)
            case 6:
                assignments.assignment6(filename1, filename2)
            case _:
                exit()
