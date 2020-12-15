from DB import DB3, NewPracticeDB2

try:
    
    
    DB3.execute("insert into employee_journal (ename,department,join_date) values ('Rahat Hassan','Data','15-JUN-2020');")
    DB3.execute("insert into employee_journal (ename,department,join_date) values ('Al Amin','Business','01-JUL-2020');")
    DB3.execute("insert into employee_journal (ename,department,join_date) values ('Maritn Howlader','Soical_Media','03-JUL-2020');")

    
    
    
    NewPracticeDB2.commit()

    print("created")
except:
    print("failed")