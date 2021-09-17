#!usr/bin/env

from typing import List, Set

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
            Submission_1:
            https://leetcode.com/submissions/detail/556647619/

            unique: Set = set(nums)
            for i in range(len(unique)+1):
                if i+1 not in unique:
                    return i+1
        '''

        '''
            Submission_2:
            https://leetcode.com/submissions/detail/556650247/
        '''
        nums = [num for num in nums if num > -1]
        if len(nums) < 1:
            return 1
        unique: Set = set(nums)
        for i in range(len(unique)):
            if i+1 not in unique:
                return i+1
        return len(unique)+1
        

print('''
    \tTest case input format
    \tSingle:
    \t\t1 2 3 4 4 5 5 6 6 3 2
    \t\tz
    \tMultiple:
    \t\t1 2 3 3 4 5 6 7 2
    \t\t2 2 2 2 2 21 2 3 12
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
    print('\nTest Case: ', test, 'Result: ',
          start.firstMissingPositive(test))