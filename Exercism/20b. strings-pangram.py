def is_pangram(sentence):
    import string
    letter_list = (string.ascii_lowercase)
    new_sentence = list(sentence.lower())
    for char in letter_list:
        print(char)
        if char not in new_sentence:
            return False
    return True
    
sentence = "a quick movement of the enemy will jeopardize five gunboats"
print(is_pangram(sentence))