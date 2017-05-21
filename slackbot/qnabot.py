import sqlite3
from random import randint

class DAO:
    db = 'qna.db'
    create_query = '''create table qna
                            (ID INTEGER PRIMARY KEY   AUTOINCREMENT,
                            question varchar(100),
                            answer varchar(1000));'''
    insert_query = "insert into qna (question, answer) values (?,?)"
    select_all_query = 'select ID, question, answer from qna'
    select_query = "select ID, question, answer from qna where question like ?"

    res = []
    count = 0

    def __init__(self):
        self.conn = sqlite3.connect(self.db)
        self.get_all()

    def create_table(self):
        try:
            self.conn.execute(self.create_query)
        except:
            print("Table Already Present")

    def save_data(self, q, a):
        self.conn.execute(self.insert_query, (q, a))
        self.conn.commit()

    def get_all(self):
        curr = self.conn.execute(self.select_all_query)
        for row in curr:
            self.res.append(row)
        return self.res

    def get_one(self):
        n = len(self.res)
        self.count = (self.count+1)%n
        return self.res[self.count]

    '''def get_data(self, q):
        res = []
        cur = self.conn.execute(self.select_query, ('%'+q+'%',))
        for row in cur:
            res.append(row)
        print(res)
        return res
    '''

db = DAO()

def show_all():
    rows = db.get_all()
    for row in rows:
        print('%s] q : %s || a : %s' % (row[0], row[1], row[2]))

def test():
    db.count = -1
    print("start test from %d" % (db.count + 1))

def show():
    print('%d a : %s' %(db.count, db.res[db.count][2]))

def next():
    db.count = (db.count + 1) % len(db.res)
    print('%d] q : %s' % (db.count, db.res[db.count][1]))

def previous():
    db.count = (db.count-1)
    if db.count < 0:
        db.count = len(db.res) - 1
    print('%d] q : %s' % (db.count, db.res[db.count][1]))

def goto(idx):
    i = int(idx)
    if i >= 0 and i<len(db.res):
        db.count = int(idx)
        print('%d] q : %s' % (db.count, db.res[db.count][1]))
    else:
        print('GO TO not in range')

def rand():
    db.count = randint(0, len(db.res))
    print('start test from %d' %(db.count))

d = {'q' : '', 'a': ''}
def preview():
    print('q : %s \na : %s' % (d['q'], d['a']))

def save():
    db.save_data(d['q'], d['a'])
    preview()

def _help():
    print('help')

print('''Welcome to flashcard!!!
        Happy Learning!!!
        ''')
while True:
    inp = input()
    if inp == 'show all':
        show_all()
    elif inp == 'test':
        test()
    elif inp == 'show':
        show()
    elif inp == 'next':
        next()
    elif inp == 'previous':
        previous()
    elif inp.startswith('goto'):
        goto(inp.split(' ')[1])
    elif inp == 'random' or inp == 'rand':
        rand()
    elif inp.startswith('q:'):
        d['q'] = inp[2:]
    elif inp.startswith('a:'):
        d['a'] = inp[2:]
    elif inp == 'preview':
        preview()
    elif inp == 'save':
        save()
    elif inp == 'help':
        _help()
    elif inp == 'exit':
        print('Good Bye!!!')
        break
    else:
        print('Do not understand the command')
