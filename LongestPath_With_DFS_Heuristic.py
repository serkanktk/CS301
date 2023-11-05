def DFSForLongest_Path(G, current_node, t, visited, path, k):
    path.append(current_node)
    visited[current_node] = True
    temp = True
    if(current_node == t and len(path) - 1 >= k):
        print("Path found with given constraints: ", path)
        return temp

    for each in G[current_node]:
        if visited[each] == False:
            if DFSForLongest_Path(G, each, t, visited, path, k):
                return temp
    path.pop()
    visited[current_node] = False
    return False

def CheckMinEdge(G, s, t, k):
    path = []
    visited = {node: False for node in G.keys()}
    
    if not DFSForLongest_Path (G, s, t, visited, path, k):
        print("The path does not exist at least", k, "edges!!")

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
    print(f'Test case {i+1}:')
    CheckMinEdge(G, s, t, k)
    
#Uncomment below section to unit test    
"""    
import unittest

class TestLongestPath(unittest.TestCase):

    def setUp(self):
        self.graph1 = {1: [2, 3], 2: [3, 4], 3: [4], 4: []}
        self.graph2 = {1: [2], 2: [3], 3: [4], 4: []}

    def test_DFSForLongest_Path(self):
        path = []
        visited = {node: False for node in self.graph1.keys()}
        self.assertTrue(DFSForLongest_Path(self.graph1, 1, 4, visited, path, 3))
        path = []
        visited = {node: False for node in self.graph2.keys()}
        self.assertFalse(DFSForLongest_Path(self.graph2, 1, 4, visited, path, 3))

    def test_CheckMinEdge(self):
        self.assertIsNone(CheckMinEdge(self.graph1, 1, 4, 3))
        self.assertIsNone(CheckMinEdge(self.graph2, 1, 4, 3))

if __name__ == '__main__':
    unittest.main()    
    """
    