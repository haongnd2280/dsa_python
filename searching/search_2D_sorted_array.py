# search_2D_sorted_array.py 

"""2D sorted array is an array that has its rows and columns non-decreasing. 
PROBLEM: Design an algo that takes a 2D sorted array and a number, and checks whether that number appears in the array.


SOLUTION: 
- brute-force approach: perform binary search on each row (column) independently => time complexity O(mlogn) (O(nlogm)).

HINT: Look at extremal cases - compare x with A[0][n-1] (end of 1th row) or A[m-1][0] (end of 1th column).
- If x == A[0][n-1] => found the desired value => return True. 
- If x > A[0][n-1] => x is greater than all elements in row 0 => eliminate that row (forward to the next row). 
- If x < A[0][n-1] => x is smaller than all elements in column n-1 => eliminate that column (step back one column).
In either case, we have a 2D array with one fewer row or column to search. 
In each iteration, we remove a row or a column => we inspect at most m + n - 1 elements => time complexity O(m + n).

The idea is to take advantage of the fact that both rows and columns are sorted.
"""


def matrix_search(A, x): 
    """Function that takes the 2D array (m x n) as A and the input number as x. 
    
    It returns True if the input number is found in the array. Otherwise, it returns False.
    """

    row, col = 0, len(A) - 1      # start from the top-right corner 
    # Keep searching while there are unclassified rows and columns
    while row < len(A) and col >= 0: 
        if A[row][col] == x: 
            return True 
        elif A[row][col] < x: 
            row += 1              # Elimiate this row
        else:                     # A[row][col] > x
            col -= 1              # Eliminate this column

    return False 

