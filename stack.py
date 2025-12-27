class Solution:
    def is_valid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        parent_dict = {'}': '{', ')': '(', ']': '['}
        stack = []
        for sym in s:
            if sym in parent_dict:
                if not stack or stack.pop() != parent_dict[sym]:
                    return False
            else:
                stack.append(sym)
        return not stack


class MinStack:
    def __init__(self):
        self.internal_array = []

    def push(self, val: int) -> None:
        if not self.internal_array:
            self.internal_array.append((val, val))
        else:
            current_min = self.internal_array[-1][1]
            if val < current_min:
                self.internal_array.append((val, val))
            else:
                self.internal_array.append((val, current_min))

        print(self.internal_array)

    def pop(self) -> None:
        self.internal_array.pop()

    def top(self) -> int:
        return self.internal_array[-1][0]

    def get_min(self) -> int:
        return self.internal_array[-1][1]

def evalRPN(tokens: list[str]) -> int:
    operation_stack = []
    result = 0
    for sym in tokens:
        if sym not in ('+', '-', '*', '/'):
            operation_stack.append(int(sym))
        else:
            if sym == '+':
                result = operation_stack.pop() + operation_stack.pop()
            elif sym == '-':
                b, a = operation_stack.pop(), operation_stack.pop()
                result = a - b
            elif sym == '*':
                result = operation_stack.pop() * operation_stack.pop()
            elif sym == '/':
                b, a = operation_stack.pop(), operation_stack.pop()
                result = int(a / b)
            operation_stack.append(result)
    return operation_stack.pop()

def daily_temperatures(temperatures: list[int]) -> list[int]:
    result = [0] * (len(temperatures))
    temp_stack = []
    for i, el in enumerate(temperatures):
        if not temp_stack:
            temp_stack.append((el, i))
            continue
        while temp_stack and temp_stack[-1][0] < el:
            pop_element = temp_stack.pop()
            result[pop_element[1]] = i - pop_element[1]
        temp_stack.append((el, i))
    return result

def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    tuples = list(zip(position, speed))
    sorted_tuples = sorted(tuples)
    print(sorted_tuples)
    result = 0
    steps_to_reach_target = 0
    while sorted_tuples:
        current = sorted_tuples.pop()
        current_steps_to_reach_target = get_steps_to_target(target, current)
        if current_steps_to_reach_target > steps_to_reach_target:
            result += 1
            steps_to_reach_target = current_steps_to_reach_target
    return result

def get_steps_to_target(target, position: (int, int))-> float:
    time = (target - position[0]) / position[1]
    return time

def largestRectangleArea(heights: list[int]) -> int:
  pass

print(largestRectangleArea([7,1,7,2,2,4]))
# print(daily_temperatures([30,38,30,36,35,40,28]))
# print(car_fleet(17, [8,12,16,11,7], [6,9,10,9,7]))
# print(evalRPN(["3","-4","+"]))
# ["MinStack", "push", -1, "push", 3, "push", -4, "getMin", "pop", "getMin", "top"]
# min_stack = MinStack()
# min_stack.push(-1)
# min_stack.push(3)
# min_stack.push(-4)
# print(min_stack.get_min())
# print(min_stack.pop())
# print(min_stack.get_min())
# print(min_stack.top())
# min_stack.push(-4)
# # min_stack.push(111)
# print(min_stack.get_min())
# sol = Solution()
# print(sol.is_valid("([{}])"))
# print(sol.is_valid("({[}})"))