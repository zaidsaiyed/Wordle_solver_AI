import words
from collections import Counter
from main import word_check_black, word_check_green, word_check_yellow, convert_color_code

all_words = words.all_wordle_words()
current_word = ""
game_init = True
valid_words = []
invalid_letters = set()

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