import pickle


class Kab:
    """
    data base
    """
    phone = None
    num = None
    name = None
    surname = None


# read new dates for our database
f = open("students.txt", 'r', encoding='utf-8')
# page in database
St = []
# list of people in this room
b = []
while True:
    # read new dates
    x = f.readline()
    if not x:
        break
    # init
    x = x.split(' ', 2)
    st = Kab()
    st.phone = x[0]
    st.num = x[1]
    b = x[2].split(" ")
    st.surname = [b[0], b[2]]
    st.name = [b[1], b[3]]

    # append ordered dates to St
    St.append(st)
    print(st.phone, st.num, st.name, st.surname)

# entry to database a new page
file_out = open('students.dat', 'wb')
pickle.dump(St, file_out)
file_out.close()
f.close()

if __name__ == "__main__":
    pass