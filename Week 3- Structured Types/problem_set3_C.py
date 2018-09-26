def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    dasABC = list('abcdefghijklmnopqrstuvwxyz')
    for ele in lettersGuessed:
        dasABC.remove(ele)
    return ''.join(map(str, dasABC))
