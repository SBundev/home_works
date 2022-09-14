txt = input("введите название файла : ")
with open(txt, encoding="utf-8", mode="wt") as fid:
    while True:
        line = input()
        if line == '':
            break
        fid.write(line + '\n')
    fid.close()

if __name__ == "__main__":
    pass
