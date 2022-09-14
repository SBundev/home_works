def longest_words(file_name):
    with open(file_name, encoding="utf-8", mode="r") as fid:
        word = fid.read().split()
        # print(word)
        # print(max(word, key=len))
        max_word = len(max(word, key=len))
        # print(max_word)
    return [w for w in word if len(w) == max_word]


if __name__ == '__main__':
    file_name = 'article.txt'
    print(longest_words(file_name))
