def solution(A):
    """
    Counts the number of passing cars (cars going east (0) followed by cars going west (1)).
    
    :param A: List[int] - Array of 0s and 1s representing cars
    :return: int - Number of passing cars, or -1 if it exceeds 1,000,000,000
    """
    east_count = 0
    passing_cars = 0
    
    for car in A:
        if car == 0:
            east_count += 1
        else:
            passing_cars += east_count
            if passing_cars > 1000000000:
                return -1
                
    return passing_cars
