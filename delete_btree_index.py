from DB import DB4, dvdrental

try:
    DB4.execute('''drop index rental_ids;''')

    

    print('btree index deleted')
except:
    print('failed')
