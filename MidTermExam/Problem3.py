def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    count = 0
    while True:
        if b**count < x:
            count += 1
        elif b**count == x:
            return count
        else:
            return count-1
