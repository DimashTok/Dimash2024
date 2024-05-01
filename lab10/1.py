import psycopg2
import csv
 
conn = psycopg2.connect(
    host="localhost", 
    dbname="Tests", 
    user="postgres",
    password="14040808", port=5432)

cur = conn.cursor()

cur.execute('DROP TABLE Phone_Book')

conn.commit()
 
cur.execute("""CREATE TABLE Phone_Book (
            name VARCHAR(255),
            pn VARCHAR(20)
);
""")
conn.commit()

filename = 'C:/Users/Dimash/Desktop/Dimash2024PP2/lab10/phone.csv'

with open(filename, "r") as file:
    csvreader = csv.reader(file, delimiter=',')
    for row in csvreader:
        name,pn = row
        cur.execute(f"""INSERT INTO Phone_Book(name, pn) VALUES
                    ('{name}','{pn}');
        """)        

conn.commit()

def input_data():
    name = input("Enter name: ")
    pn = input("Enter phone numer: ")
    return name, pn

def input_data_for_update_name():
    name = input("Enter name: ")
    return name

def input_data_for_update_pn():
    pn = input("Enter phone numer: ")
    return pn
    
while True:
    choice = input("Do you want to add another data? (yes/no): ")
    if choice.lower() != "yes":
        break
    else:
        name, pn = input_data()
        cur.execute(f"""INSERT INTO Phone_Book(name, pn) VALUES ('{name}','{pn}');""")
        conn.commit()
        print("Data added successfully!")

    
while True:
    choice2 = input("Do you want to change the values?  (yes/no): ")
    if choice2.lower() != "yes":
        break
    else:
        choice3 = input("What do you want to change? (name/pn/all): ")
        choice4 = input("Where do you want to update? name: ")
        if choice3.lower() == 'name':
            name2 = input_data_for_update_name()
            cur.execute(f"""UPDATE Phone_Book 
                        SET name = '{name2}' 
                        WHERE name = '{choice4}'
            """)
            conn.commit()
            print("Data changed successfully!")
        elif choice3.lower() == "pn":
            pn2 = input_data_for_update_pn()
            cur.execute(f"""UPDATE Phone_Book 
                        SET pn = '{pn2}' 
                        WHERE name = '{choice4}'
            """)
            conn.commit()
            print("Data changed successfully!")
        elif choice3.lower() == "all":
            name3, pn3 = input_data()
            cur.execute(f"""UPDATE Phone_Book 
                        SET name = '{name3}', pn = '{pn3}'
                        WHERE name = '{choice4}'
            """)
            conn.commit()
            print("Data changed successfully!")
while True:
    choice5 = input("Do you want delete something? (yes/no): ")
    if choice5.lower() != 'yes':
        break
    else:
        choice6 = input("What do you want to delete? name: ")
        cur.execute(f"""DELETE FROM Phone_Book
                    WHERE name = '{choice6}'
        """)
        conn.commit()
        print("Data deleted successfully!")

