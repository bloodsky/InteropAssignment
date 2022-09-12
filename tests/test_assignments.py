import logging
import unittest

from unittest.mock import patch

from assignments import assignment1, assignment2, assignment3


class TestAssignment(unittest.TestCase):

    @patch('builtins.print')
    def test_assignment1_file(self, mock_print):
        assignment1('input-test-files/input_file_test1.csv')
        mock_print.assert_called_with("\nRichest: Ursula Le Guin, Poorest: Galileo Galilei")

    @patch('builtins.print')
    def test_assignment2_file(self, mock_print):
        assignment2('input-test-files/input_file_test2.csv')
        lstr = ['Catozzo']
        mock_print.assert_called_with('\nGreek users:', ', '.join(lstr))

    @patch('builtins.print')
    def test_assignment3_file(self, mock_print):
        assignment3('input-test-files/input_file_test2.csv')
        lstr = ['Italy', 'Tatooine']
        mock_print.assert_called_with('\nITL using countries:', ', '.join(lstr))


if __name__ == '__main__':
    unittest.main()
