import sqlite3

conn = sqlite3.connect('test.db')

print('Opened db ok')

#conn.execute('''create table flashcard(ID int primary key not null,
#                                        question char(10000),
#                                        answer char(10000));''')


conn.execute("insert into flashcard values "
             "('3', 'first question', 'first answer')")


c = conn.execute("select * from flashcard")
for row in c:
    print(row)

print('Table created')
conn.commit()
conn.close()

