# kirk staver 2025 boot.dev project 1

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    sorted_list = create_sorted_char_list(text)
    print(str(sorted_list))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_text_word_count(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_dict = {}
    lower_case_text = text.lower()
    for c in lower_case_text:
        if c in char_dict:
            char_dict[c] = char_dict[c] + 1
        else:
            char_dict[c] = 1
    return char_dict

def create_sorted_char_list(text):
    sorted_list = []
    char_dict = count_chars(text)
    for k in char_dict:
        if k.isalpha():
            sorted_list.append((k,char_dict[k]))
    sorted_list.sort(reverse=True,key= lambda x: x[1])
    return sorted_list

main()