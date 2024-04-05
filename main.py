'''
This Program is a wordle solver AI that uses AI to solve the wordle game.
Created by: Zaid Saiyed
'''

import words, re
from collections import Counter

all_words = words.all_wordle_words()
current_word = ""
valid_words = sorted(all_words)
invalid_letters = set()
green_letters = set()
yellow_letters = set()
untried_letters_list = [chr(ord('a') + i) for i in range(26)]

def check_black(word):
    for letter in word:
        if letter in invalid_letters:
            return True
    return False

def check_green(word):
    for letter, position in green_letters:
        if word[position] != letter:
            return False
    return True

def check_yellow(word):
    for letter, position in yellow_letters:
        if word[position] == letter or letter not in word:
            return False
    return True

def get_valid_words(valid_words):
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

def untried_prob(words):
    counter = Counter()
    for word in words:
        for letter in word:
            if letter in untried_letters_list:
                counter[letter] += 1
    return counter

def freq_prob(words):
    counter = Counter()
    for word in words:
        for letter in word:
            counter[letter] += 1
    return counter

def smart_guess(valid_words):
    untried_letters = untried_prob(valid_words)
    freq_letter = freq_prob(valid_words)
    
    if len(untried_letters) > 1:
        score = []
        set_of_all_words = set(all_words)
        for word in set_of_all_words:
            w_set = set(word)
            untried_sum = sum([untried_letters[letter] if letter in untried_letters else 0 for letter in w_set])
            freq_sum = sum([freq_letter[letter] for letter in w_set])
            
            score.append((word, untried_sum, freq_sum))
        # priority = sorted(score, key=lambda x: (x[0], x[1], x[2]),reverse=True)
        # print(score)
        priority = sorted(score, key = lambda x: (-x[1], -x[2], x[0]))
        # print(priority)
        our_guess = priority[0][0]
        
    else:
        our_guess = sorted(valid_words, key = lambda x: (-len(set(x)), -sum(freq_letter[c] for c in x), x))[0]
    
    return our_guess
        
def load_words():
    return words.all_wordle_words()
def play():
    
    print("\nWelcome to Wordle Solver AI!\n")
    
    valid_words = get_valid_words(valid_words=all_words)
    
    
    while True:
        if valid_words == []:
            print("No valid words found")
            return
        
        elif len(valid_words) == 1:
            print("*"*21)
            print(f'* Word Found: {valid_words[0]} *')
            print("*      We Won !!    *")
            print("*"*21)
            return
        
        else:
            guess = smart_guess(valid_words)
                
        if guess:
            current_word = guess
            print(f'Try: {current_word}\n')
            for letter in current_word:
                if letter in untried_letters_list:
                    untried_letters_list.remove(letter)
            
            color_code = input("Enter the color codes eg. g for green, y for yellow, b for black: ")
            print()
            
            if color_code == 'exit':
                print("Exiting...")
                return
            
            if len(color_code) != 5:
                print("Invalid color code, must be 5 characters long")
                color_code = input("Enter the color codes eg. g for green, y for yellow, b for black: ")
                
            if not re.match(r'^[gyb]{5}$', color_code):
                print("Invalid color code, must be g, y or b only")
                color_code = input("Enter the color codes eg. g for green, y for yellow, b for black: ")
                
            if color_code == 'ggggg':
                print("*"*21)
                print(f'* Word Found: {current_word} *')
                print("*      We Won !!    *")
                print("*"*21)
                return
            green_letters, yellow_letters, invalid_letters = convert_color_code(current_word, color_code)
            
            valid_words = get_valid_words(valid_words)
            
    
# Let's play the game
play()