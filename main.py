def get_word_count(file_contents):
    words = file_contents.split()
    count = 0
    for word in words:
        count += 1
    print(count)



def main():
    with open(f"books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
    # return file_contents

    get_word_count(file_contents)

main()