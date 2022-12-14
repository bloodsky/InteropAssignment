import assignments
import logging


def get_user_input():
    user_input = input('Enter your selection : ')
    try:
        input_list = user_input.split(' ')
        if len(input_list) == 1:
            return int(input_list[0]), None, None
        elif len(input_list) == 2:
            return int(user_input.split(' ')[0]), user_input.split(' ')[1], None
        elif len(input_list) == 3:
            return int(user_input.split(' ')[0]), user_input.split(' ')[1], user_input.split(' ')[2]
        else:
            raise TooManyArgumentsException('Max number of parameters is 3!')
    except ValueError as e:
        logging.error(f' The input you provided is not valid: {e}.\nPlease try again!')


class TooManyArgumentsException(BaseException):
    pass


def display_prompt():  # OK
    print("\nPlease enter one of the following commands to execute an assignment:\n"
          "'1 <CSV filename>' to compute the richest and poorest people from the specified CSV file;\n"
          "'2 <CSV filename>' to get a list of the surnames of the greek users from the specified CSV file;\n"
          "'3 <CSV filename>' to get the list of the countries using ITL as a currency from the specified CSV file;\n"
          "'4 <CSV filename>' to get the top 5 list of countries with the highest number of users from the specified "
          "CSV file;\n"
          "'5 <CSV filename>' to compute for each persone the next-year amount using the monthly variation from the "
          "specified CSV file;\n"
          "'6 <CSV filename> <CSV filename>' to tell for each person in both files if is richer or poorer and the "
          "money delta from the specified CSV file;\n"
          "'7 exit' to exit program\n")


if __name__ == "__main__":
    while True:
        display_prompt()
        try:
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
                case 7:
                    exit()
        except Exception as e:
            logging.error(f"Something went wrong: {e}")
