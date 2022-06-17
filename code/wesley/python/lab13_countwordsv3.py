import requests
from string import punctuation

response = requests.get('https://www.gutenberg.org/cache/epub/26184/pg26184.txt')
response.encoding = 'utf-8'

new_string = response.text.translate(str.maketrans('', '', punctuation))

new_list = new_string.lower().split()

word_dict = {}
choice = input('Please choose a word: ')
for i in range(len(new_list) -1):
    if new_list[i] == choice:
        if new_list[i+1] in word_dict: 
            word_dict[new_list[i+1]] += 1
        else:
            word_dict[new_list[i+1]] = 1

words = list(word_dict.items()) 
words.sort(key=lambda tup: tup[1], reverse=True)  
for i in range(min(10, len(words))):  
    print(words[i])
