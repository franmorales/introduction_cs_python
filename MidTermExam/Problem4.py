def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Your code here
    finalList = []
    for ele in aList:
        if len(ele) < 4:
            finalList.append(ele)
    return finalList
