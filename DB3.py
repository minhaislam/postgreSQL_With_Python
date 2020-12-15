from DB import DB3, NewPracticeDB2

try:
    DB3.execute('''create table table_compare ( id serial not null primary key,
                    DB1_count int not null,
                    DB2_count int not null,
                    difference int not null,
                    table_name varchar not null );''')

    
    NewPracticeDB2.commit()

    print("created")
except:
    print("failed")