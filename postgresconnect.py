import psycopg2

connection = psycopg2.connect(
        user="postgres",
        password="artha@2024",
        host="localhost",
        port=5432,
        database="newdb"
    )

if connection:
    print("Connected to PostgreSQL database")

    # Perform database operations here...
cur=connection.cursor()
#cur.execute("create table emp(eid int,ename varchar(20),esalary int,erol varchar);")
"""empstr="insert into emp(eid,ename,esalary,erol) values(%s,%s,%s,%s);"
records=[(1,'emp1',10000,'bknd'),(2,'emp2',20000,'ftnd'),(3,'emp3',30000,'fullstack')]
cur.executemany(empstr,records)"""
#cur.execute("SELECT * FROM information_schema.tables WHERE table_schema = 'public';")
#cur.execute("select * from emp")
cur.execute("select sum(total_amount) as total from orders")
tables=cur.fetchall()
for i in tables:
    print(i)


connection.commit()




connection.close()
print("connection closed")


