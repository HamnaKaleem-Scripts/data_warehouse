
import pandas as pd
import pyodbc
from faker import Faker
import random
import os
import traceback


fake = Faker()


try:
    conn = pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=DESKTOP-508CDR9\\HAMNA;"  
        "Database=northwind_py;"          
        "Trusted_Connection=yes;"
    )
    cursor = conn.cursor()
    print("Connection successful!")
    def populate_regions(n):
        for _ in range(n):
            region_id = random.randint(1, 1000)  
            region_desc = fake.city_suffix()    
            try:
                cursor.execute(
                    "INSERT INTO Regions (RegionID, RegionDescription) VALUES (?, ?)",
                    region_id, region_desc
                )
                print(f"Inserted Region {region_id}.")
            except Exception as e:
                print(f"Error inserting Region {region_id}: {e}")
                traceback.print_exc()

    #  Faker
    def populate_territories(n):
        cursor.execute("SELECT RegionID FROM Regions")
        region_ids = [row[0] for row in cursor.fetchall()]
        if not region_ids:
            print("No regions available to assign territories.")
            return

        for _ in range(n):
            territory_id = fake.unique.zipcode()  # Ensure uniqueness
            territory_desc = fake.city()
            region_id = random.choice(region_ids)
            try:
                cursor.execute(
                    "INSERT INTO Territories (TerritoryID, TerritoryDescription, RegionID) VALUES (?, ?, ?)",
                    territory_id, territory_desc, region_id
                )
                print(f"Inserted Territory {territory_id}.")
            except Exception as e:
                print(f"Error inserting Territory {territory_id}: {e}")
                traceback.print_exc()


    def populate_shippers_from_csv(file_path):
        try:
            df = pd.read_csv(file_path,header=0)
            df.columns = df.columns.str.strip()
            df.columns = df.columns.str.strip()

            print(f"Successfully read {file_path}.")
            for index, row in df.iterrows():
                try:
                    shipper_id = int(row['ShipperID'])
                    company_name = row['CompanyName']
                    phone = row['Phone']
                    cursor.execute(
                        "INSERT INTO Shippers (ShipperID, CompanyName, Phone) VALUES (?, ?, ?)",
                        shipper_id, company_name, phone
                    )
                    print(f"Inserted Shipper {shipper_id} at row {index + 1}.")
                except Exception as e:
                    print(f"Error inserting Shipper {row['ShipperID']} at row {index + 1}: {e}")
                    traceback.print_exc()
            print(f"Successfully inserted Shippers from {file_path}.")
        except Exception as e:
            print(f"Error reading Shippers.csv: {e}")
            traceback.print_exc()

    def populate_suppliers_from_csv(file_path):
        try:
            df = pd.read_csv(file_path,header=0)
            df.columns = df.columns.str.strip()
            df.columns = df.columns.str.strip()
            print(f"Successfully read {file_path}.")
            for index, row in df.iterrows():
                try:
                    supplier_id = int(row['SupplierID'])
                    supplier_name = row['SupplierName']
                    contact_name = row['ContactName']
                    address = row['Address']
                    city = row['City']
                    postal_code = row['PostalCode']
                    country = row['Country']
                    phone = row['Phone']
                    cursor.execute(
                        """
                        INSERT INTO Suppliers (SupplierID, SupplierName, ContactName, Address, City, PostalCode, Country, Phone)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        supplier_id, supplier_name, contact_name, address, city, postal_code, country, phone
                    )
                    print(f"Inserted Supplier {supplier_id} at row {index + 1}.")
                except Exception as e:
                    print(f"Error inserting Supplier {row['SupplierID']} at row {index + 1}: {e}")
                    traceback.print_exc()
            print(f"Successfully inserted Suppliers from {file_path}.")
        except Exception as e:
            print(f"Error reading Suppliers.csv: {e}")
            traceback.print_exc()

    def populate_categories_from_csv(file_path):
        try:
            df = pd.read_csv(file_path,header=0)
            df.columns = df.columns.str.strip()
            df.columns = df.columns.str.strip()

            print(f"Successfully read {file_path}.")
            for index, row in df.iterrows():
                try:
                    category_id = int(row['CategoryID'])
                    category_name = row['CategoryName']
                    description = row['Description']
                    picture = None  # Handling IMAGE field requires binary data
                    cursor.execute(
                        """
                        INSERT INTO Categories (CategoryID, CategoryName, Description, Picture)
                        VALUES (?, ?, ?, ?)
                        """,
                        category_id, category_name, description, picture
                    )
                    print(f"Inserted Category {category_id} at row {index + 1}.")
                except Exception as e:
                    print(f"Error inserting Category {str(row['CategoryID'])} at row {index + 1}: {e}")
                    traceback.print_exc()
            print(f"Successfully inserted Categories from {file_path}.")
        except Exception as e:
            print(f"Error reading Categories.csv: {e}")
            traceback.print_exc()

    def populate_customers_from_csv(file_path):
        try:
            df = pd.read_csv(file_path,header=0)
            df.columns = df.columns.str.strip()
            df.columns = df.columns.str.strip()
            print(f"Successfully read {file_path}.")
            for index, row in df.iterrows():
                try:
                    customer_id = int(row['CustomerID']) 
                    company_name = row['CustomerName']  
                    contact_name = row['ContactName']
                    address = row['Address']
                    city = row['City']
                    postal_code = row['PostalCode']
                    country = row['Country']
                    cursor.execute(
                        """
                        INSERT INTO Customers (CustomerID, CompanyName, ContactName, Address, City, PostalCode, Country)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                        """,
                        customer_id, company_name, contact_name, address, city, postal_code, country
                    )
                    print(f"Inserted Customer {customer_id} at row {index + 1}.")
                except Exception as e:
                    print(f"Error inserting Customer {row['CustomerID']} at row {index + 1}: {e}")
                    traceback.print_exc()
            print(f"Successfully inserted Customers from {file_path}.")
        except Exception as e:
            print(f"Error reading Customers.csv: {e}")
            traceback.print_exc()

    def populate_products_from_csv(file_path):
        try:
            df = pd.read_csv(file_path,header=0)
            df.columns = df.columns.str.strip()
            df.columns = df.columns.str.strip()
            print(f"Successfully read {file_path}.")
            for index, row in df.iterrows():
                try:
                    product_id = int(row['ProductID'])
                    product_name = row['ProductName']
                    supplier_id = int(row['SupplierID'])
                    category_id = int(row['CategoryID'])
                    unit = row['Unit']
                    price = float(row['Price'])
                    cursor.execute(
                        """
                        INSERT INTO Products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price)
                        VALUES (?, ?, ?, ?, ?, ?)
                        """,
                        product_id, product_name, supplier_id, category_id, unit, price
                    )
                    print(f"Inserted Product {product_id} at row {index + 1}.")
                except Exception as e:
                    print(f"Error inserting Product {row['ProductID']} at row {index + 1}: {e}")
                    traceback.print_exc()
            print(f"Successfully inserted Products from {file_path}.")
        except Exception as e:
            print(f"Error reading Products.csv: {e}")
            traceback.print_exc()

    def populate_employees(n):
        job_titles = [
            'Sales Representative', 'Manager', 'Engineer', 'Accountant', 
            'Marketing Specialist', 'Human Resources Coordinator', 'Assistant'
        ]
        
        employee_ids = []
        for _ in range(n):
            employee_id = random.randint(1, 10000)
            last_name = fake.last_name()
            first_name = fake.first_name()
            title = random.choice(job_titles)
            title_of_courtesy = random.choice(['Mr.', 'Ms.', 'Mrs.', 'Dr.'])
            birth_date = fake.date_of_birth(minimum_age=22, maximum_age=65)
            hire_date = fake.date_between(start_date='-10y', end_date='today')
            address = fake.street_address()
            city = fake.city()
            region = fake.state()
            postal_code = fake.postcode()
            country = fake.country()
            home_phone = fake.phone_number()
            extension = str(fake.random_number(digits=4, fix_len=True))
            notes = fake.paragraph(nb_sentences=3)
            photo_path = fake.image_url(width=100, height=100)
            reports_to = None  
            try:
                cursor.execute(
                    """
                    INSERT INTO Employees (
                        EmployeeID, LastName, FirstName, Title, TitleOfCourtesy, BirthDate, HireDate,
                        Address, City, Region, PostalCode, Country, HomePhone, Extension, Notes, ReportsTo, PhotoPath
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    employee_id, last_name, first_name, title, title_of_courtesy, birth_date, hire_date,
                    address, city, region, postal_code, country, home_phone, extension, notes, reports_to, photo_path
                )
                employee_ids.append(employee_id)
                print(f"Inserted Employee {employee_id}.")
            except Exception as e:
                print(f"Error inserting Employee {employee_id}: {e}")
                traceback.print_exc()

        for emp_id in employee_ids:
            if len(employee_ids) > 1:
              
                possible_supervisors = [id for id in employee_ids if id != emp_id]
                if possible_supervisors:
                    supervisor = random.choice(possible_supervisors)
                    try:
                        cursor.execute(
                            "UPDATE Employees SET ReportsTo = ? WHERE EmployeeID = ?",
                            supervisor, emp_id
                        )
                        print(f"Assigned ReportsTo for Employee {emp_id} to Supervisor {supervisor}.")
                    except Exception as e:
                        print(f"Error updating ReportsTo for Employee {emp_id}: {e}")
                        traceback.print_exc()

    def populate_orders_from_csv(file_path):
        try:
            df = pd.read_csv(file_path,header=0)
            df.columns = df.columns.str.strip()
            df.columns = df.columns.str.strip()
            print(f"Successfully read {file_path}.")
            for index, row in df.iterrows():
                try:
                    order_id = int(row['OrderID'])
                    customer_id = int(row['CustomerID']) 
                    employee_id = int(row['EmployeeID']) 
                    order_date = row['OrderDate'] 
                    shipper_id = int(row['ShipperID']) 
                    cursor.execute(
                        """
                        INSERT INTO Orders (OrderID, CustomerID, EmployeeID, OrderDate, ShipperID)
                        VALUES (?, ?, ?, ?, ?)
                        """,
                        order_id, customer_id, employee_id, order_date, shipper_id
                    )
                    print(f"Inserted Order {order_id} at row {index + 1}.")
                except Exception as e:
                    print(f"Error inserting Order {row['OrderID']} at row {index + 1}: {e}")
                    traceback.print_exc()
            print(f"Successfully inserted Orders from {file_path}.")
        except Exception as e:
            print(f"Error reading Orders.csv: {e}")
            traceback.print_exc()

    def populate_order_details_from_csv(file_path):
        try:
            df = pd.read_csv(file_path,header=0)
            df.columns = df.columns.str.strip()
            print(f"Successfully read {file_path}.")

            df.columns = df.columns.str.strip()
            for index, row in df.iterrows():
                try:
                    
                    order_detail_id = int(row['OrderDetailID'])
                    order_id = int(row['OrderID']) 
                    product_id = int(row['ProductID'])

                    quantity = int(row['Quantity'])
                    cursor.execute(
                        """
                        INSERT INTO Order_details (OrderDetailID, OrderID, ProductID, Quantity)
                        VALUES (?, ?, ?, ?)
                        """,
                        order_detail_id, order_id, product_id, quantity
                    )
                    print(f"Inserted OrderDetail {order_detail_id} at row {index + 1}.")
                except Exception as e:
                    print(f"Error inserting OrderDetail {row['OrderDetailID']} at row {index + 1}: {e}")
                    traceback.print_exc()
            print(f"Successfully inserted Order_details from {file_path}.")
        except Exception as e:
            print(f"Error reading Order_details.csv: {e}")
            traceback.print_exc()

    def populate_employee_territories(n):
        cursor.execute("SELECT EmployeeID FROM Employees")
        employee_ids = [row[0] for row in cursor.fetchall()]
        cursor.execute("SELECT TerritoryID FROM Territories")
        territory_ids = [row[0] for row in cursor.fetchall()]
        if not employee_ids or not territory_ids:
            print("Employees or Territories not populated yet.")
            return

        for _ in range(n):
            employee_id = random.choice(employee_ids)
            territory_id = random.choice(territory_ids)
            try:
                cursor.execute(
                    "INSERT INTO EmployeeTerritories (EmployeeID, TerritoryID) VALUES (?, ?)",
                    employee_id, territory_id
                )
                print(f"Inserted EmployeeTerritory (EmployeeID: {employee_id}, TerritoryID: {territory_id}).")
            except Exception as e:
                print(f"Error inserting EmployeeTerritory (EmployeeID: {employee_id}, TerritoryID: {territory_id}): {e}")
                traceback.print_exc()

    csv_directory = r'C:\\Users\\LENOVO\\Desktop\\lab' 

    csv_files = [
        'Shippers.csv',
        'Suppliers.csv',
        'Categories.csv',
        'Customers.csv',
        'Products.csv',
        'Orders.csv',
        'Order_details.csv'
    ]

    try:
        conn.autocommit = False
        
        populate_regions(10)  
        populate_territories(20)  
        populate_shippers_from_csv(os.path.join(csv_directory, 'C:\\Users\\LENOVO\\Desktop\\lab\\Shippers.csv'))
        populate_suppliers_from_csv(os.path.join(csv_directory, 'Suppliers.csv'))  
        
        populate_customers_from_csv(os.path.join(csv_directory, 'Customers.csv'))  
        populate_categories_from_csv(os.path.join(csv_directory, 'Categories.csv')) 
        populate_products_from_csv(os.path.join(csv_directory, 'Products.csv'))  
        
        populate_employees(15)  
        populate_orders_from_csv(os.path.join(csv_directory, 'Orders.csv')) 
        populate_order_details_from_csv(os.path.join(csv_directory, 'Order_details.csv'))  
    
        populate_employee_territories(25) 
        conn.commit()
        print("Data insertion complete!")

    except Exception as e:
        conn.rollback() 
        print(f"Transaction rolled back due to error: {e}")
        traceback.print_exc()
    finally:
        conn.autocommit = True
        conn.close()
        print("Connection closed.")
finally:
    conn.commit()
    cursor.close()
    conn.close()
    print("Connection closed.")



