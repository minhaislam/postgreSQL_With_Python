from DB import *
from tablenames import tableNames

DB1.execute("SELECT * from students")
rows = DB1.fetchall()
print(rows)
        
for row in rows:
    new_row = list(row)
    new_row.pop(0)
    new_row_values = tuple(new_row)
    print(new_row_values)
        # DB2.execute("INSERT INTO "+ tableName +" ( " + columnlist[0] + "," + columnlist[1] +") values('%s','%s');" %new_row_values)
        # postgres.commit()
            

        
           
    



