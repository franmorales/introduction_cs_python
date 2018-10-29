def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    ans = 0
    for elem in hand:
        ans += hand[elem]
    return ans
