#!usr/bin/env

from typing import List, Set


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            Submission_1:
            https://leetcode.com/submissions/detail/559932358/

            maxProfit: int = 0
            lowestPriceIndex: int = 0
            for i in range(1, len(prices)):
                if prices[lowestPriceIndex] >= prices[i]:
                    lowestPriceIndex = i
                    continue
                maxProfit = max(maxProfit, prices[i] - prices[lowestPriceIndex])
            return maxProfit
        '''

        '''
            Submission_2:
            https://leetcode.com/submissions/detail/559936404/
        '''
        maxProfit: int = 0
        lowestPrice: int = prices[0]
        for i in range(1, len(prices)):
            if lowestPrice >= prices[i]:
                lowestPrice = prices[i]
                continue
            maxProfit = max(maxProfit, prices[i] - lowestPrice)
        return maxProfit
        

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
    print('\nTest Case: ', test, 'Result: ', start.maxProfit(test))
