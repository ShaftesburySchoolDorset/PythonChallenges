from random import shuffle

def make_anagram(word):
    wordArr = list(word.lower().rstrip().lstrip())
    shuffle(wordArr)
    new_word = ''.join(wordArr)
    if new_word == word:
        make_anagram(word)
    else:
        return new_word

while 1:
    print(make_anagram(input()))
