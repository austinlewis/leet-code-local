#!usr/bin/env

from typing import List, Set


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''
            Submission_1:
            https://leetcode.com/submissions/detail/551671792/
        '''
        unique: Set = set(nums)
        total_count: int = len(nums)+1
        nums.clear()
        counter: int = 1
        while(len(nums) != (total_count - len(unique)) and counter != total_count):
            if not unique.__contains__(counter):
                nums.append(counter)
            counter = counter+1
        return nums

        '''
            Unsubmitted:
            unique: Set = set(nums)
            result: List[int] = []
            for counter in range(len(nums)):
                if counter not in unique:
                    result.append(counter)
                counter = counter+1
            return result
        '''


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
          start.findDisappearedNumbers(test))
