'''
This Program is a wordle solver AI that uses AI to solve the wordle game.
'''

import words
from collections import Counter
def main():
    all_words = load_words()
    current_word = ""
    game_init = True
    valid_words = []
    invalid_letters = []
    
    print("Welcome to Wordle Solver AI!")
    print()
    if game_init == True:
        current_word = 'alert'
        
    print(f'Try: {current_word}')
    print()
    color_code = input("Enter the color codes eg. g for green, y for yellow, b for black: ")
    print()
    game_init = False
    green_letters, yellow_letters, invalid_letters = convert_color_code(current_word, color_code)
    
    print(f'Green Letters: {green_letters}')
    print(f'Yellow Letters: {yellow_letters}')
    print(f'Invalid Letters: {invalid_letters}')
    
    valid_words = word_check_black(all_words, invalid_letters, valid_words)
    green_valid = word_check_green(valid_words, green_letters)
    yellow_valid = word_check_yellow(green_valid, yellow_letters)
    print(sorted(yellow_valid))
    candiate_words = sorted(yellow_valid)
    # print(candiate_words)

def word_check_black(all_words, invalid_letters, valid_words):
    if invalid_letters:
        invalid_letters = set(invalid_letters)
        for word in all_words:
            word_set = set(word)
            intersection_set = word_set.intersection(invalid_letters)
            length = len(intersection_set)
            if length == 0:
                valid_words.append(word)
    return valid_words

def check_black(word):
    pass

def word_check_green(valid_words, green_letters):
    new_valid_words = []
    if green_letters:
        for word in valid_words:
            for elem in green_letters:
                for ch, pos in elem.items():
                    if word[pos] == ch:
                        new_valid_words.append(word)
    return new_valid_words

def word_check_yellow(valid_words, yellow_letters):
    new_valid_words = []
    if yellow_letters:
        for word in valid_words:
            for elem in yellow_letters:
                for ch, pos in elem.items():
                    print(f'Word: {word}, Letter: {ch}, Position: {pos}, elem: {elem} , yellow_letters: {yellow_letters}')
                    if word[pos] == ch:
                        print(f'YESSSSSSSSSSS!!!!  Word: {word}, Letter: {ch}, Position: {pos}, elem: {elem} , yellow_letters: {yellow_letters}')
                        new_valid_words.append(word)
                        # print(new_valid_words)
                        break
    return new_valid_words      

def convert_color_code(word, color_code):
    invalid_letters = []
    green_letters = []
    yellow_letters = []
    
    counter = 0
    word = word.lower()
    color_code = color_code.lower()
    
    for code in color_code:
        if code == 'g':
            green_letter =  word[counter]
            green_pos = counter
            letters_dict = {green_letter: green_pos}
            green_letters.append(letters_dict)
            
        if code == 'y':
            yellow_letter =  word[counter]
            yellow_pos = counter
            letters_dict = {yellow_letter: yellow_pos}
            yellow_letters.append(letters_dict)
            
        if code == 'b':
            black_letter =  word[counter]
            invalid_letters.append(black_letter)
            
        counter += 1
    
    return green_letters, yellow_letters, invalid_letters
    
        
def load_words():
    return words.all_wordle_words()

    

if __name__ == '__main__':
    main()