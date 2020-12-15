from DB import DB3, NewPracticeDB2

try:
    DB3.execute('''CREATE TABLE cities
                                (
                                id serial,
                                city_name  varchar(100),
                                country     varchar(100),
                                PRIMARY KEY (id,country)
                                )
                                PARTITION BY LIST(country);
                                CREATE TABLE EUROPE PARTITION of cities FOR VALUES IN('GERMANY','SPAIN');
                                CREATE TABLE ASIA PARTITION of cities FOR VALUES IN('TURKEY','INDIA');
                                CREATE TABLE AFRICA PARTITION of cities FOR VALUES IN('ANGOLA','BENIN');
                                CREATE TABLE NORTHAMERICA PARTITION of cities FOR VALUES IN('US','MEXICO');
                                CREATE TABLE SOUTHAMERICA PARTITION of cities FOR VALUES IN('ARGENTINA','ECUADOR');
                                CREATE TABLE AUSTRALIA PARTITION of cities FOR VALUES IN('AUSTRALIA','FIJI');''')





    NewPracticeDB2.commit()

    print("created")
except:
    print("failed")