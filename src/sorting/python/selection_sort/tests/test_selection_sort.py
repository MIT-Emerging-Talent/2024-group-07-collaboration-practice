import unittest

import os
import sys

file_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_dir + "/src")

from selection_sort import selectionsort_v1


class TestSelectionSortV1(unittest.TestCase):
    def test_empty_array(self):
        array = list()
        result = list()

        self.assertEqual(selectionsort_v1(array), result)

    def test_single_element(self):
        array = [1]
        result = [1]

        self.assertEqual(selectionsort_v1(array), result)

    def test_increasing_order(self):
        array = [1, 2, 3, 4, 5]
        result = [1, 2, 3, 4, 5]

        self.assertEqual(selectionsort_v1(array), result)

    def test_decreasing_order(self):
        array = [5, 4, 3, 2, 1]
        result = [1, 2, 3, 4, 5]

        self.assertEqual(selectionsort_v1(array), result)

    def test_random_order(self):
        array = [2, 5, 1, 4, 3]
        result = [1, 2, 3, 4, 5]

        self.assertEqual(selectionsort_v1(array), result)

    def test_duplicate_elements(self):
        array = [3, 1, 4, 2, 3, 4, 1]
        result = [1, 1, 2, 3, 3, 4, 4]

        self.assertEqual(selectionsort_v1(array), result)

    def test_negative_numbers(self):
        array = [-5, -2, -8, -1, -3]
        result = [-8, -5, -3, -2, -1]

        self.assertEqual(selectionsort_v1(array), result)

    def test_mixed_positive_and_negative_numbers(self):
        array = [10, -5, 7, -2, 4, -1]
        result = [-5, -2, -1, 4, 7, 10]

        self.assertEqual(selectionsort_v1(array), result)

if __name__ == "__main__":
    unittest.main()
