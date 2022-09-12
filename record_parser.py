import csv
import logging
from typing import Optional


#
#                                                *--------------------------------- [--Record---------]
#                       /---RecordCollection ----|----------------------\           | id = ''         |
#   *--------*          |                        v                      |           | name = ''       |
#   |        |          |       rows = { id: Record(), ... }            |           | surname = ''    |
#   |  .CSV  | ------>  |       handle duplicates                       |           | ...             |
#   |        |          |       logging errors                          |           | ...             |
#   *--------*          |                                               |           | currency = ''   |
#                       \-----------------------------------------------/           [-----------------]
#


class RecordCollection:
    @classmethod
    def from_csv_file(cls, filename):
        with open(filename, newline='\n') as csvfile:
            reader = csv.DictReader(csvfile)
            return cls(reader)

    def __init__(self, entry_iterator):
        self.__entries = {}
        for index, row in enumerate(entry_iterator):
            # Parsing raw data
            row = {k.strip(): v.strip() for k, v in row.items()}
            try:
                p = Record(row['id'], row['name'], row['surname'], row['birth-year'],
                           row['country'], row['yearly-amount'], row['monthly-variation'],
                           row['currency'])
                # Handle duplicates
                if p.id not in self.__entries:
                    self.__entries[p.id] = p
                else:
                    raise InvalidRecordException('ID must be unique number, found a duplicate!')
            except InvalidRecordException as e:
                logging.error(f' Found an error at row {index}: {e}')

    def __iter__(self):
        return iter(self.__entries.values())

    def __getitem__(self, item):
        return self.__entries[item]


class InvalidRecordException(BaseException):
    pass


class Record:
    id: int
    name: str
    surname: str
    birth_year: int
    country: str
    yearly_amount: int
    monthly_variation: int
    currency: str

    def __init__(self, id: int, name: str, surname: str, birth_year: int, country: str, yearly_amount: Optional[int],
                 monthly_variation: Optional[int], currency: Optional[str]):
        try:
            self.id = int(id)
        except ValueError:
            raise InvalidRecordException("ID must be an integer")
        if self.id <= 0:
            raise InvalidRecordException("ID can't be a negative number!")

        self.name = str(name)
        self.surname = str(surname)

        if self.name == '' and self.surname == '':
            raise InvalidRecordException('One between name and surname must be non-empty!')

        try:
            self.birth_year = int(birth_year)
        except ValueError:
            raise InvalidRecordException("Birth year must be an integer")

        self.country = str(country)

        if yearly_amount is None or yearly_amount == "":
            self.yearly_amount = 0
        else:
            try:
                self.yearly_amount = int(yearly_amount)
            except ValueError:
                raise InvalidRecordException("Yearly amount, if set, must be an integer")

        if monthly_variation is None or monthly_variation == "":
            self.monthly_variation = 0
        else:
            try:
                self.monthly_variation = int(monthly_variation)
            except ValueError:
                raise InvalidRecordException("Monthly amount, if set, must be an integer")

        if currency is None or currency == "":
            self.currency = "EUR"
        else:
            self.currency = str(currency)


def eur_yearly_amount(amount, currency):
    if currency == 'USD' or currency == 'EUR':
        return amount
    elif currency == 'ITL':
        return amount / 1936.27
    elif currency == 'GBP':
        return amount * 1.18
    else:
        raise UnknownExchangeRateException("Unknown currency found!")


class UnknownExchangeRateException(BaseException):
    pass

