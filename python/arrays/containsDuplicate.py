#!/usr/bin/env
from typing import List, Set


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ''' 
            Submission:
            https://leetcode.com/submissions/detail/550779729/
        '''
        if(len(set(nums)) != len(nums)):
            return True
        else:
            return False


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

testCases = []
while True:
    try:
        case = [int(item) for item in input().split()]
        testCases.append(case)
    except ValueError:
        break
start: Solution = Solution()
for test in testCases:
    print('\nTest Case: ', test,'Result: ',start.containsDuplicate(test))
