def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    if N//10 == 0:
        return N
    else:
        return N%10 + sumDigits(N//10)
