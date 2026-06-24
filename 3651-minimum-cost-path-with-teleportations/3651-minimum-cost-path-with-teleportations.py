import heapq
import bisect

class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = float('inf')

        all_cells = sorted(
            (grid[i][j], i, j) for i in range(m) for j in range(n)
        )
        all_vals = [c[0] for c in all_cells]

        # dist[i][j][t] — consistent indexing throughout
        dist = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]
        dist[0][0][0] = 0

        settled = [[[False] * (k + 1) for _ in range(n)] for _ in range(m)]

        # max_pushed[t] = highest all_cells index already pushed into layer t
        max_pushed = [-1] * (k + 1)

        heap = [(0, 0, 0, 0)]  # (cost, i, j, t)

        while heap:
            cost, i, j, t = heapq.heappop(heap)

            if settled[i][j][t]:
                continue
            settled[i][j][t] = True

            if i == m - 1 and j == n - 1:
                return cost

            # Normal moves: right and down
            for di, dj in [(0, 1), (1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    nc = cost + grid[ni][nj]
                    if nc < dist[ni][nj][t]:          # fixed: [ni][nj][t]
                        dist[ni][nj][t] = nc
                        heapq.heappush(heap, (nc, ni, nj, t))

            # Teleport into layer t+1
            if t < k:
                cur_val = grid[i][j]
                idx = bisect.bisect_right(all_vals, cur_val)
                nt = t + 1
                if idx - 1 > max_pushed[nt]:
                    for ci in range(max_pushed[nt] + 1, idx):
                        _, x, y = all_cells[ci]
                        if cost < dist[x][y][nt]:     # fixed: [x][y][nt]
                            dist[x][y][nt] = cost
                            heapq.heappush(heap, (cost, x, y, nt))
                    max_pushed[nt] = idx - 1

        return min(dist[m-1][n-1][t] for t in range(k + 1))