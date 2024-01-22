# test_eulerian_path.py

import unittest
from eulerian_path import eulerian_path

class TestEulerianPath(unittest.TestCase):
    def test_eulerian_path_exists(self):
        # Test cases where Eulerian paths should exist
        graph1 = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}
        self.assertTrue(eulerian_path(graph1))

        graph2 = {0: [1, 2, 3, 4], 1: [0, 2, 3, 4],
                  2: [0, 1, 3, 4], 3: [0, 1, 2, 4],
                  4: [0, 1, 2, 3]}
        self.assertTrue(eulerian_path(graph2))

    def test_no_eulerian_path(self):
        # Test cases where no Eulerian path exists
        graph3 = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2, 4], 4: []}
        self.assertEqual(eulerian_path(graph3), "No Eulerian path exists")

        graph4 = {0: [1, 2, 3], 1: [0, 2, 3], 2: [0, 1, 3], 3: [0, 1, 2], 4: []}
        self.assertEqual(eulerian_path(graph4), "No Eulerian path exists")

if __name__ == "__main__":
    unittest.main()
