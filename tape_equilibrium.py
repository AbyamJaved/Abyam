def solution(A):
    """
    Minimizes the difference between the sum of the first part and the sum of the second part.
    
    :param A: List[int] - Array of integers
    :return: int - The minimum absolute difference
    """
    left_sum = 0
    right_sum = sum(A)
    min_diff = None
    
    for p in range(0, len(A) - 1):
        left_sum += A[p]
        right_sum -= A[p]
        current_diff = abs(left_sum - right_sum)
        
        if min_diff is None or current_diff < min_diff:
            min_diff = current_diff
            
    return min_diff
