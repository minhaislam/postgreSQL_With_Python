from DB import DB2, postgres

try:
    #studens
    DB2.execute("INSERT INTO students(student_name, department) values('Rahat','EEE');")
    #teachers
    DB2.execute("INSERT INTO teachers(teacher_name, department) values('Sajib Hasan','CSE');")
    #teacherSalary
    DB2.execute("INSERT INTO teacherSalary(salary, teacher_id) values(70000,3);")
    #staffs
    DB2.execute("INSERT INTO staffs(staff_name, designation) values('Rahim','Cleaner');")
    #staffSalary
    DB2.execute("INSERT INTO staffSalary(salary, staff_id) values(15000, 2);")
    
    
    postgres.commit()

    print("created")
except:
    print("failed")