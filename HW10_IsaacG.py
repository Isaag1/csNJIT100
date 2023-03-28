"""
Isaac Guerrero
CS 100 Section 015
HW08,November 7, 2021
"""
#1
def initialLetterCount(wordList):
    count_dict = {}
    for word in wordList:
        if word[0] in count_dict:
            count_dict[word[0]] += 1
        else:
            count_dict[word[0]] = 1
    return count_dict

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetterCount(horton))

#2
def initialLetters(wordList):
    letter_dict = {}
    for word in wordList:
        letter = word[0]
        if letter in letter_dict:
            if word not in letter_dict[letter]:
                letter_dict[letter].append(word)
        else:
            letter_dict[letter] = [word]
    return letter_dict

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetters(horton))

#3
def shareOneLetter(wordList):
    shared_dict = {}
    for word1 in wordList:
        shared = []
        for word2 in wordList:
            if word1 != word2:
                if set(word1) & set(word2):
                    shared.append(word2)
        shared_dict[word1] = shared
    return shared_dict

horton = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(shareOneLetter(horton))
