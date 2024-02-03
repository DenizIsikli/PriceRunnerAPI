import sqlite3


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = self.create_connection(db_name)
        self.create_table()

    @staticmethod
    def create_connection(db_name):
        try:
            conn = sqlite3.connect(db_name, check_same_thread=False)
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise e

    def create_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Products (
                    name TEXT NOT NULL,
                    info TEXT,
                    price INTEGER,
                    link TEXT
                )
            ''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    @staticmethod
    def clean_price(price_str):
        return int(''.join(filter(str.isdigit, price_str)))

    def add_products(self, products):
        try:
            cursor = self.conn.cursor()

            product_data = [
                (product.name, product.info, self.clean_price(product.price), product.link)
                for product in products
            ]

            cursor.executemany('''
                INSERT INTO Products (name, info, price, link)
                VALUES (?, ?, ?, ?)
            ''', product_data)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error adding products: {e}")

    def get_product_by_name(self, product_name):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Products WHERE name = ?", (product_name,))
            result = cursor.fetchall()
            return result
        except sqlite3.Error as e:
            print(f"Error retrieving product: {e}")
            return None

    def update_product_price(self, product_name, new_price):
        try:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE Products SET price = ? WHERE name = ?", (self.clean_price(new_price), product_name))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error updating product price: {e}")

    def delete_product(self, product_name):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM Products WHERE name = ?", (product_name,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error deleting product: {e}")

    def clear_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM Products")
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error clearing table: {e}")

    def close_connection(self):
        self.conn.close()


if __name__ == '__main__':
    db = Database('Pricerunner.db')
    db.clear_table()
    db.close_connection()
