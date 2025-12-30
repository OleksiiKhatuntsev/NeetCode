from collections import defaultdict


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        left_i = 0
        right_i = len(matrix) - 1
        while left_i <= right_i:
            mid = (left_i + right_i) // 2
            if matrix[mid][0] <= target <= matrix[mid][len(matrix[mid]) - 1]:
                return self.search(matrix[mid], target) != -1
            elif matrix[mid][0] > target:
                right_i = mid - 1
            else:
                left_i = mid + 1
        return False

    def min_eating_speed(self, piles: list[int], h: int) -> int: # with hint
        max_el = max(piles)
        if len(piles) >= h:
            return max_el
        else:
            left = 1
            right = max_el
            res = right
            while left <= right:
                k = (left + right) // 2
                temp_attempts = 0
                for pile in piles:
                    temp_attempts += (pile + k - 1) // k
                if temp_attempts <= h:
                    right = k - 1
                    res = k
                else:
                    left = k + 1
            return res

    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            index = (right + left) // 2
            if nums[index] > nums[right]:
                left = index + 1
            else:
                right = index

        return nums[left]

    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            index = (right + left) // 2
            if nums[index] == target:
                return index
            if self.is_sorted_side(nums[index], nums[right]):
                if nums[index] < target <= nums[right]:
                    left = index + 1
                else:
                    right = index - 1
            else:
                if nums[left] <= target < nums[index]:
                    right = index - 1
                else:
                    left = index + 1

        return -1

    def is_sorted_side(self, left, right):
        return left < right


class TimeMap:
    def __init__(self):
        self.key_timestamp_value_dict = defaultdict(list[tuple])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_timestamp_value_dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_timestamp_value_dict:
            return ""
        value = self.key_timestamp_value_dict[key]
        if self.key_timestamp_value_dict[key][0][0] > timestamp:
            return ""
        left = 0
        right = len(self.key_timestamp_value_dict[key]) - 1
        res = value[left][1]
        while left <= right:
            index = (left + right) // 2
            if value[index][0] <= timestamp:
                res = value[index][1]
                left = index + 1
            else:
                right = index - 1
        return res
# sol = Solution()
# print(sol.search([-1,0,5], -1))
# print(sol.search_matrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 41))
# print(sol.min_eating_speed([1,4,3,2],8))
# print(sol.findMin([5,1,2,3,4]))
# print(sol.search([3,4,5,6,1,2], 1))
timeMap = TimeMap()
timeMap.set("alice", "happy", 1)
timeMap.get("alice", 1)
timeMap.get("alice", 2)
timeMap.set("alice", "sad", 3)
print(timeMap.get("alice", 3))

#["TimeMap", "set", ["test", "one", 10], "set", ["test", "two", 20], "set", ["test", "three", 30], "get", ["test", 15], "get", ["test", 25], "get", ["test", 35]]
timeMap.set("test", "one", 10)
timeMap.set("test", "two", 20)
timeMap.set("test", "three", 30)
print(timeMap.get("test", 15))
print(timeMap.get("test", 25))
print(timeMap.get("test", 35))
["TimeMap", "set", ["multi", "A", 1], "set", ["multi", "B", 2], "set", ["multi", "C", 3], "set", ["multi", "D", 4], "get", ["multi", 1], "get", ["multi", 2], "get", ["multi", 3], "get", ["multi", 4]]
timeMap.set("multi", "A", 1)
timeMap.set("multi", "B", 2)
timeMap.set("multi", "C", 3)
timeMap.set("multi", "D", 4)
print(timeMap.get("multi", 1))
print(timeMap.get("multi", 2))
print(timeMap.get("multi", 3))
print(timeMap.get("multi", 4))