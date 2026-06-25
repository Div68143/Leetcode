class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + (1 if nums[i] == target else -1)
        
        count = 0
        for l in range(n):
            for r in range(l, n):
                if prefix[r+1] > prefix[l]:
                    count += 1
        
        return count