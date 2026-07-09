class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        
        # Union-Find
        parent = list(range(n))
        rank   = [0] * n
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x
        
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
        
        # Since nums is sorted, only check adjacent pairs
        for i in range(n - 1):
            if nums[i+1] - nums[i] <= maxDiff:
                union(i, i + 1)
        
        # Answer queries
        return [find(u) == find(v) for u, v in queries]