k = {i for i in range(1, 41)}  # К-во учеников в классе
book_a = {i for i in range(1, 26)}
book_b = {i for i in range(max(book_a)+1, max(book_a)+23)}
book_c = {i for i in range(max(book_b)+1, max(book_b)+23)}
book_a_or_b = {i for i in range(1, 34)}
book_a_or_c = {i for i in range(1, 33)}
book_b_or_c = {i for i in range(1, 32)}
read_abc = {i for i in range(1, 11)}
read_ab = len(book_a | book_b) - len(book_a_or_b) - len(read_abc)
read_ac = len(book_a | book_c) - len(book_a_or_c) - len(read_abc)
read_bc = len(book_b | book_c) - len(book_b_or_c) - len(read_abc)
n = read_bc + read_ac + read_ab
read_a = len(book_a) - read_ab - read_ac - len(read_abc)
read_b = len(book_b) - read_ab - read_bc - len(read_abc)
read_c = len(book_c) - read_bc - read_ac - len(read_abc)
read_a_or_b_or_c = read_a + read_b + read_c
unread = len(k) - read_a_or_b_or_c - n - len(read_abc)
print("В классе", n, "учеников прочитали по две книги")
print("В классе ", read_a_or_b_or_c, "учеников, прочитали только одну книгу")
print("В классе", unread, "ученика, не прочитали ни одну книгу")
