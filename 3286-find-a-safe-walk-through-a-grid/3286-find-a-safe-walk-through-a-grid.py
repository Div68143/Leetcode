from collections import deque

class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        # min_damage[r][c] = minimum health lost to reach (r,c)
        min_damage = [[float('inf')] * n for _ in range(m)]
        min_damage[0][0] = grid[0][0]
        
        # 0-1 BFS: cost 0 for safe cell, cost 1 for unsafe
        dq = deque([(0, 0)])
        
        while dq:
            r, c = dq.popleft()
            
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_damage = min_damage[r][c] + grid[nr][nc]
                    if new_damage < min_damage[nr][nc]:
                        min_damage[nr][nc] = new_damage
                        # cost 0 → front, cost 1 → back
                        if grid[nr][nc] == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))
        
        # Need health - min_damage >= 1  →  min_damage <= health - 1
        return min_damage[m-1][n-1] <= health - 1