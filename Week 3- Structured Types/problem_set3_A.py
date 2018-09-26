def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    boolString  = ''
    duplicateLetters = lettersGuessed[:]
    for char in secretWord:
        if char in duplicateLetters:
            boolString += char
            duplicateLetters.remove(char)
    return boolString == secretWord
