#!usr/bin/env

from typing import List, Dict

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''
            Submission_1
            https://leetcode.com/submissions/detail/552720697/
        '''
        unique: Dict = dict().fromkeys(nums, 0)
        for num in nums:
            unique[num] = unique.get(num) + 1
        return [item[0] for item in unique.items() if item[1] > 1]


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
    print('\nTest Case: ', test, 'Result: ', start.findDuplicates(test))