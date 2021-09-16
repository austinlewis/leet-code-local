#!usr/bin/env

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
            Submission_1:
            https://leetcode.com/submissions/detail/556069424/
        '''
        n: int = len(matrix)
        if n > 1:
            for i in range(n//2):
                for j in range(i, n-i-1):
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[n-1-j][i]
                    matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                    matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                    matrix[j][n-1-i] = temp
        return matrix


print('''
    \tTest case input format
    \tSingle:
    \t\t[[1 2 3] [1 1 1] [1 2 3]]
    \t\tz
    \n\tPress 'z' key to start test run
    \n\n\nEnter the Test case:
''')

test_cases = []
while True:
    try:
        row = [int(item) for item in input().split()]
        test_cases.append(row)
    except ValueError:
        break
start: Solution = Solution()
print('\nTest Case: ', test_cases, 'Result: ', start.rotate(test_cases))
        