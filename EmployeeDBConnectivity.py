import mysql.connector

class Employee:

    def __init__(self):

        # Creating Connectivity
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="employeedb",
            port="3306"
        )

        self.cur = self.conn.cursor()

        print("Connectivity done successfully!!")

    # Fetch Data
    def fetch_data(self):

        query = "SELECT * FROM employeeTable"

        self.cur.execute(query)

        for row in self.cur.fetchall():
            print(row)

        print("Data has fetched Successfully!!")

    # Insert Data
    def insert_data(self):

        sql = "INSERT INTO employeeTable VALUES (%s,%s,%s)"

        values = [
            (1, "Krisha", "HR"),
            (2, "Nidhi", "Sales"),
            (3, "Prachi", "CA")
        ]

        self.cur.executemany(sql, values)
        
        self.conn.commit()

        print("Data inserted Successfully!!")

    # Delete Data
    def delete_data(self):

        sql = "DELETE FROM employeeTable WHERE emp_id = %s"

        value = (1,)

        self.cur.execute(sql, value)

        self.conn.commit()

        print("Data deleted successfully!!")

    # Close Connectivity
    def close_connection(self):

        self.conn.close()

        print("Connection is closed!!")


# Object Creation
e1 = Employee()

print("\nOptions\n1.Fetch data.\n2.Insert data.\n3.Delete data.\n4.Exit.")

option = input("Enter option 1/2/3/4 : ")

if(option == "1"):
    e1.fetch_data()

elif(option == "2"):
    e1.insert_data()

elif(option == "3"):
    e1.delete_data()

elif(option == "4"):
    print("Exit")

else:
    print("Invalid option!!")

# Close Connection
e1.close_connectivity()