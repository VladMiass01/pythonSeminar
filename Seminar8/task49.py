def find_by_lastname(phone_book, last_name):
    filtered = list(filter(lambda x: x['Фамилия'] == last_name, phone_book))
    return filtered


def change_number(phone_book, last_name, new_number):
    filtered = list(filter(lambda x: x['Фамилия'] == last_name, phone_book))
    cn = phone_book.index(filtered[0])
    phone_book[cn]['Телефон'] = new_number
    return phone_book


def delete_by_lastname(phone_book, last_name):
    filtered = list(filter(lambda x: x['Фамилия'] == last_name, phone_book))
    cn = phone_book.index(filtered[0])
    phone_book.pop(cn)
    return phone_book


def find_by_number(phone_book, number):
    filtered = list(filter(lambda x: x['Телефон'] == number, phone_book))
    return filtered


def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    record = dict(zip(fields, user_data))
    print(record)
    phone_book.append(record)
    

def read_txt(filename): 
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phin:
        for line in phin:
            record = line.split(',')
            for k in range(len(record)):
                record[k] = record[k].strip()
            record = dict(zip(fields, record))
            phone_book.append(record)
    phone_book.sort(key = lambda x: x['Фамилия'])
    return phone_book


def write_txt(filename, phone_book):
    with open('phonebook.txt', 'w', encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s = '' 
            for v in phone_book[i].values():
                s += v + ','
            phout.write(f'{s[:-1]}\n')
            

def work_with_phonebook(filename):
    choice = show_menu()
    phone_book = read_txt(filename)
    mod = False
    while choice < 7:
        if choice == 1:
            for i in range(len(phone_book)):
                print(phone_book[i])
        elif choice == 2:
            last_name = input('lastname ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('lastname ')
            new_number = input('new number ')
            mod = True
            print(change_number(phone_book, last_name, new_number))
        elif choice == 4:
            mod = True
            last_name = input('lastname ')
            print(delete_by_lastname(phone_book, last_name))
        elif choice == 5:
            number=input('number ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('new data ').split()
            mod = True
            add_user(phone_book, user_data)
        choice = show_menu()
    if mod:
        write_txt(filename, phone_book)
    return


def show_menu():
    print('1. Распечатать справочник',
          '2. Найти телефон по фамилии',
          '3. Изменить номер телефона',
          '4. Удалить запись',
          '5. Найти абонента по номеру телефона',
          '6. Добавить абонента в справочник',
          '7. Закончить работу', sep = '\n')
    choice = int(input())
    return choice


filename = 'phonebook.txt'
work_with_phonebook(filename)