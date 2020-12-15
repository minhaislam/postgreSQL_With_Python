from DB import DB1, NewPracticeDB

try:
    # DB1.execute("INSERT INTO students(student_name, department) values('Asif','EEE');")

    # DB1.execute("INSERT INTO teachers(teacher_name, department) values('Kabir Haque','EEE');")

    # DB1.execute("INSERT INTO teacherSalary(salary, teacher_id) values(70000,4);")
    
    DB1.execute("INSERT INTO staffs(staff_name, designation) values('rahim','guard');")

    DB1.execute("INSERT INTO staffSalary(salary, staff_id) values(15000,4);")
    
    
    NewPracticeDB.commit()

    print("created")
except:
    print("failed")