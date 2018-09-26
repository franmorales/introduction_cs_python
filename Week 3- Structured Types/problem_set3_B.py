def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    finalString  = ''
    duplicateLetters = lettersGuessed[:]
    for char in secretWord:
        if char in duplicateLetters:
            finalString += char
            #duplicateLetters.remove(char)
        else:
            finalString += '_ '
    return finalString
