from DB import DB3, NewPracticeDB2

try:
    
    
    DB3.execute("insert into travel_agent(a_name,allocated_area) values('Samin Hossain','Puran Dhaka');")
    DB3.execute("insert into travel_agent(a_name,allocated_area) values('Hadid','CoxBazar');")


    
    
    
    NewPracticeDB2.commit()

    print("created")
except:
    print("failed")