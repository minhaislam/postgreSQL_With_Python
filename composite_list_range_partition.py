from DB import DB3, NewPracticeDB2

try:
    DB3.execute('''create table employee_journal ( id serial,
                        ename varchar(100),
                        department varchar(100),
                        join_date date,
                        primary key (id,
                        department,join_date) ) partition by LIST(department);
                        
                        create table employee_it partition of employee_journal for
                        values in ('Developer',
                        'Data') partition by range (join_date);
                        create table employee_marketing partition of employee_journal for
                        values in ('Soical_Media',
                        'Business') partition by range (join_date);
                        create table employee_it_june partition of employee_it for
                        values
                        from
                        ('01-JUN-2020') to ('30-JUN-2020');

                        create table employee_it_july partition of employee_marketing for
                        values
                        from
                        ('01-JUL-2020') to ('30-JUL-2020');''')





    NewPracticeDB2.commit()

    print("created")
except:
    print("failed")