class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        max_cost = max(costs)
        count = [0] * (max_cost + 1)
        for c in costs:
            count[c] += 1

        bars = 0
        for cost in range(1, max_cost + 1):
            if count[cost] == 0:
                continue
            num_afford = min(count[cost], coins // cost)
            bars += num_afford
            coins -= num_afford * cost
            if coins == 0:
                break

        return bars