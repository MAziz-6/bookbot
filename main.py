def get_word_count(file_contents):
    words = file_contents.split()
    count = 0
    for word in words:
        count += 1
    # print(count)
    return count

def sort_on(dict):
    return dict["count"]

def get_char_count(file_contents):
    char_count = {}
    for char in file_contents:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    char_list = []
    for char, count in char_count.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})
    char_list.sort(key=sort_on, reverse=True)
    return char_list

      


def main():
    with open(f"books/frankenstein.txt") as f:
        file_contents = f.read()
    word_count = get_word_count(file_contents)
    char_list = get_char_count(file_contents)
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for char in char_list:
        print(f"The '{char["char"]}' character was found {char["count"]} times")
    print("--- End report ---")
    
    

main()