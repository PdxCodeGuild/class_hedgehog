# Lab 13
# Count Words
# Leigh Fair-Smiley
# 6/16/2022

import requests
import string
response = requests.get('https://www.gutenberg.org/files/62897/62897-0.txt')
response.encoding = 'utf-8' # set encoding to utf-8


text = list(response.text.lower())
for i, symbol in enumerate(text):
    if symbol in string.punctuation:
        text.pop(i)

text = "".join(text)
text = text.split(" ")

word_dict = {}
for word in text:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

word_dict = {}
for i in range(len(text) - 1):
    if text[i] + " " + text[i+1] in word_dict:
        word_dict[text[i] + " " + text[i+1]] += 1
    else:
        word_dict[text[i] + " " + text[i+1]] = 1

words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

word = input("Please enter a word: ")
word_dict = {}
for i in range(len(text) - 1):
    if text[i] == word:
        if text[i+1] in word_dict:
            word_dict[text[i+1]] += 1
        else:
            word_dict[text[i+1]] = 1
            
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])