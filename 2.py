import pickle


class Kab:
    phone = None
    num = None
    name = None
    surname = None


# open database to read dates from it
f = open('students.dat', 'rb')
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
        _     6: Завершение прогграмы        _
        ______________________________________
        """))
    except TypeError:
        print("This command isn't possible!!!! "
              "Try again!!")
        break

    if n == 1:
        ph = input()
        for i in range(len(Ka)):
            if ph == Ka[i].phone:
                print(Ka[i].num, end=": ")
                for fio in range(len(Ka[i].name)):
                    if fio != len(Ka[i].name) - 1:
                        print(Ka[i].name[fio], Ka[i].surname[fio], end=", ")
                    else:
                        print(Ka[i].name[fio], Ka[i].surname[fio])
    elif n == 2:
        nu = input()
        for i in Ka:
            if nu == i.num:
                print(i.phone)
    elif n == 3:
        sur = input("Введите Фамилию").strip()
        for i in range(len(Ka)):
            for j in range(len(Ka[i].surname)):
                if sur == Ka[i].surname[j]:
                    print(Ka[i+j].phone, Ka[i+j].num)
    elif n == 4:
        f = open('students.dat', 'ab')
        st = Kab()
        st.phone = input("Введите номер").strip()
        st.num = input("Введите номер кабинета").strip()
        kol = int(input("Введите кол-во новых людей").strip())
        st.name = []
        st.surname = []

        for i in range(kol):
            b = list(input("Введите человека(ФИ через пробел)").split())
            st.name.append(b[0])
            st.surname.append(b[1])
        Ka.append(st)
        pickle.dump(Ka, f)
        f.close()
    elif n == 5:
        for i in Ka:
            print(i.phone, i.num, *i.name, *i.surname)
    elif n == 6:
        break
    else:
        print('Введите снова')
        pass

if __name__ == "__main__":
    pass