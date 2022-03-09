
A transaddition is the process of taking a word, adding a single letter and optionally shuffling the letters to make a new word.
For example, the word "TACK" can be made via a transaddition of the word "ACT".

Please implement the following functions based on transaddition:

1. A function to check if a target word can be made via a transaddition of a source word.
e.g.
f("ACT", "TACK") == True
f("TACK", "ACT") == False
f("ACE", "TACK") == False

2. A function that takes two lists of words and returns a list of words in the second list that can be made via a transadditions of words in the first list.
e.g.
f(["ACT", "SET", "FOO"], ["TACK", "TEST", "BAR"]) == ["TEST", "TACK"]

For both functions, you can assume all strings will consist only of upper case letters with no special characters.
