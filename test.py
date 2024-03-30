
valid_words = []
all_words = ['alert', 'valid', 'words']
invalid_letters = ['a', 'l']
invalid_letters = set(invalid_letters)

for word in all_words:
    word_set = set(word)
    intersection_set = word_set.intersection(invalid_letters)
    length = len(intersection_set)
    print(f'Intersection: {intersection_set}, Length: {length}')
    if length == 0:
        valid_words.append(word)
print(valid_words)
