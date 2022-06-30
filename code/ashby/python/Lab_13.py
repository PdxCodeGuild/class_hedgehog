"""Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal. Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

Find a book on Project Gutenberg and navigate to the plain-text version. You can then send a request to that url using the requests library to get the text into Python. You can also save the file into the same folder as the .py file and open it using with.
"""

"""with open('gutenberg.txt', 'r', encoding='utf-8') as file:
    text = file.read()
print(text)

"""

import requests

def striplist(texts):
    from string import punctuation
    punc = list(punctuation) + [" ", "\n", "\r"]
    for x in punc:
        texts = texts.replace(x, "")
    return texts


def main():
    word_count = {}
    double_count = {}
    # book_text = text.split(" ")
    # print(book_text)

    response = requests.get('https://www.gutenberg.org/cache/epub/68330/pg68330.txt')
    response.encoding = 'utf-8' # set encoding to utf-8

    book_text = response.text
    book_text_split = book_text.split()
    for i, book in enumerate(book_text_split):
        book_text_split[i] = striplist(book)
        
    for i, book in enumerate(book_text_split):
        if book.lower() in word_count.keys():
            word_count[book.lower()] += 1
        else: 
            word_count[book.lower()] = 1
        if i != len(book_text_split)-1:
            check = book_text_split[i]+ " " + book_text_split[i+1]
            if check in double_count.keys():
                double_count[check] += 1
            else:
                double_count[check] = 1
    #print(word_count)
    #print(book_text_sep) 

    print("The top ten words are (Drum roll please):")
    for x in sorted(word_count, key=word_count.get, reverse=True)[0:10]:
        print(x, word_count[x])

    pause = input("The top ten DOUBLE words go to (Drum roll again):")

    for x in sorted(double_count, key=double_count.get, reverse=True)[0:10]:
        print(x, double_count[x])
main()



""""Take the following steps to build up our dictionary. The result should look something like {'a': 3, 'the': 4}

Make everything lowercase, strip punctuation, split into a list of words.
Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
Print the most frequent top 10 out with their counts. You can do that with the code below.
"""



"""Version 2 (optional)
Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts."""


"""Version 3 (optional)
Let the user enter a word, then show the words which most frequently follow it."""