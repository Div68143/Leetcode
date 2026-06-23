class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        # dp[j] = number of ways ending with value j (0-indexed)
        dp = [1] * m

        # True => next relation is "up" (<), False => "down" (>)
        up = True

        for _ in range(1, n):
            ndp = [0] * m

            if up:
                prefix = 0
                for j in range(m):
                    ndp[j] = prefix
                    prefix = (prefix + dp[j]) % MOD
            else:
                suffix = 0
                for j in range(m - 1, -1, -1):
                    ndp[j] = suffix
                    suffix = (suffix + dp[j]) % MOD

            dp = ndp
            up = not up

        # Starting with "up"
        ans = sum(dp) % MOD

        # By symmetry, starting with "down" gives the same count
        return (2 * ans) % MOD