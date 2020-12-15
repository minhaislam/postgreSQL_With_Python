from DB import DB3, NewPracticeDB2

try:
    
    
    DB3.execute("insert into employee_salary(ename,salary) values('habib',30000);")
    DB3.execute("insert into employee_salary(ename,salary) values('habib',60000);")


    
    
    
    NewPracticeDB2.commit()

    print("created")
except:
    print("failed")