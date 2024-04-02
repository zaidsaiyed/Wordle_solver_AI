
valid_words = []
all_words = ['alert', 'valid', 'words']
invalid_letters = {'a', 'l'}
untried_letters_list = [(chr(ord('a') + i)) for i in range(26)]

invalid_letters.add(("a", 0))

print(untried_letters_list)


def lets_print(word):
    print(word)
    
lets_print("hello")