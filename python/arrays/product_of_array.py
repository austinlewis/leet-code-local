#!usr/bin/env

from typing import Dict, List
from math import prod


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        '''
            Submission:
            https://leetcode.com/submissions/detail/552136217/

            result: List[int] = []
            for index in range(len(nums)):
                copy: List[int] = nums.copy()
                copy.pop(index)
                result.insert(index, prod(copy))
            return result

            Observation:
            This method leads to time-exceed error, why? --> the next is solution based on this but with storage 
        '''

        '''
            Submission:
            https://leetcode.com/submissions/detail/552219522/

            result: List[int] = []
            previousProduct: Dict = dict.fromkeys(nums, 0)
            for index in range(len(nums)):
                if previousProduct.get(nums[index]) == 0:
                    copy: List[int] = nums.copy()
                    copy.pop(index)
                    value: int = prod(copy)
                    previousProduct[nums[index]] = value
                    result.insert(index, value)
                else:
                    result.insert(index, previousProduct.get(nums[index]))
            return result
        '''

        '''
            Submission:
            https://leetcode.com/submissions/detail/552219845/
        '''
        previousProduct: Dict = dict.fromkeys(nums, 0)
        for key in previousProduct.keys():
            copy: List[int] = nums.copy()
            copy.remove(key)
            previousProduct[key] = prod(copy)
        return [previousProduct.get(num) for num in nums]

        '''
            Observation:
            Slight change from previous method looping method and use of list-compression
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
    print('\nTest Case: ', test, 'Result: ', start.productExceptSelf(test))
