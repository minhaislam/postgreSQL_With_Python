import psycopg2


try:
    #destination database
    NewPracticeDB = psycopg2.connect(database = "NewPracticeDB",
                                    user = "postgres",
                                    password = "12345678",
                                    host= "localhost",
                                    port = "5432",
                                    
                                    )
    #source table
    postgres = psycopg2.connect(database = "postgres",
                                    user = "postgres",
                                    password = "12345678",
                                    host= "localhost",
                                    port = "5432",
                                    
                                    )

    NewPracticeDB2 = psycopg2.connect(database = "NewPracticeDB2",
                                    user = "postgres",
                                    password = "12345678",
                                    host= "localhost",
                                    port = "5432",
                                    
                                    )
    

    dvdrental = psycopg2.connect(database = "dvdrental",
                                    user = "postgres",
                                    password = "12345678",
                                    host= "localhost",
                                    port = "5432",
                                    
                                    )

    DB1 = NewPracticeDB.cursor()

   

    #calling the cusor
    DB2 = postgres.cursor()

    DB3 = NewPracticeDB2.cursor()

    DB4 = dvdrental.cursor()




    

    print("success")
except:
    print("failed")