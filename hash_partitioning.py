from DB import DB3, NewPracticeDB2

try:
    DB3.execute('''create table travel_agent ( id serial,
                    a_name varchar(100),
                    allocated_area varchar(100),
                    primary key (id) ) partition by HASH(id);

                    create table dhaka_area partition of travel_agent for
                    values with (modulus 3, remainder 0);

                    create table chittagong_area partition of travel_agent for
                    values with (modulus 3, remainder 1);''')





    NewPracticeDB2.commit()

    print("created")
except:
    print("failed")