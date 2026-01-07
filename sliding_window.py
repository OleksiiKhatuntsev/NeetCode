from collections import defaultdict

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                res = max(res, prices[right] - prices[left])
            right += 1
        return res

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        unique_set = set()
        result = 1
        for right in range(0, len(s)):
            while s[right] in unique_set:
                unique_set.remove(s[left])
                left += 1

            unique_set.add(s[right])

            result = max(result, right - left + 1)
        return result

    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        if len(s) <= k:
            return len(s)
        left = 0
        current_window_repeats = defaultdict(int)
        current_window_trend_letter = ''
        result = k + 1
        for right in range(0, len(s)):
            current_window_repeats[s[right]] += 1
            current_window_trend_letter = current_window_trend_letter if current_window_repeats[s[right]] < current_window_repeats[current_window_trend_letter] else s[right]
            if right - left + 1 > k + current_window_repeats[current_window_trend_letter]:
                current_window_repeats[s[left]] -= 1
                left += 1
            result = max(right - left + 1, result)
        return result

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        first_string_dict = defaultdict(int)
        second_string_dict = defaultdict(int)
        left_num = 0
        for i in s1:
            first_string_dict[i] += 1
        for num_right, right in enumerate(s2):
            if num_right - left_num >= len(s1):
                second_string_dict[s2[left_num]] -= 1
                if second_string_dict[s2[left_num]] == 0:
                    second_string_dict.pop(s2[left_num])
                left_num += 1
            second_string_dict[right] += 1
            if first_string_dict == second_string_dict:
                return True

        return False

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        left_num = 0
        t_count = [0] * 128
        result = ""
        t_dict = defaultdict(int)
        for char in t:
            t_count[ord(char)] += 1
            t_dict[char] += 1
        s_count = [0] * 128
        for right_num, right in enumerate(s):
            s_count, right, result, left_num, right_num = self.right_letter_iteration(t_dict, t_count, s_count, s, right, result, left_num, right_num)
        return result


    def is_substring_min_window(self, t_dict: defaultdict[str, int], s_count: list[int]):
        keys = t_dict.keys()
        for i in keys:
            if t_dict[i] > s_count[ord(i)]:
                return False
        return True

    def right_letter_iteration(self, t_dict: defaultdict[str, int], t_count: list[int], s_count: list[int], s: str, right: str, result: str, left_num: int, right_num: int):
        index = ord(right)
        if t_count[index] > 0:
            s_count[index] += 1
            while self.is_substring_min_window(t_dict, s_count):
                result = result if 0 < len(result) < len(s[left_num:right_num + 1]) else s[
                    left_num:right_num + 1]
                left_index = ord(s[left_num])
                if not t_count[left_index] == 0:
                    s_count[left_index] -= 1
                    if s_count[left_index] == 0:
                        left_num += 1
                        break
                left_num += 1
        while left_num < right_num < len(s) and s[left_num] not in t_dict:
            left_num += 1

        return s_count, right, result, left_num, right_num



sol = Solution()
# print(sol.maxProfit([10,1,5,6,7,1]))
# print(sol.lengthOfLongestSubstring("zxyzxyz"))
# print(sol.lengthOfLongestSubstring("xxxx"))
# print(sol.lengthOfLongestSubstring("xy"))
# print(sol.lengthOfLongestSubstring("pwwkew"))
# print(sol.lengthOfLongestSubstring("dvdf"))
# print(sol.lengthOfLongestSubstring("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcdefghijk"))
# print(sol.characterReplacement(s = "XYYX", k = 2))
# print(sol.characterReplacement(s = "AAABABB", k = 1))
# print(sol.checkInclusion(s1 = "abc", s2 = "lecabee"))
# print(sol.checkInclusion(s1 = "abc", s2 = "lecaabee"))
# print(sol.checkInclusion(s1="ab", s2="eidboaoo"))
# print(sol.checkInclusion(s1="adc", s2="dcda"))
print(sol.minWindow(s = "OUZODYXAZV", t = "XYZ"))
print(sol.minWindow(s = "XYZ", t = "XYZ"))
print(sol.minWindow(s = "A", t="A"))
print(sol.minWindow(s = "aa", t="aa"))
print(sol.minWindow(s="ADOBECODEBANC", t="ABC"))
print(sol.minWindow(s="aaaaaaaaaaaabbbbbcdd", t="abcdd"))
print(sol.minWindow(s="baAaABabBba", t="AbbB"))
