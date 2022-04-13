import pickle
class Kab:
    phone=None
    num = None
    name = None
    surn = None
f = open('students.dat', 'rb')
Ka = pickle.load(f)
f.close()
while True:
    print()
    print("Введите число")
    print("1-Вывод по номеру телефона")
    print("2-Вывод по номеру кабинета")
    print("3-Вывод по Фамилии")
    print("4-Дабл эл")
    print("5-Вывод БД")
    print("6-Завершение прогграмы")
    n=int(input())
    if n == 1:
        ph = input()
        for i in range(len(Ka)):
            if ph == Ka[i].phone:
                print(Ka[i].num, Ka[i].name[i], Ka[i].surn[i], Ka[i].name[i+1], Ka[i].surn[i+1])
    elif n == 2:
        nu = input()
        for i in Ka:
            if nu == i.num:
                print(i.phone)
    elif n == 3:
        print("Введите Фамилию")
        sur = input()
        for i in range(len(Ka)):
            for j in range(len(Ka[i].surn)):
                if sur == Ka[i].surn[j]:
                    print(Ka[i+j].phone, Ka[i+j].num)
    elif n == 4:
        f = open('students.dat', 'ab')
        st = Kab()
        print("Введите номер")
        st.phone = input()
        print("Введите номер кабинета")
        st.num = input()
        print("Введите кол-во новых людей")
        kol = int(input())
        st.name = []
        st.surn = []
        for i in range(kol):
            print("Введите человека(ФИ через пробел)")
            b = list(input().split())
            st.name.append(b[0])
            st.surn.append(b[1])
        Ka.append(st)
        pickle.dump(Ka, f)
        f.close()
    elif n == 5:
        for i in Ka:
            print(i.phone, i.num, *i.name, *i.surn)
    elif n == 6:
        break
    else:
        print('Введите снова')
        pass
