# cyclically_sorted_array.py 

"""PROBLEM: """

def search_smallest(A): 

    left, right = 0, len(A) - 1 
    while left < right: 
        mid = (left + right) // 2
        if A[mid] > A[right]: 
            # Minimum must be in A[mid + 1: right]
            left = mid + 1 
        else:   # A[mid] < A[right]
            # Minimum cannot be in A[mid + 1: right] => it must be in A[left: mid]
            right = mid  

    # Loop ends when left == right 
    return left, A[left]


if __name__ == '__main__':
    A = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
    print(search_smallest(A))