import sqlite3
conn = sqlite3.connect('students.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()
c.executescript("
    DROP TABLE IF EXISTS class;
    CREATE TABLE IF NOT EXISTS class (
    id INTEGER PRIMARY KEY ASC,
    name varchar(250) NOT NULL,
    profile varchar(250) DEFAULT ''
    )")
c.executescript('''
    DROP TABLE IF EXISTS student;
    CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY ASC,
    first_name varchar(250) NOT NULL,
    last_name varchar(250) NOT NULL,
    age INTEGER NOT NULL,
    class_id INTEGER NOT NULL,
    FOREIGN KEY(class_id) REFERENCES class(id)
    )''')
classes = (
    (None, '1A', 'Humanistyczny'),
    (None, '1B', 'Ścisły')
)
c.executemany('INSERT INTO class VALUES(?,?,?)', classes)
c.execute('SELECT id FROM class WHERE name = ?', ('1A',))
class1A_id = c.fetchone()[0]
students_1A = (
    (None, 'Adam', 'Bednarski', 18, class1A_id),
    (None, 'Rafał', 'Nowak', 17, class1A_id),
    (None, 'Kamil', 'Kowalski', 17, class1A_id),
    (None, 'Dawid', 'Ziobro', 19, class1A_id),
)
c.executemany('INSERT INTO student VALUES(?,?,?,?,?)', students_1A)
c.execute('SELECT id FROM class WHERE name = ?', ('1B',))
class1B_id = c.fetchone()[0]
students_1B = (
    (None, 'Maciej', 'Szyluk', 18, class1B_id),
    (None, 'Arkadiusz', 'Operacz', 16, class1B_id),
)
c.executemany('INSERT INTO student VALUES(?,?,?,?,?)', students_1B)
conn.commit()

'''wyswietlanie calej bazy danych:'''


def read_db():
    c.execute(
        '''
    SELECT student.id, first_name, last_name, age, name FROM student, class
    WHERE student.class_id = class.id
''')
    students = c.fetchall()
    for student in students:
        print(student['id'], student['first_name'],
              student['last_name'], student['age'], student['name'])
    print()


read_db()

'''wyswietlenie uczniow powyzej 17 roku zycia:'''


c.execute(
    '''
    SELECT student.id, first_name, last_name, age, name FROM student, class
    WHERE student.class_id = class.id AND student.age > 17
''')
students = c.fetchall()
for student in students:
    print(student['id'], student['first_name'],
          student['last_name'], student['age'], student['name'])
print()

'''wyswietlenie uczniow z klasy o profilu: ścisły:'''


c.execute(
    '''
    SELECT student.id, first_name, last_name, age, name FROM student, class
    WHERE student.class_id = class.id AND class.profile = 'Ścisły'
''')

students = c.fetchall()
for student in students:
    print(student['id'], student['first_name'],
          student['last_name'], student['age'], student['name'])
print()

'''aktualizacja rekordu'''


c.execute('SELECT id FROM class WHERE name = ?', ('1B',))
class_id = c.fetchone()[0]
c.execute('UPDATE student SET class_id=? WHERE id=?', (class_id, 4))


'''usuniecie rekodu'''


def del_record(student_id):
    c.execute('DELETE FROM student WHERE id=?', (student_id,))


del_record(2)
conn.commit()
read_db()
