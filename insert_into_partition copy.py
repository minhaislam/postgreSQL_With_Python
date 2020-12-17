from DB import DB3, NewPracticeDB2

try:
    
    
    DB3.execute("insert into cities(city_name,country) values ('Delhi', 'INDIA');")
    DB3.execute("insert into cities(city_name,country) values ('Istanbul', 'TURKEY');")
    DB3.execute("insert into cities(city_name,country) values ('Tijuana', 'MEXICO');")

    
    
    
    NewPracticeDB2.commit()

    print("created")
except:
    print("failed")