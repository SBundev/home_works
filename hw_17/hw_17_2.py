def longest_words(file_name):
    with open(file_name, encoding="utf-8", mode="r") as fid:
        word = fid.read().split()
    return [w for w in word if len(w) == len(max(word, key=len))]


if __name__ == '__main__':
    file_name = 'article.txt'
    print(longest_words(file_name))
