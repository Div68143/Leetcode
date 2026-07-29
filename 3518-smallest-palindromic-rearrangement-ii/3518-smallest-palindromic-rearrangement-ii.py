from math import log

class Solution:
    LIM = 10**6 + 1

    def ways(self, cnt, rem, log_fact):
        if rem == 0:
            return 1

        # Use logarithms to quickly determine if answer exceeds LIM
        val = log_fact[rem]
        for x in cnt:
            val -= log_fact[x]

        if val > log(self.LIM):
            return self.LIM

        # Exact multinomial coefficient (capped at LIM)
        ans = 1
        left = rem

        for take in cnt:
            if take == 0:
                continue

            cur = 1
            for i in range(1, take + 1):
                cur = cur * (left - take + i) // i
                if cur > self.LIM:
                    cur = self.LIM

            ans *= cur
            if ans > self.LIM:
                ans = self.LIM

            left -= take

        return min(ans, self.LIM)

    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        half = [0] * 26
        mid = ""
        m = 0

        for i in range(26):
            if freq[i] % 2:
                mid = chr(i + ord('a'))
            half[i] = freq[i] // 2
            m += half[i]

        # Precompute log factorials
        log_fact = [0.0] * (m + 1)
        for i in range(1, m + 1):
            log_fact[i] = log_fact[i - 1] + log(i)

        # Check if k is valid
        if self.ways(half, m, log_fact) < k:
            return ""

        left = []

        for pos in range(m):
            for c in range(26):
                if half[c] == 0:
                    continue

                half[c] -= 1
                cnt = self.ways(half, m - pos - 1, log_fact)

                if cnt >= k:
                    left.append(chr(c + ord('a')))
                    break
                else:
                    k -= cnt
                    half[c] += 1

        left = "".join(left)
        return left + mid + left[::-1]