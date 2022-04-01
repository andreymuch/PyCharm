import pickle
class Stud:
    fam=None
    name=None
    surn=None
    bal=None
f=open('students.dat','rb')
St= pickle.load(f)
f.close()
while True:
    print("Введите число")
    print("1-Сортировка по ср. арифм")
    print("2-Студенты с 2")
    print("3-Добавл эл")
    print("4-Вывод БД")
    print("5-Завершение прогграмы")
    n=int(input())
    if n==1:
        St.sort(key=lambda x:sum(x.bal)/len(x.bal),reverse=True)
        for i in St:
            print(i.fam,i.name,i.surn,*i.bal)
    elif n==2:
        for i in St:
            if 2 in i.bal:
                print(i.fam,i.name,i.surn,*i.bal)
    elif n==3:
        f=open('students.dat','ab')
        st=Stud()
        st.fam=input()
        st.name=input()
        st.surn=input()
        st.bal=list(map(int,input().split()))
        St.append(st)
        pickle.dump(St,f)
        f.close()
    elif n==4:
        for i in St:
            print(i.fam,i.name,i.surn,*i.bal)
    elif n==5:
        break
    else:
        print('Введите снова')
        pass
