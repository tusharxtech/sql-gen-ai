import sqlite3

connection=sqlite3.connect("sqldb.db")
cursor=connection.cursor()

cursor.execute(
"CREATE TABLE products (product_id INT PRIMARY KEY,product_name VARCHAR(50),category VARCHAR(50),price INT,stock_quantity INT);"
)
cursor.execute(
    
    '''INSERT INTO products (product_id, product_name, category, price, stock_quantity)
    VALUES(1, 'Laptop', 'Electronics', 75000.00, 10),
    (2, 'Smartphone', 'Electronics', 45000.00, 25),
    (3, 'Headphones', 'Accessories', 2500.00, 50),
    (4, 'Keyboard', 'Accessories', 1500.00, 40),
    (5, 'Monitor', 'Electronics', 12000.00, 15),
    (6, 'Chair', 'Furniture', 5000.00, 20),
    (7, 'Desk', 'Furniture', 8000.00, 12),
    (8, 'Water Bottle', 'Lifestyle', 300.00, 100);
    '''
)

connection.commit()
connection.close()