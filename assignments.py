from collections import Counter

from row_parser import CsvList
from utils.utils_functions import get_list_dir, print_menu, row_is_wrong, convert_currency, load_csv


def assignment1(csv_struct):
    csv_as_list = csv_struct.get_csv()
    partial = []
    for row in csv_as_list:
        if not row_is_wrong(row.index, csv_struct.get_errors_dict()):
            partial.append((row.name + ' ' + row.surname, convert_currency(row.yearly_amount, row.currency)))
    res = sorted(partial, key=lambda x: x[1], reverse=True)
    print('Richest:', res[0][0], ', Poorest:', res[-1][0])


def assignment2(csv_struct):
    csv_as_list = csv_struct.get_csv()
    res = []
    for row in csv_as_list:
        if not row_is_wrong(row.index, csv_struct.get_errors_dict()) and row.country == 'Greece':
            res.append(row.surname)
    print('Greek users:', ', '.join(res))


def assignment3(csv_struct):
    csv_as_list = csv_struct.get_csv()
    res = []
    for row in csv_as_list:
        if not row_is_wrong(row.index, csv_struct.get_errors_dict()) and row.currency == 'ITL':
            res.append(row.country)
    print('ITL using countries:', ', '.join(res))


def assignment4(csv_struct):
    csv_as_list = csv_struct.get_csv()
    partial = []
    for row in csv_as_list:
        if not row_is_wrong(row.index, csv_struct.get_errors_dict()):
            partial.append(row.country)
    count = Counter(partial)
    res = sorted(count.items(), key=lambda x: x[1], reverse=True)
    [print(v[0], v[1]) for v in res]


def assignment5(csv_struct):
    csv_as_list = csv_struct.get_csv()
    for row in csv_as_list:
        if not row_is_wrong(row.index, csv_struct.get_errors_dict()):
            amount = row.yearly_amount + row.monthly_variation * 12
            print('Next year', row.name, row.surname, 'will have', amount, row.currency)


def assignment6(csv_struct):
    csv_as_list = csv_struct.get_csv()

    # Same job as loading the main csv file
    csv_struct2 = CsvList()
    loadCsvFile(csv_struct2)
    csv_as_list2 = csv_struct2.get_csv()

    # Actual assignment
    for row in csv_as_list:
        first_amount = row.yearly_amount
        second_amount = csv_as_list2[row.index].yearly_amount
        delta = first_amount - second_amount
        currency = row.currency
        if delta > 0:
            print(row.name, row.surname, 'is', delta, currency, 'richer than before')
        else:
            print(row.name, row.surname, 'is', delta, currency, 'poorer than before')

    del csv_struct2


def loadCsvFile(csv_struct):
    files = get_list_dir()
    print_menu(files)
    load_csv(csv_struct, files)


def close(csv_struct):
    del csv_struct
    exit()


# Create a menu dictionary where the key is an integer number and the
# value is a function name.
functions_names = [assignment1, assignment2, assignment3, assignment4, assignment5, assignment6, loadCsvFile, close]
functions_menu = dict(zip(range(1, len(functions_names) + 1), functions_names))
