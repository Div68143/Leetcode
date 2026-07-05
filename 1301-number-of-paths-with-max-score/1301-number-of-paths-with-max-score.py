class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        MOD = 10**9 + 7
        n = len(board)
        
        # dp[r][c] = (max_sum, count)
        INF = float('-inf')
        dp = [[(INF, 0)] * n for _ in range(n)]
        
        # Start at S = bottom-right
        dp[n-1][n-1] = (0, 1)
        
        # Fill DP from bottom-right to top-left
        for r in range(n-1, -1, -1):
            for c in range(n-1, -1, -1):
                if board[r][c] == 'X':
                    continue
                if dp[r][c][1] == 0:  # unreachable
                    continue
                
                curr_sum, curr_cnt = dp[r][c]
                
                # Current cell value (S and E contribute 0)
                val = 0
                if board[r][c].isdigit():
                    val = int(board[r][c])
                
                # Move to: up (r-1,c), left (r,c-1), up-left (r-1,c-1)
                for nr, nc in [(r-1, c), (r, c-1), (r-1, c-1)]:
                    if nr < 0 or nc < 0:
                        continue
                    if board[nr][nc] == 'X':
                        continue
                    
                    new_sum = curr_sum + val
                    prev_sum, prev_cnt = dp[nr][nc]
                    
                    if new_sum > prev_sum:
                        dp[nr][nc] = (new_sum, curr_cnt % MOD)
                    elif new_sum == prev_sum:
                        dp[nr][nc] = (prev_sum, (prev_cnt + curr_cnt) % MOD)
        
        best_sum, best_cnt = dp[0][0]
        if best_cnt == 0:
            return [0, 0]
        return [best_sum, best_cnt % MOD]