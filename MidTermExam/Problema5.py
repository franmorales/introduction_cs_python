def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Your code here
    newKy = list(d.values())
    newVal = list(d.keys())
    newDict = {}
    tracker = 0
    #newMgValues = []
    for ele in newKy:
        if ele not in newKy[:tracker]:
            newDict[ele] = [newVal[tracker]]      
        else:
            newDict[ele].append(newVal[tracker])
            newDict[ele].sort()
        tracker += 1
    return newDict
