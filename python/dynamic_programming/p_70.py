#!usr/bin/env
from itertools import combinations
from math import factorial


class Solution:
    def climbStairs(self, n: int) -> int:
        '''
            Submission_1:
            https://leetcode.com/submissions/detail/559385152/
        
        steps_count: int = 1
        for count in range(1, n//2+1):
            steps_count = steps_count + self.combination(n-count, count)
        return steps_count

    def combination(self, n, r):
        if n <= r:
            return 1
        return self.factorial(n) // (self.factorial(r) * self.factorial(n-r))

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2
        return n*self.factorial(n-1)
        '''

        '''
            Submission_2:
            https://leetcode.com/submissions/detail/559387551/
        '''
        steps_count: int = 1
        for count in range(1, n//2+1):
            steps_count = steps_count + self.combination(n-count, count)
        return steps_count

    def combination(self, n, r):
        if n <= r:
            return 1
        return factorial(n) // (factorial(r) * factorial(n-r))

        '''
            Tring python3's itertools-combinations function
        steps_count: int = 1
        for count in range(1, n//2+1):
            val = combinations(range(n-count), n-count)
            print(len(val))
            for combi in val:
                print(combi)
            #steps_count = steps_count + combinations([i for i in range(n-count)], count)
        return steps_count
        '''


print('''
    \tTest case input format
    \tSingle:
    \t\t2
    \t\tz
    \tMultiple:
    \t\t1 2 5
    \t\tz
    \n\tPress 'z' key to start test run
    \n\n\nEnter the Test case:
''')

test_cases = []
while True:
    try:
        test_cases = [int(item) for item in input().split()]
    except ValueError:
        break
start: Solution = Solution()
for test in test_cases:
    print('\nTest Case: ', test, 'Result: ', start.climbStairs(test))
