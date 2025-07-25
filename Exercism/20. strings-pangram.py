# The best known English pangram is:
# The quick brown fox jumps over the lazy dog.
# Pangram means "every letter".
import string

def is_pangram(sentence):
    letter_list = list(string.ascii_lowercase)
    
    #convert to list and lower case
    new_sentence = list(sentence.lower())

    # find common alphabets
    intersection = list(set(letter_list) & set(new_sentence))
    sorted_intersection = sorted(intersection)
    
    # if sentence has all letters of alphabet then True
    if  sorted_intersection == letter_list:
        return True
    else:
        return False
    
sentence = "a quick movement of the enemy will jeopardize five gunboats"
print(is_pangram(sentence))
