import pickle


class Kab:
    # cabinet phoone number int, two symbols
    phone = None
    num = None
    name = None
    surname = None


# open database to read dates from it
f = open('students.dat', 'rb')
# all data base in text format
Ka = pickle.load(f)
f.close()

while True:
    # database command processing
    try:
        n = int(input("""
        ______________________________________
        _ Enter number:                      _
        _     1: Вывод по номеру телефона    _
        _     2: Вывод по номеру кабинета    _
        _     3: Вывод по Фамилии            _
        _     4: Дабл эл                     _
        _     5: Вывод БД                    _
        _     6: Удаление эл                 _
        _     7: Завершение прогграмы        _
        ______________________________________
        """))
    except TypeError:
        print("This command isn't possible!!!! "
              "Try again!!")
        break

    if n == 1:
        # input telephone number for cabinet, that you find
        ph = input()
        # find and print out
        for i in range(len(Ka)):
            if ph == Ka[i].phone:
                print(Ka[i].num, end=": ")
                for fio in range(len(Ka[i].name)):
                    if fio != len(Ka[i].name) - 1:
                        print(Ka[i].name[fio], Ka[i].surname[fio], end=", ")
                    else:
                        print(Ka[i].name[fio], Ka[i].surname[fio])
    elif n == 2:
        # cabinet number
        nu = input()
        for i in Ka:
            if nu == i.num:
                print(i.phone)
    elif n == 3:
        # surname
        sur = input("Введите Фамилию ").strip()
        for i in range(len(Ka)):
            for j in range(len(Ka[i].surname)):
                if sur == Ka[i].surname[j]:
                    print(Ka[i+j].phone, Ka[i+j].num)
    elif n == 4:
        # input new string to data base
        f = open('students.dat', 'ab')
        Ka = Kab()
        Ka.phone = input("Введите номер ").strip()
        Ka.num = input("Введите номер кабинета ").strip()
        kol = int(input("Введите кол-во новых людей ").strip())
        Ka.name = []
        Ka.surname = []

        # append people to cabinet
        for i in range(kol):
            b = list(input("Введите человека(ФИ через пробел) ").split())
            Ka.name.append(b[0])
            Ka.surname.append(b[1])
        Ka.append(Ka)
        pickle.dump(Ka, f)
        f.close()

    elif n == 5:
        # output data base
        for i in Ka:
            print(i.phone, i.num, *i.name, *i.surname)

    elif n == 6:
        # delete person in data
        f = open('students.dat', 'ab')

        surname, name = input("Введите человека(ФИ через пробел) ").split()
        is_find = False
        for i in range(len(Ka)):
            for j in range(len(Ka[i].surname)):
                if Ka[i].surname[j] == surname and Ka[i].name[j] == name:
                    is_find = True
                    Ka[i].surname.pop(j)
                    Ka[i].name.pop(i)
                    break
            if is_find == True:
                break
        pickle.dump(Ka, f)
        f.close()
    elif n == 7:
        break
    else:
        print('Введите снова')
        pass

if __name__ == "__main__":
    pass
