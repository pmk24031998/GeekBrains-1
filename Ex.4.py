def rewrite_file():
    num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    new_text = []
    try:
        with open('Ex.4.txt', 'r+', encoding="utf-8") as file:
            with open('Ex.4.2.txt', 'r+', encoding="utf-8") as new_file:
                l = file.readlines()
                for i in l:
                    i = i.split(' ', 1)
                    new_text.append(num[i[0]] + ' ' + i[1])
                new_file.writelines(new_text)
    except FileNotFoundError:
        return 'Файл не найден.'
rewrite_file()