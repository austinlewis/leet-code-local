#!usr/bin/env

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
            Submission:
            https://leetcode.com/submissions/detail/551703808/
        '''
        counter: int = 0
        while(counter != len(nums)):
            check_num: int = nums.pop(counter)
            if nums.count(check_num) != 1:
                return check_num
            nums.remove(check_num)

        '''
            Above method loops through all methods time-complexity is more,
            replacing extra count-condition with try-except for remove cut execution-time by half,
            A better approach to use Bitwise-XOR, i.e., result ^= nums[i] : twice appearning digits cancel out each other while leaving the one time appearing digit in result
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
    print('\nTest Case: ', test, 'Result: ', start.singleNumber(test))
