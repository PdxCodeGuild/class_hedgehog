# Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal. 
# Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

# Find a book on Project Gutenberg and navigate to the plain-text version. 
# You can then send a request to that url using the requests library to get the text into Python. 
# You can also save the file into the same folder as the .py file and open it using with.

# Take the following steps to build up our dictionary. The result should look something like {'a': 3, 'the': 4}

# 1. Make everything lowercase, strip punctuation, split into a list of words.
# 2. Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
# 3. Print the most frequent top 10 out with their counts. You can do that with the code below.

import requests
from collections import Counter
import string


def count():
    response = requests.get("https://www.gutenberg.org/cache/epub/68325/pg68325.txt")
    response.encoding = 'utf-8'
    books = response.text
    book = books.lower() # Make lowercase
    new_book = book.translate(str.maketrans('', '', string.punctuation)) # Remove punctuation


    # word_dict is a dictionary where the key is the word and the value is the count
    word_dict = dict(Counter(new_book.split())) # Found Counter method
    words = list(word_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])

count()