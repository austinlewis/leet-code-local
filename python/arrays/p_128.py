#usr/bin/env

from typing import List, Set

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
            Submission_1:
            https://leetcode.com/submissions/detail/556106555/
        '''
        if len(nums) < 1:
            return 0
        nums.sort()
        max_count: int = 0
        cur_count: int = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue

            if nums[i] == nums[i+1]-1:
                cur_count+=1
                continue
           
            if(max_count < cur_count):
                max_count = cur_count
            cur_count=0
        return max_count if max_count > cur_count else cur_count


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
          start.longestConsecutive(test))