def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def print_report(file_path):
    with open(file_path) as f:
        content = f.read()
        
        words = content.split()
        word_count = len(words)
        
        char_count = count_characters(content)
        
        sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
        
        print(f"--- Begin report of {file_path} ---")
        print(f"{word_count} words found in the document\n")
        
        for char, count in sorted_char_count:
            print(f"The '{char}' character was found {count} times")
        
        print("--- End report ---")

print_report("books/frankenstein.txt")