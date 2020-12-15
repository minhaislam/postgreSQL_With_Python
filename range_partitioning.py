from DB import DB3, NewPracticeDB2

try:
    DB3.execute('''CREATE TABLE employee_salary (
                                                    id SERIAL,
                                                    ename VARCHAR(30),
                                                    salary INT,
                                                    primary key(id,salary)
                                                    
                                                )
                                                PARTITION BY RANGE (salary);

                                                create table salary_range1 partition of employee_salary for
                                                values
                                                from
                                                (10000) to (35000);
                                                
                                                create table salary_range2 partition of employee_salary for
                                                values
                                                from
                                                (36000) to (70000);''')





    NewPracticeDB2.commit()

    print("created")
except:
    print("failed")