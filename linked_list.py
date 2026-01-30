from collections import defaultdict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} {self.next}"

    def __repr__(self):
        return f"{self.val} {self.next}"

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# Definition for a Node.
class RandomNode:
    def __init__(self, x: int, next: 'RandomNode' = None, random: 'RandomNode' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class TwoLinkedNode(ListNode):
    def __init__(self, val=0, next=None, prev=None):
        super.__init__(val, next)
        self.prev = prev

class Solution:
    def reverseList(self, head: ListNode):
        cur = head
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        #tail = list1 or list2
        return dummy.next

    def hasCycle(self, head: ListNode) -> bool:
        index_short = head
        index_long = head
        while index_long and index_long.next:
            index_long = index_long.next.next
            index_short = index_short.next
            if index_short == index_long:
                return True
        return False

    def reorderList(self, head: ListNode) -> None:
        slow = head
        fast = head
        prev_reverse = None
        counter = 1
        while fast and fast.next:
            fast = fast.next.next
            prev_reverse = slow
            slow = slow.next
            counter += 1

        cur = slow
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        slow.next = None
        right = prev
        left = head

        while right:
            left_cache = left.next
            left.next = right
            right = left_cache
            left = left.next

        print(head)

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        counter = 0
        cur = head
        while cur:
            counter += 1
            cur = cur.next

        if counter < n:
            return head
        if counter == n:
            return head.next
        node_to_remove = counter - n

        prev = None
        cur = head
        while node_to_remove > 0:
            node_to_remove -= 1
            prev = cur
            cur = cur.next

        prev.next = cur.next
        return head

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        counter = n
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        while counter > 0:
            counter -= 1
            cur = cur.next
        to_remove = dummy
        prev = dummy
        while cur:
            cur = cur.next
            prev = to_remove
            to_remove = to_remove.next

        prev.next = to_remove.next

        return dummy.next

    # def copyRandomList(self, head: RandomNode) -> RandomNode:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first_cur = l1
        second_cur = l2

        result_dummy = ListNode()
        res_cur = result_dummy

        is_transferred = False

        while first_cur or second_cur:
            res_cur.next = ListNode()
            res_cur = res_cur.next

            s = int(is_transferred)
            if first_cur:
                s += first_cur.val
            if second_cur:
                s += second_cur.val
            res_cur.val += s % 10

            if s >= 10:
                is_transferred = True
            else:
                is_transferred = False

            if first_cur:
                first_cur = first_cur.next
            if second_cur:
                second_cur = second_cur.next

        if is_transferred:
            res_cur.next = ListNode(val=1)

        return result_dummy.next

    def findDuplicate(self, nums: list[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

    def copyRandomList(self, head: Node) -> Node:
        old_to_new = {None: None}
        cur = head
        while cur:
            copy = Node(cur.val)
            old_to_new[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            old_to_new[cur].next = old_to_new[cur.next]
            old_to_new[cur].random = old_to_new[cur.random]
            cur = cur.next
        return old_to_new[head]





class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_values = defaultdict(int)
        self.linked = ListNode()
        self.last = ListNode()
        self.head = ListNode()
        self.head.next = self.last

    def get(self, key: int) -> int:
        return self.key_values[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            self.key_values.pop(self.head.val)
            self.head = self.head.next

        self.last.next = ListNode()
        self.last.next.val = key
        self.last = self.last.next


        self.key_values[key] = value



sol = Solution()
# node = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
# node1 = ListNode(1, ListNode(3, ListNode(5)))
# node2 = ListNode(1, ListNode(2, ListNode(4)))
# cycled_node = ListNode(3, ListNode(4))
# cycled_node.next = cycled_node
# node3 = ListNode(1, ListNode(2, cycled_node))
# print(sol.reverseList(node))
# print(sol.mergeTwoLists(node1, node2))
# print(sol.hasCycle(node3))
# print(sol.hasCycle(node1))

# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(1)
#
# # Связываем их стрелочками (next)
# node1.next = node2
# node2.next = node3
# node3.next = None  # ВАЖНО: Последний указывает в пустоту. Это и есть index = -1
#
# # Запускаем проверку
# result1 = sol.hasCycle(node1)
# print(f"Ожидается: False")
# print(f"Твой результат: {result1}")
# print("-" * 20)
node1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
# print(sol.reorderList(node1))
# print(sol.reorderList(ListNode(1)))
# print(sol.removeNthFromEnd(node1, 6))
# print(sol.removeNthFromEnd2(node1, 6))

nums = [1,2,3,2,2]
nums1 = [1,2,3,4,4]
nums2=[1,3,4,2,2]
print(sol.findDuplicate(nums))
print(sol.findDuplicate(nums1))
print(sol.findDuplicate(nums2))

# 2. Помощники (чтобы не создавать узлы вручную)
# def create_list(nums):
#     """Превращает список Python [2, 4, 3] в Linked List 2->4->3"""
#     dummy = ListNode()
#     curr = dummy
#     for n in nums:
#         curr.next = ListNode(n)
#         curr = curr.next
#     return dummy.next
#
#
# def print_list(node):
#     """Красиво печатает Linked List"""
#     res = []
#     while node:
#         res.append(str(node.val))
#         node = node.next
#     return " -> ".join(res) if res else "Empty"
#
#
# # ==========================================
# # 4. ТЕСТЫ
# # ==========================================
# sol = Solution()
#
# test_cases = [
#     {
#         "name": "Тест 1: Стандартный (LeetCode Пример)",
#         "l1": [2, 4, 3],  # 342
#         "l2": [5, 6, 4],  # 465
#         "expected": "7 -> 0 -> 8"  # 807
#     },
#     {
#         "name": "Тест 2: Сложение с нулем",
#         "l1": [0],
#         "l2": [0],
#         "expected": "0"
#     },
#     {
#         "name": "Тест 3: Разная длина + Перенос в середине",
#         "l1": [9, 9, 9, 9, 9, 9, 9],  # 9999999
#         "l2": [9, 9, 9, 9],  # 9999
#         "expected": "8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1"  # 10009998
#     },
#     {
#         "name": "Тест 4: Перенос создает новый узел в конце (Важный!)",
#         "l1": [5],
#         "l2": [5],
#         "expected": "0 -> 1"  # 10
#     },
#     {
#         "name": "Тест 5: Каскад девяток (99 + 1)",
#         "l1": [1],
#         "l2": [9, 9],  # 99
#         "expected": "0 -> 0 -> 1"  # 100
#     }
# ]
#
# print(f"{'=' * 20} ЗАПУСК ТЕСТОВ {'=' * 20}")
#
# for test in test_cases:
#     print(f"\n🔹 {test['name']}")
#
#     # Создаем списки
#     list1 = create_list(test["l1"])
#     list2 = create_list(test["l2"])
#
#     # Запускаем твое решение
#     try:
#         result_node = sol.addTwoNumbers(list1, list2)
#         result_str = print_list(result_node)
#
#         print(f"   Вход l1: {test['l1']}")
#         print(f"   Вход l2: {test['l2']}")
#         print(f"   Ожидание: {test['expected']}")
#         print(f"   Результат: {result_str}")
#
#         # Простая проверка строки
#         if result_str == test['expected']:
#             print("   ✅ PASSED")
#         else:
#             print("   ❌ FAILED")
#
#     except Exception as e:
#         print(f"   🔥 ОШИБКА ИСПОЛНЕНИЯ: {e}")
#
# print(f"\n{'=' * 20} КОНЕЦ {'=' * 20}")