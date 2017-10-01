import re
from heapq import nlargest

class Analyzer():

    file = None
    words = []
    freq = []
    pairs = []

    def __init__(self):
        try:
            self.file = open("corpus.txt", "r")
        except:
            print("Couldn't load the corpus")

    def analyzeFreq(self):
        for line in self.file:
            #Spliting the lines into words using regular expressions
            words = re.findall(r"[\w]+", line)
            #for each word in the array check if it's in the global array of words, otherwise append it and increment the freq array at it' point
            for word in words:
                w = word.lower()
                if(w not in self.words):
                    self.words.append(w)
                    self.freq.append(1)
                else:
                    i = self.words.index(w)
                    self.freq[i] = self.freq[i] + 1

        for i in range(0, len(self.words)):
            self.pairs.append(tuple((self.words[i], self.freq[i])))
        topFreq = nlargest(10, self.freq)
        topMostFreqWords = []
        for pair in self.pairs:
            if(pair[1] in topFreq and (pair[0] not in topMostFreqWords)):
                topMostFreqWords.append(tuple((pair[0], pair[1])))
        return topMostFreqWords



a = Analyzer()
print(a.analyzeFreq())
