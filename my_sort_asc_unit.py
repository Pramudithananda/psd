import unittest
from my_sort_asc import my_sort_asc

class TestMySortAsc(unittest.TestCase):
    def test_empty_list(self):
        lst = []
        expected_output = []
        self.assertEqual(my_sort_asc(lst), expected_output)

    def test_sorted_list(self):
        lst = [1, 2, 3, 4, 5]
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(my_sort_asc(lst), expected_output)

    def test_reverse_sorted_list(self):
        lst = [5, 4, 3, 2, 1]
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(my_sort_asc(lst), expected_output)

    def test_unsorted_list(self):
        lst = [3, 1, 4, 2, 5]
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(my_sort_asc(lst), expected_output)

    def test_list_with_duplicates(self):
        lst = [3, 1, 4, 2, 5, 1]
        expected_output = [1, 1, 2, 3, 4, 5]
        self.assertEqual(my_sort_asc(lst), expected_output)

if __name__ == '__main__':
    unittest.main()
