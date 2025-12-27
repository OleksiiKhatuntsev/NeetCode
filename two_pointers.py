from collections import Counter, defaultdict

class Solution:
    def is_palindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while not s[left].isalnum():
                left += 1
                if left >= len(s):
                    return True
            while not s[right].isalnum():
                right -=1
                if right < 0:
                    return True
            if not (s[left].lower() == s[right].lower()):
                return False
            left += 1
            right -= 1

        return True

    def two_sum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

    def three_sum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        result = []
        prev_element = None
        for i in range (0, len(nums) - 2):
            if prev_element == nums[i]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[left] + nums[right] + nums[i]
                if s < 0:
                    left += 1
                    continue
                elif s > 0:
                    right -= 1
                    continue
                else:
                    result.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
            prev_element = nums[i]
        return result

    def max_area(self, heights: list[int]) -> int:
        current_max = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            current_area = (right - left) * min(heights[right], heights[left])
            if current_area > current_max:
                current_max = current_area
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return current_max

    def trap(self, heights: list[int]) -> int:
        s = 0
        left_max = 0
        right_max = 0
        left = 0
        right = len(heights) - 1
        while left <= right:
            if left_max < heights[left]:
                left_max = heights[left]
            if right_max < heights[right]:
                right_max = heights[right]
            if left_max < right_max:
                s += left_max - heights[left]
                left += 1
            else:
                s += right_max - heights[right]
                right -= 1

        return s


solution = Solution()
# print(solution.max_area([1,7,2,5,12,3,500,500,7,8,4,7,3,6]))
print(solution.trap([0,2,0,3,1,0,1,3,2,1]))
# print(solution.is_palindrome(".,"))
# print(solution.two_sum([1,2,3,4], 3))
# print(solution.two_sum([2, 3, 5, 10, 15, 50, 75, 100], 65))
# print(solution.three_sum([-1,0,1,2,-1,-4]))