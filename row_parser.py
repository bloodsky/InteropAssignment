import csv
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
    def __init__(self):
        self.__rows = []
        self.__duplicates = set()
        self.__errors = {}
        self.__csv_loaded = False

    def get_csv(self):
        return self.__rows

    def get_duplicates_set(self):
        return self.__duplicates

    def get_errors_dict(self):
        return self.__errors

    def set_csv_status(self, status):
        self.__csv_loaded = status

    def get_csv_status(self):
        return self.__csv_loaded

    def clean(self):
        self.__rows = []
        self.get_duplicates_set().clear()
        self.get_errors_dict().clear()
        self.__csv_loaded = False


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
    index: int
    csv_list: CsvList  # Pointer to main struct holding all the csv

    def check_for_dups_and_neg(self):
        dup = self.csv_list.get_duplicates_set()
        if self.id not in dup:
            dup.add(self.id)
        else:
            self.csv_list.get_errors_dict()[self.index] = 'ID must be unique number, found a duplicate!'

    def constraints_check(self, value_with_err):
        try:
            match value_with_err:
                case 'id':
                    # Types not mathing! Try to convert to int
                    self.id = int(self.id)
                    if self.id > 0:
                        # Convert not raising ValueError -> Check for duplicate and negativity
                        self.check_for_dups_and_neg()
                    else:
                        self.csv_list.get_errors_dict()[self.index] = "ID can't be a negative number!"
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
                self.csv_list.get_errors_dict()[self.index] = value_with_err+' is invalid!'

    # Post_Init needed to validate correct type. Is called right after __init__ method of this dataclass
    def __post_init__(self):
        for f in fields(type(self)):
            if not isinstance(getattr(self, f.name), f.type):
                # type(getattr(self, f.name)) == type received
                # f.type == type take should be
                # f.name == field
                self.constraints_check(f.name)
            elif self.name == '' and self.surname == '':
                self.csv_list.get_errors_dict()[self.index] = 'One between name and surname must be non-empty!'


def read(c_list, filename):
    with open(filename, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile)
        for index, row in enumerate(reader):
            # Parsing raw data
            row = {k.strip(): v.strip() for k, v in row.items()}
            p = RowParser(row['id'], row['name'], row['surname'], row['birth-year'],
                          row['country'], row['yearly-amount'], row['monthly-variation'],
                          row['currency'], index, c_list)
            c_list.get_csv().append(p)
