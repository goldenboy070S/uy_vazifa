import psycopg2
from decimal import Decimal


class ExamDB:
    def __init__(self, database, user, password, host='localhost', port='5432'):
        self.conn = psycopg2.connect(database=database,
                                user=user,
                                password=password,
                                host=host,
                                port=port)

        self.cursor = self.conn.cursor()
    def projectDB(self):
        name = 'Samsung A32'
        price = 12.45869
        priname = (round(price, 2), name)
        self.cursor.execute("INSERT INTO product (price, _name) VALUES (%s, %s);", priname)
        self.conn.commit()
        self.conn.rollback()
    def decimalkod(self, x, y):
        s = Decimal(str(x))
        b = Decimal(str(y))
        if isinstance(x, float) and isinstance(y, float):
            natija = s + b
            return Decimal(natija)
        else:
            raise TypeError('Kiritilgan qiymatning  tipi float bolishi kerak')


exe = ExamDB('exam', 'postgres', 'sardor2007a')
# print(exe.decimalkod(float(input('birinchi sonni kiriting')), float(input('ikkinchi sonni kiriting'))))
print(exe.projectDB())
