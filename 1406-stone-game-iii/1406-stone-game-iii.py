from functools import lru_cache

class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + stoneValue[i]

        @lru_cache(maxsize=None)
        def dp(i):
            # returns max score current player can get from index i onward
            if i >= n:
                return 0
            best = float('-inf')
            for take in range(1, 4):
                if i + take > n:
                    break
                # current player takes stoneValue[i..i+take-1]
                # opponent plays optimally from i+take
                taken = suffix[i] - suffix[i + take]
                opponent = dp(i + take)
                # remaining after opponent = suffix[i+take] - opponent
                my_score = taken + (suffix[i + take] - opponent)
                best = max(best, my_score)
            return best

        alice = dp(0)
        bob = suffix[0] - alice

        if alice > bob:
            return "Alice"
        elif bob > alice:
            return "Bob"
        else:
            return "Tie"