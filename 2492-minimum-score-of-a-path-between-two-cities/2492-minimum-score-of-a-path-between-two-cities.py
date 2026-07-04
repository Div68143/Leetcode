from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        adj = defaultdict(list)
        for a, b, d in roads:
            adj[a].append((b, d))
            adj[b].append((a, d))
        
        # BFS to find all nodes in component containing node 1
        visited = set([1])
        queue = deque([1])
        ans = float('inf')
        
        while queue:
            node = queue.popleft()
            for neighbor, dist in adj[node]:
                ans = min(ans, dist)
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return ans