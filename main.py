'''
This Program is a wordle solver AI that uses AI to solve the wordle game.
'''

import words
from collections import Counter

all_words = words.all_wordle_words()
current_word = ""
valid_words = sorted(all_words)
invalid_letters = set()
green_letters = set()
yellow_letters = set()

def check_black(word):
    for letter in word:
        if letter in invalid_letters:
            return False
    return True

def check_green(word):
    for letter, position in green_letters:
        if word[position] != letter:
            return False
    return True

def check_yellow(word):
    for letter, position in yellow_letters:
        if word[position] != letter or letter not in word:
            return False
    return True

def get_valid_words():
    new_words = []
    for word in valid_words:
        if check_black(word) or not check_green(word) or not check_yellow(word):
            continue
        new_words.append(word)
        
    return new_words


def convert_color_code(word, color_code):
    
    counter = 0
    word = word.lower()
    color_code = color_code.lower()
    
    for code in color_code:
        if code == 'g':
            green_letter =  word[counter]
            green_pos = counter
            letters_set = (green_letter, green_pos)
            print(letters_set)
            print(green_letters)
            green_letters.add(letters_set)
            
        if code == 'y':
            yellow_letter =  word[counter]
            yellow_pos = counter
            letters_set = (yellow_letter, yellow_pos)
            yellow_letters.add(letters_set)
            
        if code == 'b':
            black_letter =  word[counter]
            invalid_letters.add(black_letter)
            
        counter += 1
    
    return green_letters, yellow_letters, invalid_letters
    
        
def load_words():
    return words.all_wordle_words()
def play():
    game_init = True
    
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
    
    valid_words = get_valid_words()
    print(f'Valid Words: {valid_words}')
    


play()