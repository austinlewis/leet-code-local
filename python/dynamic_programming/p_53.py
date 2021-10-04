#usr/bin/activate

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
            Submission_1: 
            https://leetcode.com/submissions/detail/565805932/
        '''
        maxSum: int = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1]+nums[i], nums[i])
            maxSum = max(maxSum, nums[i])
        return maxSum


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
    print('\nTest Case: ', test, 'Result: ', start.maxSubArray(test))