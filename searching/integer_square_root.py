# integer_square_root.py

"""Write a program which takes a nonnegative integer and retums the largest integer whose square is
less than or equal to the given integer. For example: 
- If the input is 16, return 4.
- If the input is 300, return 17, since 17^2 = 289 < 300 and 18^2 = 324 > 300.

SOLUTION: 
- brute-force approach: loop through 1 to k, square each number and stop if the result exceed => time complexity O(k). 

HINT: Use binary search to eliminate a large set of candidate numbers. 
- If x^2 < k => no number smaller than x can be the result. 
- If x^2 > k => no number greater than or equal to x can be the result.

We maintain an interval consisting of value whose squares are unclassified with respect to k, i.e., might be less 
than or greater than k. 
"""

def square_root(k): 
    """Function that takes a nonnegative integer and returns the largest integer
    whose square is less than or equal to the given integer. 
    """

    left, right = 0, k 

    """Candiate interval [left, right] where everything before left has square <= k, 
    everything after right has square < k.
    """
    while left <= right:
        mid = (left + right) // 2 
        mid_squared = mid * mid 

        if mid_squared == k: 
            return mid 
        elif mid_squared < k: 
            left = mid + 1         # remove the left interval 
        elif mid_squared > k: 
            right = mid - 1        # remove the right interval
    
    return left - 1 


if __name__ == "__main__":
    k = 36 
    print(square_root(k))
    k = 39
    print(square_root(k))
    k = 1500
    print(square_root(k))
    k = 150_000
    print(square_root(k))

        
