#!/usr/bin/env
from typing import List, Set


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ''' 
            Submission:
            https://leetcode.com/submissions/detail/551598823/
        '''
        for number in range(len(nums)+1):
            if not nums.__contains__(number):
                return number
            
        '''
            Observations:
            Above method loops through all values time-complexity is more,
            A better approach was to calculate sum of given list and then calculate actual sum using n*(n+1)/2
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
