#!usr/bin/env

from typing import List, Set

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
            Submission_1:
            https://leetcode.com/submissions/detail/552234956/

            for num in nums:
                if nums.count(num) > 1:
                    return num
        '''

        '''
            Submission_2:
            https://leetcode.com/submissions/detail/552234956/
        '''
        unique: Set = set(nums)
        return (sum(nums) - sum(unique)) // (len(nums) - len(unique))

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
    print('\nTest Case: ', test, 'Result: ', start.findDuplicate(test))