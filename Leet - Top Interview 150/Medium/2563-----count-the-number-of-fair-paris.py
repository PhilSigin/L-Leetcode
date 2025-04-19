"""

2563. Count the Number of Fair Pairs
https://leetcode.com/problems/count-the-number-of-fair-pairs/

Given a 0-indexed integer array nums of size n and two integers lower and upper, return the number of fair pairs.

A pair (i, j) is fair if:
    0 <= i < j < n, and
    lower <= nums[i] + nums[j] <= upper

Example 1:
Input: nums = [0,1,7,4,4,5], lower = 3, upper = 6
Output: 6
Explanation: There are 6 fair pairs: (0,3), (0,4), (0,5), (1,3), (1,4), and (1,5).

Example 2:
Input: nums = [1,7,9,2,5], lower = 11, upper = 11
Output: 1
Explanation: There is a single fair pair: (2,3).

"""

# My slowest Solution (THEY DO NOT ACCEPT IT)

def countFairPairs1( nums: List[int], lower: int, upper: int) -> int:

    """ This solution works, but is too slow!"""
    fair = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j]) >= lower and (nums[i] + nums[j]) <= upper:
                fair +=1
    return fair


# This onr works, too but too slow too (THEY DO NOT ACCEPT IT)
def countFairPairs2( nums: List[int], lower: int, upper: int) -> int:

    import bisect
    from collections import Counter

    fair = 0

    """ Оптимизировано в одну строчку - быстрый Counter -> dict """
    numbers_dict = dict(sorted(Counter(nums).items()))
    print(dict(numbers_dict))

    all_keys = list (numbers_dict.items())
    keys_only = [k for k, _ in all_keys]

    for i_key, i_value in all_keys:
        print (i_key, i_value)

        min_j = max(lower-i_key, i_key)
        max_j = upper - i_key

        # Находим индексы границ
        left_idx = bisect.bisect_left(keys_only, min_j)
        right_idx = bisect.bisect_right(keys_only, max_j)

        # Получаем нужный срез
        valid_j_keys = keys_only[left_idx:right_idx]
        print(valid_j_keys)


        if valid_j_keys:
            print("VALID", valid_j_keys[0])
            if valid_j_keys[0] == i_key:
                fair += i_value * (i_value - 1) // 2  # сочетания из count_a по 2 ***********
                del valid_j_keys[0]
            if valid_j_keys:
                sum_j_values = sum(numbers_dict[j_key] for j_key in valid_j_keys)
                fair += i_value * sum_j_values

    return fair


# AI VERSION, WORKS, ACCEPTED

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        fair = 0
        n = len(nums)

        for i in range(n):
            left = bisect_left(nums, lower - nums[i], i + 1, n)
            right = bisect_right(nums, upper - nums[i], i + 1, n)
            fair += right - left

        return fair


