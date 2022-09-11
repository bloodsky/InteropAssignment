from collections import Counter
from row_parser import CsvList
from utils.utils_functions import convert_currency


def assignment1(filename):
    csv_as_list = CsvList.from_csv_file(filename)
    partial = [(f"{row.name} {row.surname}", convert_currency(row.yearly_amount, row.currency)) for row in csv_as_list]
    richest = max(partial, key=lambda x: x[1])
    poorest = min(partial, key=lambda x: x[1])
    print(f'Richest: {richest}, Poorest: {poorest}')


def assignment2(filename):
    csv_as_list = CsvList.from_csv_file(filename)
    print('Greek users:', ', '.join([row.surname for row in csv_as_list if row.country == 'Greece']))


def assignment3(filename):
    csv_as_list = CsvList.from_csv_file(filename)
    print('ITL using countries:', ', '.join([row.country for row in csv_as_list if row.currency == 'ITL']))


def assignment4(filename):
    csv_as_list = CsvList.from_csv_file(filename)
    count = Counter([row.country for row in csv_as_list])
    res = sorted(count.items(), key=lambda x: x[1], reverse=True)
    [print(v[0], v[1]) for v in res]


def assignment5(filename):
    csv_as_list = CsvList.from_csv_file(filename)
    for row in csv_as_list:
        amount = row.yearly_amount + row.monthly_variation * 12
        print(f'Next year {row.name} {row.surname} will have {amount} {row.currency}')


def assignment6(filename1, filename2):
    csv_as_list = CsvList.from_csv_file(filename1)
    csv_as_list2 = CsvList.from_csv_file(filename2)

    # Actual assignment
    for row in csv_as_list:
        first_amount = row.yearly_amount
        second_amount = csv_as_list2[row.id].yearly_amount
        delta = first_amount - second_amount
        currency = row.currency
        if delta > 0:
            print(row.name, row.surname, 'is', delta, currency, 'richer than before')
        else:
            print(row.name, row.surname, 'is', delta, currency, 'poorer than before')
