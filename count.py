from DB import *
from tablenames import tableNames
#DB1.execute('''SELECT COUNT(*) from students''')

#students_row = DB1.fetchone()[0] 

#print(students_row)
#DB2.execute('''SELECT COUNT(*) from students''')

#students_row1 = DB2.fetchone()[0] 

# Outputlist = []

# if students_row != students_row1:
#     output_tuple = (students_row,students_row1)
#     Outputlist.append(output_tuple)

# print(Outputlist)


#print(tableNames)

for tableName in tableNames:
    DB1.execute("select count(*) from "+tableName)
    DB2.execute("select count(*) from "+tableName)
    DB1_students = DB1.fetchone()[0]
    DB2_students = DB2.fetchone()[0]
    #print(DB1_students)
    if DB1_students != DB2_students:
        result = (DB1_students,DB2_students,abs(DB1_students-DB2_students),tableName)
        print(result)
        #try:
        DB3.execute("INSERT INTO table_compare(db1_count, db2_count,difference, table_name) values(%d,%d,%d,'%s');" %result)
            
        print('success')
        #except:
            #print('Insertion failed')
       #DB1.execute("INSERT INTO students(student_name, department) values('Tahmid','CSE');")
        NewPracticeDB2.commit()

#print(DB1_students)
#print(DB2_students)