def solution(A, K):
    """
    Rotates array A to the right by K steps.
    
    :param A: List[int] - The array of integers to rotate
    :param K: int - The number of right rotations
    :return: List[int] - The rotated array
    """
    # Handle edge case for an empty array
    if not A:
        return A
    
    n = len(A)
    # If K is larger than the array length, use modulo to avoid redundant rotations
    K = K % n
    
    if K == 0:
        return A
        
    # Slice the array to shift the last K elements to the front
    return A[-K:] + A[:-K]
