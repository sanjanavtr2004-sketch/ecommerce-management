import sqlite3
import os

DB_FILE = "ecommerce.db"
connection = sqlite3.connect(DB_FILE)
# print("ecommerce file connected successfully")
def connect_db():
    connection = sqlite3.connect(DB_FILE)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def init_db():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            phone TEXT NOT NULL,
            gender TEXT,
            address TEXT,
            city TEXT,
            state TEXT,
            pincode TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT NOT NULL
        )
        """
    )  
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_id INTEGER NOT NULL,
            product_name TEXT NOT NULL,
            brand TEXT,
            price REAL NOT NULL,
            status TEXT DEFAULT 'Available',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(category_id) REFERENCES categories(id)
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS cart(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            added_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(product_id) REFERENCES products(id)
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            order_date TEXT NOT NULL,
            total_amount REAL NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
        """   
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS order_items(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY(product_id) REFERENCES products(id)
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE returns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            return_reason TEXT,
            return_status TEXT DEFAULT 'Pending',
            return_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (order_id) REFERENCES orders(id),
            FOREIGN KEY (product_id) REFERENCES products(id),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """
    )
    connection.commit()
    connection.close()

def add_user():
    connection = connect_db()
    cursor = connection.cursor()
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    gender = input("Enter Gender (Male/Female/Other): ")
    address = input("Enter Address: ")
    city = input("Enter City: ")
    state = input("Enter State: ")
    pincode = input("Enter Pincode: ")
    cursor.execute("""
        INSERT INTO users
        (name, email, phone, gender, address, city, state, pincode)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, email, phone, gender, address, city, state, pincode))
    connection.commit()
    connection.close()
    print("User added successfully!")
def add_category():
    connection = connect_db()
    cursor = connection.cursor()
    category_name = input("Enter Category Name: ")
    cursor.execute("""
        INSERT INTO categories (category_name)
        VALUES (?)
    """, (category_name,))
    connection.commit()
    connection.close()
    print("Category added successfully!")
def add_product():
    connection = connect_db()
    cursor = connection.cursor()
    category_id = int(input("Enter Category ID: "))
    product_name = input("Enter Product Name: ")
    brand = input("Enter Brand Name: ")
    price = float(input("Enter Price: "))
    cursor.execute("""
        INSERT INTO products
        (category_id, product_name, brand, price)
        VALUES (?, ?, ?, ?)
    """, (category_id, product_name, brand, price))
    connection.commit()
    connection.close()
    print("Product added successfully!")
def add_to_cart():
    connection = connect_db()
    cursor = connection.cursor()
    user_id = int(input("Enter User ID: "))
    product_id = int(input("Enter Product ID: "))
    quantity = int(input("Enter Quantity: "))
    cursor.execute("""
        INSERT INTO cart (user_id, product_id, quantity)
        VALUES (?, ?, ?)
    """, (user_id, product_id, quantity))
    connection.commit()
    connection.close()
    print("Product added to cart successfully!")   

def add_order():
    connection = connect_db()
    cursor = connection.cursor()

    user_id = int(input("Enter User ID: "))
    order_date = input("Enter Order Date (YYYY-MM-DD): ")
    total_amount = float(input("Enter Total Amount: "))

    cursor.execute("""
        INSERT INTO orders
        (user_id, order_date, total_amount)
        VALUES (?, ?, ?)
    """, (user_id, order_date, total_amount))

    connection.commit()
    connection.close()

    print("Order added successfully!")

def add_order_item():
    connection = connect_db()
    cursor = connection.cursor()

    order_id = int(input("Enter Order ID: "))
    product_id = int(input("Enter Product ID: "))
    quantity = int(input("Enter Quantity: "))

    cursor.execute("""
        INSERT INTO order_items
        (order_id, product_id, quantity)
        VALUES (?, ?, ?)
    """, (order_id, product_id, quantity))

    connection.commit()
    connection.close()

    print("Order item added successfully!")
def add_return():
    connection = connect_db()
    cursor = connection.cursor()

    order_id = int(input("Enter Order ID: "))
    product_id = int(input("Enter Product ID: "))
    user_id = int(input("Enter User ID: "))
    return_reason = input("Enter Return Reason: ")

    cursor.execute("""
        INSERT INTO returns
        (order_id, product_id, user_id, return_reason)
        VALUES (?, ?, ?, ?)
    """, (order_id, product_id, user_id, return_reason))

    connection.commit()
    connection.close()

    print("Return request added successfully!")   

def checkout():
    connection = connect_db()
    cursor = connection.cursor()

    user_id = int(input("Enter User ID: "))
    total_amount = float(input("Enter Total Amount: "))

    cursor.execute("""
        INSERT INTO orders (user_id, order_date, total_amount)
        VALUES (?, DATE('now'), ?)
    """, (user_id, total_amount))

    connection.commit()
    connection.close()

    print("Order placed successfully!")         


def view_users():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()

    for user in users:
        print(user)

    connection.close()

def view_categories():
    connection = connect_db()
    cursor = connection.cursor()
  
    cursor.execute("SELECT * FROM categories")

    categories = cursor.fetchall()

    for category in categories:
        print(category)

    connection.close()

def view_products():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    for product in products:
        print(product)

    connection.close()   

def view_cart():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM cart")

    cart_items = cursor.fetchall()

    for item in cart_items:
        print(item)

    connection.close()

def view_orders():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM orders")

    orders = cursor.fetchall()

    for order in orders:
        print(order)

    connection.close()

def view_order_items():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM order_items")

    items = cursor.fetchall()

    for item in items:
        print(item)

    connection.close()

def view_returns():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM returns")

    returns = cursor.fetchall()

    for return_item in returns:
        print(return_item)

    connection.close()                 



def print_menu():
    print("\n=== Ecommerce Management ===")
    print("1. Add User")
    print("2. View Users")
    print("3. Add Category")
    print("4. View Categories")
    print("5. Add Product")
    print("6. View Product")
    print("7. Add Cart")
    print("8. View Cart")
    print("9. Add order")
    print("10. View order")  
    print("11. Add order items")
    print("12. View order items") 
    print("13. Add return")
    print("14. View return") 
    print("15. checkouts") 
    print("16. Exit")
     

def main():
    try:
        init_db()
    except:
        print("already exists")
    
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_user()
        elif choice == "2":
            view_users()
        elif choice == "3":
            add_category()
        elif choice == "4":
            view_categories()
        elif choice == "5":
            add_product()
        elif choice == "6":
            view_products()
        elif choice == "7":
            add_cart()
        elif choice == "8":
            view_cart()    
        elif choice == "9":
            add_order()
        elif choice == "10":
            view_orders()
        elif choice == "11":
            add_order_item()
        elif choice == "12":
            view_order_items()
        elif choice == "13":
            add_return()
        elif choice == "14":
            view_returns()        

        elif choice == "15":
            print("Thank You!")
            break
        else:
            print("Invalid Choice!")
    
if __name__ == "__main__":
    main()
    
   

# connection.close()