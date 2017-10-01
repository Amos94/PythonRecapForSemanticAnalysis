import re
from heapq import nlargest

class PairAnalyzer():

    file = None

    freq = []
    pairs = []

    def __init__(self):
        try:
            self.file = open("corpus.txt", "r")
        except:
            print("Couldn't load the corpus")

    def analyzeFreq(self):
        dict = {}
        for line in self.file:
            #Spliting the lines into words using regular expressions
            words = re.findall(r"[\w]+", line)
            #for each word in the array check if it's in the global array of words, otherwise append it and increment the freq array at it' point
            for i in range(0, len(words)):
                if(i != len(words)-1):
                    w1 = words[i].lower()
                    w2 = words[i+1].lower()

                    tp = tuple((w1,w2))

                    if(tp in dict):
                        dict[tp] += 1
                    else:
                        dict[tp] = 1

        top = nlargest(10, dict.values())
        toReturn = []
        for w,w1 in dict.items():
            if(w1 in top):
                toReturn.append(tuple((w,w1)))
        return toReturn



a = PairAnalyzer()
print(a.analyzeFreq())
