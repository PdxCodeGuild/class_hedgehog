""" Version 1 """

# import requests
# import string

# def main():
#     response = requests.get('https://www.gutenberg.org/cache/epub/257/pg257.txt')
#     response.encoding = 'utf-8' # set encoding to utf-8
#     # print(response.text)
 
#     dict_of_words = {}
#     response = response.text.lower().replace('\n', '').replace('\r', '')
#     for character in string.punctuation:
#         response = response.replace(character, ' ')
#     list_of_words = response.split(' ')

#     for word in list_of_words:
#         if word not in dict_of_words and word not in ['ebook', 'project', 'gutenberg', '', '\\r\\n', 'of', 'and', 'for', 'the', 'this', 'that', 'but', 'not']:
#             dict_of_words[word] = 1
#         elif word in dict_of_words:
#             dict_of_words[word] += 1

#     most_frequent = []
#     for word in dict_of_words:
#         if dict_of_words[word] >= 200 and len(word) > 2:
#             most_frequent.append({word: dict_of_words[word]})

#     for word in most_frequent:
#         print(word)

# main()

#########################################################################################################
""" Version 2 """

# import requests
# import string

# def main():
#     response = requests.get('https://www.gutenberg.org/cache/epub/257/pg257.txt')
#     response.encoding = 'utf-8' # set encoding to utf-8
#     # print(response.text)
 
#     dict_of_words = {}
#     dict_of_word_pairs = {}
#     response = response.text.lower().replace('\n', '').replace('\r', '')
#     for character in string.punctuation:
#         response = response.replace(character, ' ')
#     for digit in string.digits:
#         response = response.replace(digit, '')
#     response = response.replace('  ', ' ')
#     list_of_words = response.split(' ')

#     previous_word = list_of_words[0]
#     for word in list_of_words:
#         if f'{previous_word} {word}' not in dict_of_word_pairs and word != ' ' and word != '':
#             dict_of_word_pairs[f'{previous_word} {word}'] = 1
#             previous_word = word
#         elif f'{previous_word} {word}' in dict_of_word_pairs:
#             dict_of_word_pairs[f'{previous_word} {word}'] += 1
#             previous_word = word

#     list_of_pairs = []
#     for pair in dict_of_word_pairs:
#         if dict_of_word_pairs[pair] > 10:
#             list_of_pairs.append((pair, dict_of_word_pairs.get(pair)))

#     # print(list_of_pairs)

#     for i in range(len(list_of_pairs)):
#         for j in range(len(list_of_pairs)-1):
#             if list_of_pairs[j][1] < list_of_pairs[j+1][1]:
#                 list_of_pairs[j], list_of_pairs[j+1] = list_of_pairs[j+1], list_of_pairs[j]
#     for x in range(10):
#         print(list_of_pairs[x])
    
# main()

#########################################################################################################
""" Version 3 """

import requests
import string

def main():
    response = requests.get('https://www.gutenberg.org/cache/epub/257/pg257.txt')
    response.encoding = 'utf-8' # set encoding to utf-8
    # print(response.text)
 
    dict_of_word_pairs = {}
    response = response.text.lower().replace('\n', '').replace('\r', '')
    for character in string.punctuation:
        response = response.replace(character, ' ')
    for digit in string.digits:
        response = response.replace(digit, '')
    response = response.replace('  ', ' ')
    list_of_words = response.split(' ')


    previous_word = list_of_words[0]
    for word in list_of_words:
        if f'{previous_word} {word}' not in dict_of_word_pairs and word != ' ' and word != '':
            dict_of_word_pairs[f'{previous_word} {word}'] = 1
            previous_word = word
        elif f'{previous_word} {word}' in dict_of_word_pairs:
            dict_of_word_pairs[f'{previous_word} {word}'] += 1
            previous_word = word

    list_of_pairs = []
    for pair in dict_of_word_pairs:
        if dict_of_word_pairs[pair] > 10:
            list_of_pairs.append((pair, dict_of_word_pairs.get(pair)))

    # print(list_of_pairs)

    for i in range(len(list_of_pairs)):
        for j in range(len(list_of_pairs)-1):
            if list_of_pairs[j][1] < list_of_pairs[j+1][1]:
                list_of_pairs[j], list_of_pairs[j+1] = list_of_pairs[j+1], list_of_pairs[j]
    
    user_word = input("Enter a word: \n\t> ").lower()
    list_of_following_words = []
    for pair in list_of_pairs:
        if user_word in pair[0] and user_word[0] == pair[0][0]:
            following_word = str(pair).replace('\'','').replace(',','').split(' ')
            list_of_following_words.append(following_word[1])
    if list_of_following_words == []:
        print(f"There are no words that frequently (> 10 instances) follow {user_word}.")
    else:
        print(f"These words most frequently follow {user_word}, starting with most frequent:")
        for word in list_of_following_words:
            print(word)
main()


"""
Lab 13: Count Words
Let's write a python module to analyze a given text file containing a book for its vocabulary frequency and display the most frequent words to the user in the terminal. Remember there isn't any "perfect" way to identify a word in english (acronymns, mr/ms, contractions, etc), try to find rules that work best.

Find a book on Project Gutenberg and navigate to the plain-text version. You can then send a request to that url using the requests library to get the text into Python. You can also save the file into the same folder as the .py file and open it using with.

import requests
response = requests.get('https://www.gutenberg.org/files/62897/62897-0.txt')
response.encoding = 'utf-8' # set encoding to utf-8
print(response.text)
We can also download a file of english words and place it next our .py file and load it like so:

with open('the_raven.txt', 'r', encoding='utf-8') as file:
    text = file.read()
print(text)
Take the following steps to build up our dictionary. The result should look something like {'a': 3, 'the': 4}

Make everything lowercase, strip punctuation, split into a list of words.
Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
Print the most frequent top 10 out with their counts. You can do that with the code below.
# word_dict is a dictionary where the key is the word and the value is the count
word_dict = {'apples': 2, 'bananas': 1, 'pears': 1, 'kiwi': 7}
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

Version 2 (optional)
Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.

Version 3 (optional)
Let the user enter a word, then show the words which most frequently follow it.
"""