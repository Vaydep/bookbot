def main():
    path_to_file = "books/frankenstein.txt"
    text = get_file_contents(path_to_file)
    words = split_text_to_words(text)
    chars_count = get_character_count(words)
    print_report(path_to_file, get_word_count(words), chars_count)

def get_file_contents(path):
    with open(path) as f:
        return f.read()    

def split_text_to_words(text):
    return text.split()

def get_word_count(words):
    return len(words)

def get_character_count(words):
    characters = { }
    for word in words:
        for char in word:
            if char.lower() in characters:
                characters[char.lower()] += 1
            else:
                characters[char.lower()] = 1

    return sorted(characters.items(), key=lambda t: -t[1])

def print_report(path, words, chars):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    print("")
    for char in chars:
        if char[0].isalpha():
            print(f"The '{char[0]}' character was found {char[1]} times")

    print("--- End report ---")

main()