"""
Lab 13: Count Words
April 
16 June 2022
"""

"""Version One"""

import string
import requests

# find a book on Project Gutenberg
# send a request to that url using the requests library to get text into Python
response = requests.get("https://www.gutenberg.org/files/11/11-0.txt") 
response.encoding = "utf-8" # set encoding to utf-8

# save the file into the same folder as the .py file 
open('alice.txt', 'wb').write(response.content)

# download a file of english words and place it next our .py file
with open('alice.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Make everything lowercase, strip punctuation, split into a list of words
text = text.lower().split()

# word_dict is a dictionary where the key is the word and the value is the count
word_dict = {}

# If a word isn't in dictionary yet, add it with a count of 1. If it is, increment its count.
for word in text:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

# print(word_dict)

# Print the most frequent top 10 out with their counts. You can do that with the code below.

words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])