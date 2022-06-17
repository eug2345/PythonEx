# Given a string, return a string where for every char in the original string, there are three chars.

# <EXAMPLES>

# one("The") → "TTThhheee"
# one("AAbb") → "AAAAAAbbbbbb"
# one("Hi-There") → "HHHiii---TTThhheeerrreee"

word1= "The" "TTThheee"
word2 = "AAbb" "AAAAAAbbbbbb"
word3 = "JHi-There" "HHHhiiii----TTTThhheeeerree"

sentence = word1 + " " + word2 + " " + word3
print(sentence)

