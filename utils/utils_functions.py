import glob
import logging
import os

from row_parser import read


def is_csv_loaded(selection, csv_status):
    if selection != 7 and selection != 8 and not csv_status:
        print('\n')
        logging.error(' Load some CSV file first!')
        return False
    return True


def invalid_user_input():
    print('\n')
    logging.error(' Insert valid input')


def get_user_input(csv_struct, functions=True):
    res = int(input('Enter your selection : ' if not csv_struct.get_csv_status() else
                    'Enter your selection : (CSV file is loaded)'))  # Get function key
    menu = range(1, 9) if functions else range(1, 4)
    if res not in menu:
        raise ValueError
    print('\n')
    return res


def load_csv(csv_struct, files):
    try:
        selection = get_user_input(csv_struct, functions=False)  # Function false mean to print files not assignments!
        if csv_struct.get_csv_status():
            csv_struct.clean()
        read(csv_struct, files[selection])
        csv_struct.set_csv_status(True)
    except ValueError:
        invalid_user_input()


def get_list_dir():
    mylist = [f for f in glob.glob('input-test-files/*.csv')]
    return dict(zip(range(1, len(mylist) + 1), mylist))


def clear_screen():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")


def display_func_menu(m):  # OK
    print('\n')
    for k, function in m.items():
        print(str(k) + ') ' + function.__name__)


def convert_currency(amount, currency):  # OK
    if currency == 'USD' or currency == 'EUR' or currency == '':
        return amount
    elif currency == 'ITL':
        return amount / 1936.27
    elif currency == 'GBP':
        return amount * 1.18


def row_is_wrong(row_index, errors):  # OK
    if row_index in errors:
        logging.error(' Row '+str(row_index)+' '+str(errors[row_index]))


def print_menu(fdict):
    print('\n')
    for k in fdict.keys():
        print(str(k) + ') ' + fdict[k])
