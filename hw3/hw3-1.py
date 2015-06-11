def bunny_ears(p):
    # Base case
    if (p < 1):
        return 0
    # If odd, add 2 ears
    elif (p%2 == 1):
        return bunny_ears(p-1) + 2
    # If even, add 3 ears
    elif (p%2 == 0):
        return bunny_ears(p-1) + 3
    
