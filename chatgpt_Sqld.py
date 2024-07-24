import sqlite3
import random
import string

class ElectronicsDatabase:
    def __init__(self, db_name='electronics.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS electronics (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def insert_product(self, product_name, price):
        self.cursor.execute('''
            INSERT INTO electronics (product_name, price)
            VALUES (?, ?)
        ''', (product_name, price))
        self.conn.commit()

    def update_product(self, product_id, product_name, price):
        self.cursor.execute('''
            UPDATE electronics
            SET product_name = ?, price = ?
            WHERE product_id = ?
        ''', (product_name, price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute('''
            DELETE FROM electronics
            WHERE product_id = ?
        ''', (product_id,))
        self.conn.commit()

    def select_all_products(self):
        self.cursor.execute('SELECT * FROM electronics')
        return self.cursor.fetchall()

def generate_sample_data():
    products = []
    for _ in range(100):
        product_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        price = round(random.uniform(10.0, 1000.0), 2)
        products.append((product_name, price))
    return products

if __name__ == "__main__":
    db = ElectronicsDatabase()

    # 샘플 데이터 생성
    sample_data = generate_sample_data()

    # 샘플 데이터 삽입
    for product_name, price in sample_data:
        db.insert_product(product_name, price)

    # 데이터 출력
    products = db.select_all_products()
    for product in products:
        print(product)
