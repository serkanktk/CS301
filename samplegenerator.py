# -*- coding: utf-8 -*-
"""

@author: Serkan
"""

import random

def generate_random_instance(n):
    V = list(range(n))
    E = []
    for i in range(n):
        for j in range(i+1, n):
            if random.choice([True, False]):
                E.append((i, j))                
    s, t = random.sample(V, 2)
    k = random.randint(1, n)
    G = {node: [] for node in V}
    for edge in E:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])
    
    return G, s, t, k
for i in range(20):
    G, s, t, k = generate_random_instance(5)
    print(G, s, t, k)