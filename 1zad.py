searched_book = input()
next_book = input()
is_book_found = False
broi = 0
while next_book != 'No More Books':
    if next_book == searched_book:
        is_book_found = True
        print(f'You checked {broi} books and found it.')
        break
    broi += 1
    next_book = input()

if not is_book_found:
    print('The book you search is not here!')
    print(f'You checked {broi} books.')
