import heapq
import math
import queue
from collections import defaultdict, deque


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

    def leastInterval(self, tasks: list[str], n: int) -> int:
        heap = []
        dict_task = defaultdict(int)
        for task in tasks:
            dict_task[task] += 1

        for k in dict_task.keys():
            heapq.heappush(heap, (-dict_task[k], k))

        time = 0
        q = deque()
        while len(heap) > 0 or len(q) > 0:
            if len(q) > 0 and q[0][1] == time:
                heapq.heappush(heap, q[0][0])
                q.popleft()
            time += 1
            if len(heap) > 0:
                el = heapq.heappop(heap)
                new_el = (el[0] + 1, el[1])
                if new_el[0] < 0:
                    q.append((new_el, time + n))
        return time


sol = Solution()
# print(sol.kClosest(points = [[0,2],[2,2]], k = 1))
# print(sol.kClosest(points = [[0,2],[2,0],[2,2]], k = 2))
# print(sol.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2))
# print(sol.leastInterval(tasks = ["X","X", "Y","Y"], n = 2))
print(sol.leastInterval(tasks = ["A","A","A","B","C"], n = 3))