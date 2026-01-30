import heapq
import math
from collections import defaultdict


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        heapq.heapify(nums)
        self.k = k
        self.heap = nums
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]

    def lastStoneWeight(self, stones: list[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        if len(stones) == 1:
            return stones[0]
        if len(stones) == 0:
            return 0
        while len(stones) >= 2:
            res_stone = -(abs(heapq.heappop(stones)) - abs(heapq.heappop(stones)))
            if res_stone != 0:
                heapq.heappush(stones, res_stone)
            if len(stones) == 1:
                return -stones[0]
            if len(stones) == 0:
                return 0

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        res = []
        points_dict = defaultdict(list[list[int]])
        heapq.heapify(res)
        for x in points:
            distance = -math.sqrt(x[0] * x[0] + x[1] * x[1])
            heapq.heappush(res, distance)
            if distance in points_dict:
                points_dict[distance].append(x)
            else:
                points_dict[distance] = [x]
            if len(res) > k:
                dist = res[0]
                if len(points_dict[dist]) > 1:
                    points_dict[dist].pop()
                else:
                    heapq.heappop(res)
                    points_dict.pop(dist)
        res_arr = []
        for i in points_dict.keys():
            for el in points_dict[i]:
                res_arr.append(el)
        return res_arr

sol = Solution()
print(sol.kClosest(points = [[0,2],[2,2]], k = 1))
print(sol.kClosest(points = [[0,2],[2,0],[2,2]], k = 2))
print(sol.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2))