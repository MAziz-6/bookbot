def get_word_count(file_contents):
    words = file_contents.split()
    count = 0
    for word in words:
        count += 1
    print(count)

def get_char_count(file_contents):
    char_count = {}
    for char in file_contents:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

    


def main():
    with open(f"books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
    # return file_contents
    # get_word_count(file_contents)
    char_count = get_char_count(file_contents)
    print(char_count)
    

main()