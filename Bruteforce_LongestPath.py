# -*- coding: utf-8 -*-
"""

@author: OzgeKarasu
"""
import time
import random
def is_simple_path(path):
    visited_nodes = set()
    for node in path:
        if node in visited_nodes:
            return False
        visited_nodes.add(node)
    return True

def length(path):
    return len(path) - 1  

def checklongest(G, s, t, k, path=[]):
    path = path + [s]
    if s == t:
        return is_simple_path(path) and length(path) >= k
    for node in G[s]:
        if node not in path:
            if checklongest(G, node, t, k, path):
                return True
    return False
test_cases = [
    ({0: [2, 4], 1: [], 2: [0, 4], 3: [4], 4: [0, 2, 3]}, 3, 0, 3),
    ({0: [1, 2, 3], 1: [0, 4], 2: [0, 3, 4], 3: [0, 2], 4: [1, 2]}, 4, 2, 1),
    ({0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2], 4: []}, 2, 1, 5),
    ({0: [1, 2], 1: [0, 2, 3, 4], 2: [0, 1], 3: [1, 4], 4: [1, 3]}, 2, 4, 4),
    ({0: [1, 3, 4], 1: [0, 2, 3, 4], 2: [1, 4], 3: [0, 1, 4], 4: [0, 1, 2, 3]}, 0, 3, 2),
    ({0: [1, 2, 3, 4], 1: [0], 2: [0, 4], 3: [0], 4: [0, 2]}, 4, 2, 1),
    ({0: [3], 1: [2, 4], 2: [1, 4], 3: [0], 4: [1, 2]}, 4, 3, 5),
    ({0: [1, 2, 4], 1: [0, 2], 2: [0, 1, 3, 4], 3: [2, 4], 4: [0, 2, 3]}, 3, 2, 2),
    ({0: [3], 1: [], 2: [3, 4], 3: [0, 2, 4], 4: [2, 3]}, 2, 3, 1),
    ({0: [4], 1: [2], 2: [1], 3: [], 4: [0]}, 3, 4, 5),
    ({0: [1, 2, 4], 1: [0, 2, 3, 4], 2: [0, 1, 3], 3: [1, 2], 4: [0, 1]}, 0, 1, 1),
    ({0: [3], 1: [2], 2: [1, 3, 4], 3: [0, 2, 4], 4: [2, 3]}, 3, 1, 1),
    ({0: [], 1: [4], 2: [3, 4], 3: [2], 4: [1, 2]}, 1, 4, 3),
    ({0: [2], 1: [2, 4], 2: [0, 1, 3, 4], 3: [2, 4], 4: [1, 2, 3]}, 3, 1, 5),
    ({0: [3, 4], 1: [2, 4], 2: [1, 4], 3: [0], 4: [0, 1, 2]}, 2, 3, 1),
    ({0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3, 4], 3: [1, 2], 4: [2]}, 2, 3, 5),
    ({0: [3, 4], 1: [3, 4], 2: [3, 4], 3: [0, 1, 2], 4: [0, 1, 2]}, 2, 0, 1),
    ({0: [1, 2, 3], 1: [0, 4], 2: [0, 3, 4], 3: [0, 2, 4], 4: [1, 2, 3]}, 0, 1, 5),
    ({0: [2, 3, 4], 1: [2, 3, 4], 2: [0, 1], 3: [0, 1], 4: [0, 1]}, 4, 1, 5),
    ({0: [], 1: [], 2: [], 3: [4], 4: [3]}, 3, 0, 5)
]

for i, (G, s, t, k) in enumerate(test_cases):
    print(f'Test case {i+1}: {checklongest(G, s, t, k)}')

    
#Uncomment below section to unit test    
"""import unittest
class TestLongestPath(unittest.TestCase):

    def setUp(self):
        self.graph1 = {1: [2, 3], 2: [3, 4], 3: [4], 4: []}
        self.graph2 = {1: [2], 2: [3], 3: [4], 4: []}

    def test_simple_path(self):
        self.assertTrue(is_simple_path([1, 2, 3, 4]))
        self.assertFalse(is_simple_path([1, 2, 3, 4, 2]))

    def test_length(self):
        self.assertEqual(length([1, 2, 3, 4]), 3)

    def test_checklongest(self):
        self.assertTrue(checklongest(self.graph1, 1, 4, 3))
        self.assertFalse(checklongest(self.graph2, 1, 4, 3))

if __name__ == '__main__':
    unittest.main()    """