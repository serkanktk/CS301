# -*- coding: utf-8 -*-
"""
@author: Serkan
"""

def generate_incremental_instance(n):
    V = list(range(n))
    E = []
    for i in range(n):
        for j in range(i+1, n):
            E.append((i, j))                
    s, t = 0, 1
    k = n // 2
    G = {node: [] for node in V}
    for edge in E:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])
    
    return G, s, t, k

for i in range(2, 10):
    G, s, t, k = generate_incremental_instance(i)
    print(G, s, t, k)