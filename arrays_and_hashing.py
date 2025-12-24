from collections import Counter, defaultdict

def has_duplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    result_dict = {}
    for letter in s:
        result_dict.get(letter, 1)


    for letter in t:
        if letter not in result_dict:
            return False
        result_dict[letter] -= 1
        if result_dict[letter] == 0:
            del result_dict[letter]

    if len(result_dict) == 0:
        return True

    return False

def is_anagram_collections(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

def two_sum(nums: list[int], target: int) -> list[int]:
    temp_dict = {}
    for i, num in enumerate(nums):
        diff = target - num

        if diff in temp_dict:
            return [temp_dict[diff], i]
        else:
            temp_dict[num] = i

    return []

def group_anagrams(strs: list[str]) -> list[list[str]]:
    result_dict = defaultdict(list)

    for word in strs:
        sorted_word = "".join(sorted(word))
        result_dict[sorted_word].append(word)

    result = []

    for key in result_dict.keys():
        result.append(result_dict[key])

    return result

def group_anagrams_2(strs: list[str]) -> list[list[str]]:
    result_dict = defaultdict(list)
    for word in strs:
        word_letter_counter = [0] * 26
        for letter in word:
            letter_index = ord(letter) - ord('a')
            word_letter_counter[letter_index] += 1
        result_dict[tuple(word_letter_counter)].append(word)
    result = []
    for key in result_dict.keys():
        result.append(result_dict[key])

    return result

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    result_dict = Counter(nums)

    freq_buckets = [[] for i in range(len(nums) + 1)]
    for key, value in result_dict.items():
        freq_buckets[value].append(key)

    print(freq_buckets)

    result = []
    for value in range(len(freq_buckets) - 1, -1, -1):
        if k == 0:
            return result
        if not freq_buckets[value]:
            continue
        for num in freq_buckets[value]:
            result.append(num)
            k = k-1
    return result

def product_except_self(nums: list[int]) -> list[int]:
    all_left_arr = [0] * len(nums)
    all_left_arr[0] = 1

    left_multiply = 1
    i = 1
    while i < len(nums):
        left_multiply *= nums[i-1]
        all_left_arr[i] = left_multiply
        i += 1

    right_multiply = 1
    i = len(nums) - 2
    while i >= 0:
        right_multiply *= nums[i+1]
        all_left_arr[i] *= right_multiply
        i -= 1

    return all_left_arr


def longest_consecutive(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0

    elements_set = set(nums)

    highest_sequence = 1

    for i in range(0, len(nums)):
        if nums[i] not in elements_set:
            continue
        current_sequence = 1
        j = nums[i] + 1
        while True:
            if j not in elements_set:
                break
            current_sequence += 1
            elements_set.remove(j)
            j += 1

        j = nums[i] - 1
        while True:
            if j not in elements_set:
                break
            current_sequence += 1
            j -= 1

        if nums[i] in elements_set:
            elements_set.remove(nums[i])

        if current_sequence > highest_sequence:
            highest_sequence = current_sequence

    return highest_sequence

def longest_consecutive_2(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0

    elements_set = set(nums)

    highest_sequence = 1

    for num in elements_set:
        is_start_of_sequence = num - 1 not in elements_set
        if not is_start_of_sequence:
            continue

        current_sequence = 1
        is_sequence_continue = num + current_sequence in elements_set
        while is_sequence_continue:
            current_sequence += 1
            is_sequence_continue = num + current_sequence in elements_set

        if current_sequence > highest_sequence:
            highest_sequence = current_sequence

    return highest_sequence

def is_valid_sudoku(board: list[list[str]]) -> bool:
    cols = defaultdict(set)
    squares = defaultdict(set)

    for i in range(0, len(board)):
        current_line = set()
        for j in range(0, len(board[i])):
            if board[i][j].isdigit():
                current_square = get_correct_square(i, j)
                if board[i][j] in cols[j] or board[i][j] in current_line or board[i][j] in squares[current_square]:
                    return False
                current_line.add(board[i][j])
                cols[j].add(board[i][j])
                squares[get_correct_square(i, j)].add(board[i][j])
                continue
            if board[i][j] == '.':
                continue
            return False
    return True

def get_correct_square(i: int, j: int):
    return i // 3, j // 3

def encode(strs: list[str]) -> str:
    result = ""
    for string in strs:
        result += f"%{len(string)}#{string}"
    return f"{result}"

def decode(s: str) -> list[str]:
    result = []
    if len(s) > 0:
        i = 0
        while i < len(s):
            if s[i] == '#':
                z = i-1
                next_word_str_len = ''
                while z >= 0 and s[z] != '%':
                    next_word_str_len += s[z]
                    z -= 1
                next_word_len = int(next_word_str_len[::-1])
                start = i+1
                end = i+1+next_word_len
                i += next_word_len
                result.append(s[start:end])
            i += 1
    return result


print(encode(["neet","code","love","you"]))
print(decode(encode(["#", "a"])))

# print(is_valid_sudoku([["1","2",".",".","3",".",".",".","."],
#                      ["4",".",".","5",".",".",".",".","."],
#                      [".","9","8",".",".",".",".",".","3"],
#                      ["5",".",".",".","6",".",".",".","4"],
#                      [".",".",".","8",".","3",".",".","5"],
#                      ["7",".",".",".","2",".",".",".","6"],
#                      [".",".",".",".",".",".","2",".","."],
#                      [".",".",".","4","1","9",".",".","8"],
#                      [".",".",".",".","8",".",".","7","9"]]))
# print(longest_consecutive_2([2,20,4,10,3,4,5]))
# print(product_except_self([1,2,4,6]))
# print(group_anagrams(strs=["act","pots","tops","cat","stop","hat"]))
# print(group_anagrams_2(strs=["act","pots","tops","cat","stop","hat"]))
# print(top_k_frequent([1,2], 2))