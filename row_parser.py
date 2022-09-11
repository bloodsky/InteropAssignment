import csv
import logging
from dataclasses import dataclass, fields

#
#                                                          *------------------------ [--RowParser------]
#                       /---CsvList Class------------------|-------------\           | id = ''         |
#   *--------*          |                                  v             |           | name = ''       |
#   |        |          |       rows = [ RowParser(), RowParser(), ... ] |           | surname = ''    |
#   |  .CSV  | ------>  |   *---duplicates = ()                          |           | ...             |
#   |        |          |   |   errors = {}                              |           | ...             |
#   *--------*          |   |      |                                     |           | currency = ''   |
#                       \---|------|-------------------------------------/           [-----------------]
#                           |      v
#                           |      used by RowParser to record errors found in a line
#                           v
#                           used by RowParser to keep track of ids to make sure no duplicate is injected


class CsvList:
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
                p = RowParser(row['id'], row['name'], row['surname'], row['birth-year'],
                              row['country'], row['yearly-amount'], row['monthly-variation'],
                              row['currency'])
                if p.id not in self.__entries:
                    self.__entries[p.id] = p
                else:
                    raise InvalidRowException('ID must be unique number, found a duplicate!')
            except InvalidRowException as e:
                logging.error(f' Found an error at row {index}: {e}')

    def __iter__(self):
        return iter(self.__entries.values())

    def __getitem__(self, item):
        return self.__entries[item]


@dataclass
class RowParser:
    id: int
    name: str
    surname: str
    birth_year: int
    country: str
    yearly_amount: int
    monthly_variation: int
    currency: str

    def constraints_check(self, value_with_err):
        try:
            match value_with_err:
                case 'id':
                    # Types not mathing! Try to convert to int
                    self.id = int(self.id)
                    if self.id <= 0:
                        raise InvalidRowException("ID can't be a negative number!")
                case 'yearly_amount':
                    self.yearly_amount = int(self.yearly_amount)

                case 'monthly_variation':
                    self.monthly_variation = int(self.monthly_variation)

                case 'birth_year':
                    self.birth_year = int(self.birth_year)
        except ValueError:
            # Int conversion raise a ValueError -> Int containing alphas or empty! Str is empty or mean 0 (zero)
            if value_with_err == 'yearly_amount':
                self.yearly_amount = 0
            elif value_with_err == 'monthly_variation':
                self.monthly_variation = 0
            else:
                raise InvalidRowException(value_with_err+' is invalid!')

    # Post_Init needed to validate correct type. Is called right after __init__ method of this dataclass
    def __post_init__(self):
        for f in fields(type(self)):
            if not isinstance(getattr(self, f.name), f.type):
                # type(getattr(self, f.name)) == type received
                # f.type == type take should be
                # f.name == field
                self.constraints_check(f.name)
            elif self.name == '' and self.surname == '':
                raise InvalidRowException('One between name and surname must be non-empty!')


class InvalidRowException(BaseException):
    pass
