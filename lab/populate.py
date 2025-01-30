import pyodbc
from faker import Faker
import random

# Database connection
conn = pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=DESKTOP-508CDR9\\HAMNA;"  # Replace with your actual server name
        "Database=northwind_py;"           # Replace with your database name
        "Trusted_Connection=yes;"
    )

cursor = conn.cursor()

# Initialize Faker
fake = Faker()

# # Function to populate Employees
# def populate_employees(n):
#     for _ in range(n):
#         employee_id = random.randint(1, 1000)  # Generate random employee_id
#         last_name = fake.last_name()
#         first_name = fake.first_name()
#         title = fake.job_title()
#         title_of_courtesy = random.choice(['Mr.', 'Ms.', 'Mrs.', 'Dr.'])
#         birth_date = fake.date_of_birth(minimum_age=22, maximum_age=65)
#         hire_date = fake.date_between(start_date='-10y', end_date='today')
#         address = fake.street_address()
#         city = fake.city()
#         region = fake.state()
#         postal_code = fake.postcode()
#         country = fake.country()
#         home_phone = fake.phone_number()
#         extension = fake.random_number(digits=4, fix_len=True)
#         notes = fake.paragraph(nb_sentences=3)
#         photo_path = fake.image_url(width=100, height=100)
#         reports_to = random.choice([None, employee_id - 1])  # Randomly assign a supervisor
        
#         cursor.execute(
#             """
#             INSERT INTO Employees (EmployeeID, LastName, FirstName, Title, TitleOfCourtesy, BirthDate, HireDate,
#                                    Address, City, Region, PostalCode, Country, HomePhone, Extension, Notes, ReportsTo, PhotoPath)
#             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#             """,
#             employee_id, last_name, first_name, title, title_of_courtesy, birth_date, hire_date,
#             address, city, region, postal_code, country, home_phone, extension, notes, reports_to, photo_path
#         )
# Function to populate Employees
def populate_employees(n):
    job_titles = [
        'Sales Representative', 'Manager', 'Engineer', 'Accountant', 
        'Marketing Specialist', 'Human Resources Coordinator', 'Assistant'
    ]
    
    for _ in range(n):
        employee_id = random.randint(1, 1000)  # Generate random employee_id
        last_name = fake.last_name()
        first_name = fake.first_name()
        title = random.choice(job_titles)  # Choose a random job title from the list
        title_of_courtesy = random.choice(['Mr.', 'Ms.', 'Mrs.', 'Dr.'])
        birth_date = fake.date_of_birth(minimum_age=22, maximum_age=65)
        hire_date = fake.date_between(start_date='-10y', end_date='today')
        address = fake.street_address()
        city = fake.city()
        region = fake.state()
        postal_code = fake.postcode()
        country = fake.country()
        home_phone = fake.phone_number()
        extension = fake.random_number(digits=4, fix_len=True)
        notes = fake.paragraph(nb_sentences=3)
        photo_path = fake.image_url(width=100, height=100)
        reports_to = random.choice([None, employee_id - 1])  # Randomly assign a supervisor
        
        cursor.execute(
            """
            INSERT INTO Employees (EmployeeID, LastName, FirstName, Title, TitleOfCourtesy, BirthDate, HireDate,
                                   Address, City, Region, PostalCode, Country, HomePhone, Extension, Notes, ReportsTo, PhotoPath)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            employee_id, last_name, first_name, title, title_of_courtesy, birth_date, hire_date,
            address, city, region, postal_code, country, home_phone, extension, notes, reports_to, photo_path
        )


# Function to populate EmployeeTerritories
def populate_employee_territories(n):
    cursor.execute("SELECT EmployeeID FROM Employees")
    employee_ids = [row[0] for row in cursor.fetchall()]
    
    cursor.execute("SELECT TerritoryID FROM Territories")
    territory_ids = [row[0] for row in cursor.fetchall()]

    for _ in range(n):
        employee_id = random.choice(employee_ids)
        territory_id = random.choice(territory_ids)
        cursor.execute(
            "INSERT INTO EmployeeTerritories (EmployeeID, TerritoryID) VALUES (?, ?)",
            employee_id, territory_id
        )
def populate_regions(n):
    for _ in range(n):
        region_id = random.randint(1, 1000)  # Generate random region_id
        region_desc = fake.city_suffix()     # Fake city suffix for region description
        cursor.execute(
            "INSERT INTO Regions (RegionID, RegionDescription) VALUES (?, ?)",
            region_id, region_desc
        )
# Function to populate Territories
def populate_territories(n):
    cursor.execute("SELECT RegionID FROM Regions")  # Get available RegionIDs
    region_ids = [row[0] for row in cursor.fetchall()]

    for _ in range(n):
        territory_id = fake.unique.zipcode()          # Fake and unique territory id
        territory_desc = fake.city()                 # Fake city name for description
        region_id = random.choice(region_ids)        # Randomly pick a RegionID
        cursor.execute(
            "INSERT INTO Territories (TerritoryID, TerritoryDescription, RegionID) VALUES (?, ?, ?)",
            territory_id, territory_desc, region_id
        )

# Populate the tables
populate_regions(10)          # Populate 10 regions
populate_territories(20)      # Populate 20 territories
populate_employees(15)        # Populate 15 employees
populate_employee_territories(25)  # Populate 25 employee-territory assignments

# Commit the transactions
conn.commit()

# Close the connection
conn.close()

print("Data inserted successfully!")
