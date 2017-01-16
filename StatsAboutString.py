# Code to count the number of:
#   characters with no space
#   characters with space
#   frequency of a given character
#   letters
#   words
# in a string.

class CountCharactersAndWordsInString:
    def __init__(self, StringSource):
        self.stringSource = StringSource

    def displayString(self):
        print "The string is: ", self.stringSource

    def countCharactersNoSpace(self):
        return len(self.stringSource) - self.stringSource.count(" ")    # Excluding white space

    def countCharactersWithSpace(self):
        return len(self.stringSource)    # Including white space

    def countFrequencyOfLetter(self, CharSource):   # Returns the number of occurrences of the provided char
        return self.stringSource.count(CharSource)

    def countLetters(self):
        myOriginalList= list(self.stringSource)   # Converts the string to list
        myLetterList = []
        # Now that we have the list, we only consider the characters that are letters
        for c in myOriginalList:
            if c >= 'A' and c<='z': # Letter vary from A,B,, ..., a, b, ...,z
                myLetterList.append(c)
        return len(myLetterList)

    def countWords(self):
        # "split()" breaks the string when a white space is found.
        # Any character that is not a white space, and it is by itself, is considered a word.
        # If we need not count the non-white space characters as words, then we need to make
        # sure that only characters A,B, ..., a,b, ..., z are considered.
        return len((self.stringSource).split())

def statsOfString():

    string1 = "abc    !def?"
    class1 = CountCharactersAndWordsInString(string1)
    class1.displayString()
    print "There are ", class1.countCharactersNoSpace() , "characters, excluding white spaces, in the string"
    print "There are ", class1.countCharactersWithSpace(), "characters, including white spaces, in the string"
    print "There are ", class1.countLetters(), "letters in the string"
    print "There are ", class1.countWords(), " words in the string"

if __name__ == "__main__":
    statsOfString()