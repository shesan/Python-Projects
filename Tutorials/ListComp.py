# ListComp.py

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
print(words)

#
for word in words:
    if word != "the":
        word_lengths.append(len(word))
print(word_lengths)

#
word_lengths2 = [len(word) for word in words if word != "the"]
print(word_lengths2)

#
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = []

newlist = [number for number in numbers if number > 0]
print(newlist)
