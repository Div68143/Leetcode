class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        size = 2 * n + 2
        bit = [0] * (size + 1)

        def update(i):
            i += 1
            while i <= size:
                bit[i] += 1
                i += i & (-i)

        def query(i):
            i += 1
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s

        offset = n
        count = 0
        prefix = 0

        update(prefix + offset)

        for num in nums:
            prefix += 1 if num == target else -1
            p_idx = prefix + offset

            if p_idx > 0:
                count += query(p_idx - 1)

            update(p_idx)

        return count