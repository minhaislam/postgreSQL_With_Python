from DB import DB1, NewPracticeDB

try:
    DB1.execute('''create table students ( id serial not null primary key,
                    student_name varchar(50) not null,
                    department varchar(50) not null );''')

    DB1.execute('''create table teachers ( id serial not null primary key,
                    teacher_name varchar(50) not null,
                    department varchar(50) not null );''')
    
    DB1.execute('''create table teacherSalary (
                    id serial not null primary key,
                    salary int not null,
                    teacher_id int references teachers(id) on delete cascade );''')

    DB1.execute('''create table staffs ( 
                    id serial not null primary key,
                    staff_name varchar(50) not null,
                    designation varchar(50) not null );''')
    
    DB1.execute('''create table staffSalary (
                    id serial not null primary key,
                    salary int not null,
                    staff_id int references staffs(id) on delete cascade );''')
    
    NewPracticeDB.commit()
    students = "create table students ( id serial not null primary key,student_name varchar(50) not null,department varchar(50) not null );"

    

    print("created")
except:
    print("failed")