import unittest

from row_parser import Record, InvalidRecordException, RecordCollection


class TestRecordIDs(unittest.TestCase):

    def test_empty_id(self):
        self.assertRaises(InvalidRecordException, Record, '', 'test', 'test', '1234', 'test', '456', '+56', 'EUR')

    def test_negative_id(self):
        self.assertRaises(InvalidRecordException, Record, '-123', 'test', 'test', '1234', 'test', '456', '+56', 'EUR')

    def test_well_formatted_id(self):
        raised = False
        try:
            r = Record('123', 'test', 'test', '1234', 'test', '456', '+56', 'EUR')
        except InvalidRecordException:
            raised = True
        self.assertFalse(raised, 'Exception raised')

    def test_name_surname_empty(self):
        self.assertRaises(InvalidRecordException, Record, '1', '', '', '1234', 'test', '456', '+56', 'EUR')

    def test_only_name(self):
        raised = False
        try:
            r = Record(1, 'roberto', '', 1234, 'test', 456, +56, 'EUR')
        except InvalidRecordException:
            raised = True
        self.assertFalse(raised, 'Exception raised')
        self.assertEqual(r.name, 'roberto')
        self.assertEqual(r.surname, '')

    def test_only_surname(self):
        raised = False
        try:
            r = Record(1, '', 'qwerty', 1234, 'test', 456, +56, 'EUR')
        except InvalidRecordException:
            raised = True
        self.assertFalse(raised, 'Exception raised')
        self.assertEqual(r.name, '')
        self.assertEqual(r.surname, 'qwerty')

    def test_yearly_amount(self):
        self.assertRaises(InvalidRecordException, Record, '1', 'test', '', '1234', 'test', '4ert', '+56', 'EUR')
        r = Record(1, 'roberto', '', 1234, 'test', '', +56, 'EUR')
        self.assertEqual(r.yearly_amount, 0)

    def test_monthly_variation(self):
        self.assertRaises(InvalidRecordException, Record, '1', 'test', '', '1234', 'test', '-234', '+ciao56', 'EUR')
        r = Record(1, 'roberto', '', 1234, 'test', 456, '', 'EUR')
        self.assertEqual(r.monthly_variation, 0)

    def test_currency(self):
        r = Record(1, 'roberto', '', 1234, 'test', 456, -67, '')
        self.assertEqual(r.currency, 'EUR')


if __name__ == '__main__':
    unittest.main()
