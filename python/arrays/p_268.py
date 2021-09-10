#!/usr/bin/env
from typing import List, Set


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ''' 
            Submission 1:
            https://leetcode.com/submissions/detail/551598823/
        '''
        for number in range(len(nums)+1):
            if not nums.__contains__(number):
                return number

        '''
            Submission 2:
            cur_sum: int = sum(nums)
            sum_value: int = sum(list(range(len(nums)+1)))
            return sum_value - cur_sum
        '''


print('''
    \tTest case input format
    \tSingle:
    \t\t1 2 3 4 5 6 7
    \t\tz
    \tMultiple:
    \t\t1 2
    \t\t2 21 2 3
    \t\tz
    \n\tPress 'z' key to start test run
    \n\n\nEnter the Test cases:
''')

test_cases = []
while True:
    try:
        case = [int(item) for item in input().split()]
        test_cases.append(case)
    except ValueError:
        break
start: Solution = Solution()
for test in test_cases:
    print('\nTest Case: ', test, 'Result: ', start.missingNumber(test))
