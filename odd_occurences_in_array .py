def solution(A):
    """
    Finds the unpaired element in an array where every other element occurs an even number of times.
    
    :param A: List[int] - The array of integers
    :return: int - The unpaired element
    """
    result = 0
    for number in A:
        result ^= number
    return result
