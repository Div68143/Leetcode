from collections import Counter

class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        cnt = Counter(nums)
        ans = 1

        for x in cnt:
            if x == 1:
                c = cnt[1]
                ans = max(ans, c if c % 2 == 1 else c - 1)
                continue

            # Build chain of levels where count >= 2
            chain = []
            cur = x
            while cur in cnt and cnt[cur] >= 2:
                chain.append(cur)
                cur = cur * cur
                if cur > 10**18:  # prevent overflow
                    break

            if not chain:
                # x exists but count < 2, can only use as lone center
                ans = max(ans, 1)
                continue

            # The pattern MUST have exactly one center at the top.
            # Every level below center contributes 2 elements (left + right mirror).
            # So: length = (number of pair levels) * 2 + 1

            # Option A: center comes from NEXT level beyond chain
            if cur in cnt and cnt[cur] >= 1:
                length = len(chain) * 2 + 1  # all chain levels are pairs
            else:
                # Option B: topmost chain level becomes center (can't be a pair)
                length = (len(chain) - 1) * 2 + 1

            ans = max(ans, length)

        return ans