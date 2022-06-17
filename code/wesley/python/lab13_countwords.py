import requests
from string import punctuation

response = requests.get('https://www.gutenberg.org/cache/epub/26184/pg26184.txt')
response.encoding = 'utf-8'

new_string = response.text.translate(str.maketrans('', '', punctuation))

new_list = new_string.split()

word_dict = {}
for word in new_list:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

# word_dict is a dictionary where the key is the word and the value is the count
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
