class Solution:
    # def canJump(self, nums: list[int]) -> bool:
    #     cur = 0
    #     while len(nums) - 1 > cur and nums[cur] != 0:
    #         best_jump = self.get_best_jump(nums, cur, nums[cur])
    #         cur += best_jump
    #     if len(nums) - 1 <= cur:
    #         return True
    #     return False
    #
    # def get_best_jump(self, nums, cur_index, jump_size) -> int:
    #     best_jump = 0
    #     for i in range(cur_index,cur_index+jump_size):
    #         best_jump = max(best_jump, i - cur_index + nums[i])
    #     return best_jump

    # def canJump(self, nums: list[int]) -> bool:
    #     power_reserve = nums[0]
    #     for i in nums[0:-1]:
    #         power_reserve -= 1
    #         power_reserve = max(i, power_reserve)
    #         if power_reserve == 0:
    #             return False
    #     return True

    def canJump(self, nums: list[int]) -> bool:
        goal = 0

        for i, jump in enumerate(nums):

            if i > goal:
                return False

            goal = max(goal, i + jump)

        return True

    def jump(self, nums: list[int]) -> int:
        current_jumps = 0

        i = 0
        while i < len(nums) - 1:
            current_best_jump = self.best_jump(nums, nums[i], i)
            i = current_best_jump
            current_jumps += 1
            pass
        return current_jumps

    def best_jump(self, nums, jump_size, start_index):
        abs_reach = -1
        current_index = start_index
        max_index = start_index + 1
        if current_index + jump_size >= len(nums) - 1:
            return len(nums) - 1
        while jump_size:
            jump_size -= 1
            current_index += 1
            if abs_reach < nums[current_index] + current_index:
                abs_reach = nums[current_index] + current_index
                max_index = current_index
        return max_index
sol = Solution()
print(sol.jump(nums=[2,1,2,1,0]))