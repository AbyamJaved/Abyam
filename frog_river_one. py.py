def solution(X, A):
    """
    Finds the earliest time the frog can jump across the river.
    
    :param X: int - The target position the frog needs to reach
    :param A: List[int] - The positions where leaves fall at each second
    :return: int - The earliest time (index), or -1 if the frog cannot cross
    """
    leaves = set()
    
    for time, position in enumerate(A):
        if position <= X:
            leaves.add(position)
            
        # Once we collected all unique positions from 1 to X, return the current time
        if len(leaves) == X:
            return time
            
    return -1
