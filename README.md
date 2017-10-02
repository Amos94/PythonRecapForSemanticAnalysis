# Tasks
Find my the code at: https://github.com/Amos94/PythonRecapForSemanticAnalysis

1. Choose a corpus
Let’s say the text of this page: http://www.ifi.uzh.ch/en/ifi/aboutus.html

2. Collect words with their frequencies and print 10 most frequent
--> what data structure suits this task?
	>Dictionary (key: word, value: frequency)
	>Singly Linked List(each node containing a tuple)
	>2 lists one of words + one of frequencies
--> how to avoid memory problems while reading the corpus?
	Read each line and check if the word is already in the data structure used.

Code for 2: https://github.com/Amos94/PythonRecapForSemanticAnalysis/blob/master/Analyzer.py

3. Collect word pairs with their frequencies and print 10 most frequent 
--> what data structure suits this task?
	>Singly Linked List(each node containing a tuple(a tuple of words), frequency)
	>2 lists one of tuples + one of frequencies
--> how to avoid memory problems while reading the corpus? 
	Read each line and check if the tuple is already in the data structure used.

Code for 3: 
https://github.com/Amos94/PythonRecapForSemanticAnalysis/blob/master/PairAnalyzer.py

4. Write a function which takes as an input a word pair (a,b) and your frequency structure from #3. The function returns a probability of this pair (a,b) and a probability of (a,-b), i.e. all the word pairs where word “a” is in the first position and in the second position is the forward different than “b”.

Code for 4:
https://github.com/Amos94/PythonRecapForSemanticAnalysis/blob/master/TaskFour

--> should this function take any other input to make the calculations more efficient if we call it many times for different word pairs but frequencies are collected based on the same corpus?
	Yes, a datastructure such a matrix would be better.


