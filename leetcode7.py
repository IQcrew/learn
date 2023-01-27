


def maxScoreWords( words: list[str], letters: list[str], score: list[int]) -> int:
    lettersValues = [ord(o)-97 for o in letters]
    print(lettersValues)
    
    ...



print(maxScoreWords(words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]))