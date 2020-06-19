'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    # if the length of the word is less than or equal to 1 
    # than there is not a th together. so return 0.
    if len(word) <= 1:
        return 0

    # if the 0 AND 1 index of the word are th then add 1 and recurse over the new word, shortend by one letter.
    elif word[0] == 't' and word[1] == 'h':
        return 1 + count_th(word[1:])
    
    # if the 0 AND 1 index of the word are not th, and the word is longer than 1 letter
    # then we need to recurse over the new letters and see if there are any other th
    # in the rest of the word.
    return count_th(word[1:])
