import heapq
from collections import defaultdict

class Solution:
    def findMaxPathScore(self, edges, online, k):
        n = len(online)
        
        adj = defaultdict(list)
        for u, v, c in edges:
            adj[u].append((v, c))
        
        costs = sorted(set(c for _, _, c in edges))
        
        if not costs:
            return -1
        
        def canAchieve(min_cost):
            INF = float('inf')
            dist = [INF] * n
            dist[0] = 0
            heap = [(0, 0)]
            
            while heap:
                total, u = heapq.heappop(heap)
                if total > dist[u]:
                    continue
                if u == n - 1:
                    return total <= k
                for v, c in adj[u]:
                    if c < min_cost:
                        continue
                    if v != n - 1 and not online[v]:
                        continue
                    new_total = total + c
                    if new_total < dist[v]:
                        dist[v] = new_total
                        heapq.heappush(heap, (new_total, v))
            
            return dist[n-1] <= k
        
        lo, hi = 0, len(costs) - 1
        ans = -1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if canAchieve(costs[mid]):
                ans = costs[mid]
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans