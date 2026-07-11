from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        # Union-Find
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            parent[find(x)] = find(y)

        for a, b in edges:
            union(a, b)

        # Count nodes and edges per component
        node_cnt = defaultdict(int)
        edge_cnt = defaultdict(int)

        for i in range(n):
            node_cnt[find(i)] += 1

        for a, b in edges:
            edge_cnt[find(a)] += 1

        # Check completeness: k nodes need k*(k-1)/2 edges
        result = 0
        for root in node_cnt:
            k = node_cnt[root]
            if edge_cnt[root] == k * (k - 1) // 2:
                result += 1

        return result