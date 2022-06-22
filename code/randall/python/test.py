def get_count(sentence):
    count = 0
    for char in sentence:
        if char in 'aeiouAEIOU':
            count += 1
    return count

print(get_count("I don't know what we're yelling about"))