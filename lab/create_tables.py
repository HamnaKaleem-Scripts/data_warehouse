import pyodbc

try:
    conn = pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=DESKTOP-508CDR9\\HAMNA;"  
        "Database=northwind_py;"           
        "Trusted_Connection=yes;"
    )
    cursor = conn.cursor()
    print("Connection successful!")

    sql_commands = [
        """
        CREATE TABLE Shippers (
            ShipperID INT PRIMARY KEY,
            CompanyName NVARCHAR(100),
            Phone NVARCHAR(50)
    );

        """,
        """
        CREATE TABLE Customers (
            CustomerID INT PRIMARY KEY,
            CName VARCHAR(255),
            ContactName VARCHAR(30),
            Address VARCHAR(255),
            City VARCHAR(50),
            PostalCode VARCHAR(20),
            Country VARCHAR(50),
            
        );
        """,
        """
        
        """,
        """
        CREATE TABLE Suppliers (
            SupplierID INT PRIMARY KEY,
            SupplierName NVARCHAR(100),
            ContactName NVARCHAR(100),
            Address NVARCHAR(255),
            City NVARCHAR(100),
            PostalCode NVARCHAR(20),
            Country NVARCHAR(50),
            Phone NVARCHAR(50)
        );

        """,
                """
        CREATE TABLE Categories (
            CategoryID INT PRIMARY KEY,
            CategoryName VARCHAR(255),
            Description TEXT,
            Picture IMAGE
        );
    """,
        """
        CREATE TABLE Products (
            ProductID INT PRIMARY KEY,
            ProductName NVARCHAR(100),
            SupplierID INT,
            CategoryID INT,
            Unit NVARCHAR(100),
            Price FLOAT,
            FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID),
            FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
            
        );
        """,
        """
        CREATE TABLE Employees (
            EmployeeID INT PRIMARY KEY,
            LastName VARCHAR(255),
            FirstName VARCHAR(255),
            Title VARCHAR(50),
            TitleOfCourtesy VARCHAR(25),
            BirthDate DATE,
            HireDate DATE,
            Address VARCHAR(255),
            City VARCHAR(50),
            Region VARCHAR(50),
            PostalCode VARCHAR(20),
            Country VARCHAR(50),
            HomePhone VARCHAR(24),
            Extension VARCHAR(4),
            Photo IMAGE,
            Notes TEXT,
            ReportsTo INT,
            PhotoPath VARCHAR(255),
            FOREIGN KEY (ReportsTo) REFERENCES Employees(EmployeeID)
        );
        """,
       """
        CREATE TABLE Orders (
            OrderID INT PRIMARY KEY,
            CustomerID INT,
            EmployeeID INT,
            OrderDate DATE,
            ShipperID INT,
            FOREIGN KEY (ShipperID ) REFERENCES Shippers(ShipperID),
            FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
            FOREIGN KEY (EmployeeID ) REFERENCES Employees(EmployeeID )
            
            
            
        );
    """,
        """
        CREATE TABLE Order_details (
            OrderDetailID INT PRIMARY KEY,
            OrderID INT,
            ProductID INT,
            Quantity INT,
            FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
            FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
        );
        """,
        
        """
        CREATE TABLE Regions (
            RegionID INT PRIMARY KEY,
            RegionDescription VARCHAR(50)
        );
        """,
        """
        CREATE TABLE Territories (
            TerritoryID VARCHAR(20) PRIMARY KEY,
            TerritoryDescription VARCHAR(50),
            RegionID INT,
            FOREIGN KEY (RegionID) REFERENCES Regions(RegionID)
        );
        """,
        """
        CREATE TABLE EmployeeTerritories (
            EmployeeID INT,
            TerritoryID VARCHAR(20),
            PRIMARY KEY (EmployeeID, TerritoryID),
            FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
            FOREIGN KEY (TerritoryID) REFERENCES Territories(TerritoryID)
        );
        """

        
    ]

    for command in sql_commands:
        cursor.execute(command)
        print("Table created successfully.")

    conn.commit()

except Exception as e:
    print(f"Error: {e}")
finally:

    if 'conn' in locals():
        conn.close()
        print("Connection closed.")
