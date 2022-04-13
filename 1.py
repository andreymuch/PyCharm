import pickle
class Kab:
    phone = None
    num = None
    name = None
    surn = None
f = open("students.txt", 'r', encoding='utf-8')
St = []
b = []
while True:
    x = f.readline()
    if not x:
        break
    x = x.split(' ', 2)
    st = Kab()
    st.phone = x[0]
    st.num = x[1]
    b = x[2].split(" ")
    st.surn = [b[0], b[2]]
    st.name = [b[1], b[3]]
    St.append(st)
    print(st.phone, st.num, st.name, st.surn)
fout = open('students.dat', 'wb')
pickle.dump(St, fout)
fout.close()
f.close()