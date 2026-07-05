class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        MOD = 10**9 + 7
        n = len(board)
        
        INF = float('-inf')
        dp_sum = [[INF] * n for _ in range(n)]
        dp_cnt = [[0]   * n for _ in range(n)]
        
        dp_sum[n-1][n-1] = 0
        dp_cnt[n-1][n-1] = 1
        
        for r in range(n-1, -1, -1):
            for c in range(n-1, -1, -1):
                if board[r][c] == 'X' or dp_cnt[r][c] == 0:
                    continue
                
                curr_sum = dp_sum[r][c]
                curr_cnt = dp_cnt[r][c]
                val = int(board[r][c]) if board[r][c].isdigit() else 0
                
                for nr, nc in [(r-1, c), (r, c-1), (r-1, c-1)]:
                    if nr < 0 or nc < 0 or board[nr][nc] == 'X':
                        continue
                    
                    new_sum = curr_sum + val
                    
                    if new_sum > dp_sum[nr][nc]:
                        dp_sum[nr][nc] = new_sum
                        dp_cnt[nr][nc] = curr_cnt % MOD
                    elif new_sum == dp_sum[nr][nc]:
                        dp_cnt[nr][nc] = (dp_cnt[nr][nc] + curr_cnt) % MOD
        
        if dp_cnt[0][0] == 0:
            return [0, 0]
        return [dp_sum[0][0], dp_cnt[0][0] % MOD]