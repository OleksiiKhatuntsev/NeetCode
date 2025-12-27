from re import search


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

sol = Solution()
print(sol.search([-1,0,5], -1))
print(sol.search_matrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 41))
print(sol.min_eating_speed([1,4,3,2],8))