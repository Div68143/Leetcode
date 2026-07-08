class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        m = len(s)
        
        prefix_sum = [0] * (m + 1)
        prefix_x   = [0] * (m + 1)
        prefix_cnt = [0] * (m + 1)
        
        for i in range(m):
            d = int(s[i])
            prefix_sum[i+1] = prefix_sum[i] + (d if d != 0 else 0)
            prefix_cnt[i+1] = prefix_cnt[i] + (1 if d != 0 else 0)
            if d != 0:
                prefix_x[i+1] = (prefix_x[i] * 10 + d) % MOD
            else:
                prefix_x[i+1] = prefix_x[i]
        
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = pow10[i-1] * 10 % MOD
        
        result = []
        for l, r in queries:
            digit_sum = prefix_sum[r+1] - prefix_sum[l]
            cnt = prefix_cnt[r+1] - prefix_cnt[l]
            x = (prefix_x[r+1] - prefix_x[l] * pow10[cnt]) % MOD
            ans = x * digit_sum % MOD
            result.append(ans)
        
        return result