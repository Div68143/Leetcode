from bisect import bisect_right, bisect_left

class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[int]:
        order = sorted(range(n), key=lambda i: nums[i])
        sv = [nums[i] for i in order]

        pos = [0] * n
        for p, orig in enumerate(order):
            pos[orig] = p

        rgt = [bisect_right(sv, sv[p] + maxDiff) - 1 for p in range(n)]
        lft = [bisect_left(sv,  sv[p] - maxDiff)     for p in range(n)]

        LOG = 17
        R = [rgt[:]]
        L = [lft[:]]
        for k in range(1, LOG):
            Rk = [R[k-1][R[k-1][p]] for p in range(n)]
            Lk = [L[k-1][L[k-1][p]] for p in range(n)]
            R.append(Rk)
            L.append(Lk)

        def solve(u, v):
            pu, pv = pos[u], pos[v]
            if pu == pv:
                return 0
            if pu > pv:
                pu, pv = pv, pu
            if rgt[pu] == pu:
                return -1

            cur = pu
            hops = 0
            for k in range(LOG-1, -1, -1):
                nxt = R[k][cur]
                if nxt < pv:
                    cur = nxt
                    hops += (1 << k)

            if R[0][cur] >= pv:
                return hops + 1
            return -1

        return [solve(u, v) for u, v in queries]