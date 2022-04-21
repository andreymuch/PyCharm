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
    # init, we add new database to the class Kab objects and append new object of this class to St list
    x = x.split(' ', 2)
    st = Kab()
    st.phone = x[0]
    st.num = x[1]
    b = x[2].split(" ")
    st.surname = [b[0], b[2]]
    st.name = [b[1], b[3]]

    # append ordered dates to St
    St.append(st)
    # print dates, that had been loaded to the database in console
    print(st.phone, st.num, st.name, st.surname)

# open database file
file_out = open('students.dat', 'wb')
# entry to database a new page
pickle.dump(St, file_out)
# close files to safe result and correct end of program
file_out.close()
f.close()

# for testing
if __name__ == "__main__":
    pass
