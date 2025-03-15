def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    num_characters = {}
    for character in text:
        lowered = character.lower()
        if lowered in num_characters:
            num_characters[lowered] += 1
        else:
            num_characters[lowered] = 1
    return num_characters

def sort_num_characters(dict):
    return dict["count"]