def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    boolFlag = False
    if word in wordList:
        boolFlag = True
        for char in word:
            if char in hand:
                value = word.count(char)
                if value > hand[char]:
                    boolFlag = False
            else:
                boolFlag = False
                break
    return boolFlag
