import unittest

from row_parser import InvalidRecordException, RecordCollection


class TestRecordCollection(unittest.TestCase):
    def test_duplicated_id(self):
        # Simulating read from a CSV file
        r0 = {
            'id': '1',
            'name': 'roberto',
            'surname': '',
            'birth-year': '1234',
            'country': 'test',
            'yearly-amount': '456',
            'monthly-variation': '+56',
            'currency': 'EUR'
        }

        r1 = {
            'id': '1',
            'name': 'marco',
            'surname': 'ciao',
            'birth-year': '134',
            'country': 'test',
            'yearly-amount': '456',
            'monthly-variation': '+56',
            'currency': 'EUR'
        }

        rc = RecordCollection([r0, r1])
        l = [x for x in rc] # list must contain only one row-record
        self.assertEqual(len(l), 1)

    def test_wrong_file(self):
        rc = RecordCollection.from_csv_file('')
        self.assertEqual(rc,None)


if __name__ == '__main__':
    unittest.main()
