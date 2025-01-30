import time
import matplotlib.pyplot as plt
import pyodbc


conn = pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=DESKTOP-508CDR9\\HAMNA;"  
        "Database=northwind_py;"           
        "Trusted_Connection=yes;"
    )
cursor = conn.cursor()

# Define your queries in a dictionary
queries = {
    'PK_Orders_OrderID': "SELECT * FROM Orders WHERE OrderID = <your_order_id>",
    'PK_Customers_CustomerID': "SELECT * FROM Customers WHERE CustomerID = <your_customer_id>",
    'PK_Suppliers_SupplierID': "SELECT * FROM Suppliers WHERE SupplierID = <your_supplier_id>",
    'PK_Products_ProductID': "SELECT * FROM Products WHERE ProductID = <your_product_id>",
    'PK_Employees_EmployeeID': "SELECT * FROM Employees WHERE EmployeeID = <your_employee_id>",
    'NonPK_Customers_CustomerName': "SELECT * FROM Customers WHERE CName = '<customer_name>'",
    'NonPK_Shippers_CompanyName': "SELECT * FROM Shippers WHERE CompanyName = '<company_name>'",
    'NonPK_Orders_OrderDate': "SELECT * FROM Orders WHERE OrderDate = '<order_date>'",
    'NonPK_Orders_ByCustomerName': "SELECT * FROM Orders o JOIN Customers c ON o.CustomerID = c.CustomerID WHERE c.CName = '<customer_name>'",
    'NonPK_Orders_ByShipperName': "SELECT * FROM Orders o JOIN Shippers s ON o.ShipperID = s.ShipperID WHERE s.CompanyName = '<company_name>'"
}

# Dictionary to store execution times
execution_times = {}

# Assuming cursor is your database connection cursor object
for query_name, query in queries.items():
    start_time = time.time()
    cursor.execute(query)
    cursor.fetchall()  # Fetch results to ensure full execution
    end_time = time.time()
    
    # Calculate the execution time
    execution_time = end_time - start_time
    execution_times[query_name] = execution_time
    
    # Print the execution time for each query
    print(f"Execution time for {query_name}: {execution_time:.6f} seconds")

# Plotting the results
plt.bar(execution_times.keys(), [time * 100 for time in execution_times.values()])  # Scale time if differences are small
plt.xlabel('Queries')
plt.ylabel('Execution Time (scaled)')
plt.title('Query Execution Times')
plt.xticks(rotation=90)
plt.show()
