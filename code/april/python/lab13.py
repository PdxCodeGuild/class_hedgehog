"""
Lab 13: Count Words
April 
16 June 2022
"""

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
translator = str.maketrans('', '', string.punctuation)
remove_punctuation = text.translate(translator)
text = remove_punctuation.lower().split()

###################

# added excluded word removal 
def exclusions():
    with open("articles.txt") as f:
        articles = f.read()
        # articles = articles.split()
        # print(articles)

    with open("conjunctions.txt") as f:
        conjunctions = f.read()
        # print(conjunctions)

    with open("prepositions.txt") as f:
        prepositions = f.read()
        # print(prepositions)


    def default_not():
        not_words = open("not_words_list.txt", "w")
        other_words = ["Gutenberg\n", "eBook \n", "www\n", "she\n", "he\n", "I\n", '"i\n', "they\n", "is\n", "they\n", "her\n", "him\n", "was\n", "it\n", "you\n", "all\n", "his\n", '“i\n',"UTF"]
        not_words.writelines(other_words)
        not_words.close()

    def exclude_articles():
        not_words = open("not_words_list.txt", "a")  
        not_words.write(f"\n{articles}")
        not_words.close()

    def exclude_prepositions():
        not_words = open("not_words_list.txt", "a")  
        not_words.write(f"\n{prepositions}")
        not_words.close()

    def exclude_conjunctions():
        not_words = open("not_words_list.txt", "a")  
        not_words.write(f"\n{conjunctions}")
        not_words.close()

    def exclude_all():
        not_words = open("not_words_list.txt", "a")  
        not_words.write(f"\n{articles}\n{prepositions}\n{conjunctions}")
        not_words.close()

    def exclusion_choices():
        while True:
            menu = """
            What would you like to exclude?
            1) Exclude Nothing
            2) Exclude Articles
            3) Exclude Prepositions
            4) Exclude Conjunctions
            5) Exclude Articles and Prepositions
            6) Exclude Articles and Conjunctions
            7) Exclude Prepositions and Conjunctions
            8) Exclude All
            """
            
            choice = input(menu + "-> ")
            default_not()
            if choice == "1":
                break
            elif choice == "2":
                exclude_articles()
                break
            elif choice == "3":
                exclude_prepositions()
                break
            elif choice == "4":
                exclude_conjunctions()
                break
            elif choice == "5":
                exclude_articles()
                exclude_prepositions()
                break
            elif choice == "6":
                exclude_articles()
                exclude_conjunctions()
                break
            elif choice == "7":
                exclude_prepositions()
                exclude_conjunctions()
                break
            elif choice == "8":
                exclude_all()
                break
            else:
                print("Error")
                break

    exclusion_choices()
exclusions()


#####################

with open('not_words_list.txt', 'r', encoding='utf-8') as f:
    not_words = f.read()

translator2 = str.maketrans('', '', string.punctuation)
remove_punctuation2 = not_words.translate(translator2)
not_words = remove_punctuation2.lower().split()

for word in list(text): 
    if word in not_words:
        text.remove(word)

#####################

# word_dict is a dictionary where the key is the word and the value is the count
word_dict = {}

# If a word isn't in dictionary yet, add it with a count of 1. If it is, increment its count.
for word in text:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1


# Print the most frequent top 10 out with their counts. You can do that with the code below.
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])
