from DB import DB1, NewPracticeDB

try:
    DB1.execute("SELECT * from students")

    rows = DB1.fetchall()
    print("Student List")
    for row in rows:
        print("ID: "+ str(row[0]))
        print("Name: "+ (row[1]))
        print("Depertment: "+ str(row[2]))
        print("\n")
    DB1.execute("SELECT * from teachers")

    rows2 = DB1.fetchall()
    print("Teacher List")
    for row in rows2:
        print("ID: "+ str(row[0]))
        print("salary: "+ (row[1]))
        print("teacher_ID: "+ str(row[2]))
    #print("created")
except:
    print("failed")