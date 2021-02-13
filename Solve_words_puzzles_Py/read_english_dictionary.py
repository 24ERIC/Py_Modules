def load_words():
    with open('words_alpha.txt') as word_file: #change file path
        valid_words = set(word_file.read().split())

    return valid_words


if __name__ == '__main__':
    english_words = load_words()
    # demo print
    for a in english_words:
        if len(a) == 8 and a[2:4] == "co" and a[5]=="a" and a[7]=="e":		#change condition
            print(a)
                
