import psycopg2
import csv
def connect():
    return psycopg2.connect(
        host="localhost", 
        dbname="postgres", 
        user="postgres",
        password="KamaMur_205" 
    )
def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            phone VARCHAR(20)
        )
    """)
    conn.commit()
    cur.close()
    conn.close()
def insert_manual():
    conn = connect()
    cur = conn.cursor()
    name = input("Input your name: ")
    phone = input("Input your phone number: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Information added manually.")
def insert_from_csv():
    conn = connect()
    cur = conn.cursor()
    file_path = input("Input your CSV file name (example: contacts.csv): ")
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 2:
                name, phone = row
                cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Information added from CSV file.")
def update_data():
    conn = connect()
    cur = conn.cursor()
    name = input("Enter the name whose phone number you want to update: ")
    new_phone = input("Enter new phone number: ")
    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
    conn.commit()
    cur.close()
    conn.close()
    print("Phone number updated.")
def query_data():
    conn = connect()
    cur = conn.cursor()
    name_filter = input("Input the name to search: ")
    cur.execute("SELECT * FROM phonebook WHERE name = %s", (name_filter,))
    rows = cur.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
    if not rows:
        print("Nothing found.")
    cur.close()
    conn.close()
def delete_data():
    conn = connect()
    cur = conn.cursor()
    name = input("Enter the name to delete: ")
    cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    conn.commit()
    cur.close()
    conn.close()
    print("Information deleted.")
def search_by_pattern():
    conn = connect()
    cur = conn.cursor()
    pattern = input("Enter pattern to search (part of name or phone): ")
    like_pattern = f"%{pattern}%"
    cur.execute("""
        SELECT * FROM phonebook
        WHERE name ILIKE %s OR phone ILIKE %s
    """, (like_pattern, like_pattern))
    rows = cur.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
    if not rows:
        print("No matching records found.")
    cur.close()
    conn.close()
def insert_or_update_user():
    conn = connect()
    cur = conn.cursor()
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
    result = cur.fetchone()
    if result:
        cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (phone, name))
        print("User exists. Phone updated.")
    else:
        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
        print("New user added.")
    conn.commit()
    cur.close()
    conn.close()
def insert_many_users():
    conn = connect()
    cur = conn.cursor()
    users = []
    n = int(input("How many users do you want to add? "))
    for _ in range(n):
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        users.append((name, phone))

    incorrect_data = []
    for name, phone in users:
        if not phone.isdigit():
            incorrect_data.append((name, phone))
            continue
        cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    if incorrect_data:
        print("Incorrect data found:")
        for name, phone in incorrect_data:
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("All users inserted successfully.")
def query_with_pagination():
    conn = connect()
    cur = conn.cursor()
    limit = int(input("Enter limit (how many records to show): "))
    offset = int(input("Enter offset (how many records to skip): "))
    cur.execute("""
        SELECT * FROM phonebook
        ORDER BY id
        LIMIT %s OFFSET %s
    """, (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
    if not rows:
        print("No records found.")
    cur.close()
    conn.close()
def delete_by_name_or_phone():
    conn = connect()
    cur = conn.cursor()
    keyword = input("Enter name or phone to delete: ")
    cur.execute("""
        DELETE FROM phonebook
        WHERE name = %s OR phone = %s
    """, (keyword, keyword))
    conn.commit()
    cur.close()
    conn.close()
    print("Deleted if existed.")
def menu():
    create_table()
    while True:
        print("\n PHONEBOOK:")
        print("1. Add information manually")
        print("2. Add information from CSV")
        print("3. Update information")
        print("4. Search information")
        print("5. Delete information")
        print("6. Search by pattern")
        print("7. Insert or update user")
        print("8. Insert many users with validation")
        print("9. Query with pagination")
        print("10. Delete by name or phone")
        print("11. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            insert_manual()
        elif choice == "2":
            insert_from_csv()
        elif choice == "3":
            update_data()
        elif choice == "4":
            query_data()
        elif choice == "5":
            delete_data()
        elif choice == "6":
            search_by_pattern()
        elif choice == "7":
            insert_or_update_user()
        elif choice == "8":
            insert_many_users()
        elif choice == "9":
            query_with_pagination()
        elif choice == "10":
            delete_by_name_or_phone()
        elif choice == "11":
            print("The code is over.")
            break
        else:
            print("ERROR. Please, try again.")
if __name__ == "__main__":
    menu()