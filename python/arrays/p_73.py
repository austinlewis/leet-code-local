#!usr/bin/env

from typing import Dict, List, Set, Tuple
from math import prod


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
            Submission_1:
            https://leetcode.com/submissions/detail/554268008/
        '''
        zeroed_column: Dict = dict().fromkeys(range(len(matrix[0])), 1)
        for row in range(len(matrix)):
            row_product: int = prod(matrix[row])
            for column in range(len(matrix[row])):
                if matrix[row][column] == 0 and zeroed_column.get(column) == 1:
                    zeroed_column[column] = 0
                    row_counter: int = row - 1
                    while(row_counter != -1):
                        matrix[row_counter][column] = 0
                        row_counter = row_counter - 1
                if row_product == 0:
                    matrix[row][column] = 0
                else:
                    matrix[row][column] = matrix[row][column] * \
                        zeroed_column.get(column)
        return matrix

        '''
            Submission_2:
            https://leetcode.com/submissions/detail/554275907/

            zeroed_column: Dict = dict().fromkeys(range(len(matrix[0])), 1)
            for row_counter, row in enumerate(matrix):
                row_product: int = prod(row) if prod(row) == 0 else 1
                for column_counter, column in enumerate(row):
                    if column == 0 and zeroed_column.get(column_counter) == 1:
                        zeroed_column[column_counter] = 0
                        update_row_counter: int = row_counter - 1
                        while(update_row_counter != -1):
                            matrix[update_row_counter][column_counter] = 0
                            update_row_counter = update_row_counter - 1
                    matrix[row_counter][column_counter] = matrix[row_counter][column_counter] * zeroed_column.get(column_counter) * row_product
            return matrix
        '''


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
print('\nTest Case: ', test_cases, 'Result: ', start.setZeroes(test_cases))
