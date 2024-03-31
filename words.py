def all_wordle_words():
    list_of_words = []
    with open('wordle_words.txt') as f:

        for line in f.readlines():
            list_of_words.append(line.strip())            
    return list_of_words