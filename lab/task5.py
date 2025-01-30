import pyodbc
import time
import matplotlib.pyplot as plt

conn = pyodbc.connect (
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=DESKTOP-508CDR9\\HAMNA;"  
        "Database=northwind_py;"           
        "Trusted_Connection=yes;"
    )
cursor = conn.cursor()
pk_queries = {
    "Get Order Details": "SELECT * FROM Orders WHERE OrderID = 10248",
    "Get Customer Info": "SELECT * FROM Customers WHERE CustomerID = 1",
    "Get Supplier Details": "SELECT * FROM Suppliers WHERE SupplierID = 1",
    "Get Product Details": "SELECT * FROM Products WHERE ProductID = 1",
    "Get Employee Details": "SELECT * FROM Employees WHERE EmployeeID = 1"
}

non_pk_queries = {
    "Get Customer Details by Name": "SELECT * FROM Customers WHERE CName = 'Alfreds Futterkiste'",
    "Get Shipper Details": "SELECT * FROM Shippers WHERE CompanyName = 'Speedy Express'",
    "Get Orders by Order Date": "SELECT * FROM Orders WHERE OrderDate = '2022-07-04'",
    "Get Orders by Customer Name": "SELECT * FROM Orders WHERE CustomerID IN (SELECT CustomerID FROM Customers WHERE CName = 'Alfreds Futterkiste')",
    "Get Orders by Shipper Name": "SELECT * FROM Orders WHERE ShipperID IN (SELECT ShipperID FROM Shippers WHERE CompanyName = 'Speedy Express')"
}

pk_execution_times = {}
for query_name, query in pk_queries.items():
    start_time = time.time()
    cursor.execute(query)
    cursor.fetchall() 
    end_time = time.time()
    pk_execution_times[query_name] = (end_time - start_time) * 1000 

non_pk_execution_times = {}
for query_name, query in non_pk_queries.items():
    start_time = time.time()
    cursor.execute(query)
    cursor.fetchall()  
    end_time = time.time()
    non_pk_execution_times[query_name] = (end_time - start_time) * 1000  # Convert to milliseconds

cursor.close()
conn.close()

all_execution_times = {**pk_execution_times, **non_pk_execution_times}

plt.bar(all_execution_times.keys(), all_execution_times.values())
plt.xticks(rotation=45, ha='right')
plt.xlabel('Queries')
plt.ylabel('Execution Time (milliseconds)')
plt.title('Query Execution Times')
plt.tight_layout()
plt.show()
