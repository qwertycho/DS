def read_alias(path):
    dict = {}
    data = None
    with open(path, 'r') as file:
        data = json.load(file)
        for product in data:
            for alias in data[product]:
                dict[alias] = product
    return dict

def get_cleaned_name(name, dict):
    if name in dict:
        return dict[name].upper()
    else:
        return name.upper()
    
    
def create_db(name : str, cursor):
    CREATE_ORDER_TABLE = """
    CREATE TABLE "OrderLines" (
	"OrderlineID"	INTEGER,
	"OrderID"	INTEGER,
	"CustomerID"	NUMERIC,
	"Date"	TEXT,
	"Product"	TEXT,
    "ProductName"	TEXT,
	"Amount"	REAL
    );
    """
    
    CREATE_PRODUCT_TABLE = """
    CREATE TABLE "ProductInfo" (
    	"ProductID"	INTEGER,
    	"ProductName"	TEXT,
    	"ProductType"	TEXT,
    	"CostPrice"	REAL,
    	"SalesPrice"	REAL
    );
    """
    cursor.execute(CREATE_ORDER_TABLE)
    cursor.execute(CREATE_PRODUCT_TABLE)
    print("db created")

def insert_products_db(dataframe, cursor):
    INSERT_PRODUCT_SQL = "INSERT INTO ProductInfo (ProductID,ProductName,ProductType, CostPrice, SalesPrice) VALUES (?,?,?,?,?)"
    for p in dataframe:
        cursor.execute(INSERT_PRODUCT_SQL, (p["ProductID"],p["ProductName"],p["ProductType"],p["CostPrice"],p["SalesPrice"]))
    
    
def insert_orders_db(dataframe, names : dict, cursor):
    INSERT_ORDER_LINE = """ INSERT INTO OrderLines (OrderlineID, OrderID, CustomerID, Date, Product, ProductName, Amount) VALUES (?,?,?,?,?,?,?)"""
    for line in dataframe:
        ProductName = get_cleaned_name(line["Product"], names)
        cursor.execute(INSERT_ORDER_LINE, (line["OrderlineID"], line["OrderID"], line["CustomerID"], line["Date"], line["Product"], ProductName, line["Amount"]))

def update_price_db(id : int, price: float, cursor):
    sql = "UPDATE ProductInfo set SalesPrice = ? WHERE ProductID = ?"
    cursor.execute(sql, (price, id))
    
import sqlite3
import json
import pandas as pd
import os

orderlines = pd.read_csv("OrderLines.csv").to_dict(orient='records')
names = read_alias("know_alias.json")


conn = None
cursor = None

if os.path.isfile("test.db"):
    print("db bestaat al!")
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
else:
    #maak een nieuwe database aan met de tabellen
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    create_db("test.db", cursor)
    #sla op
    conn.commit()
    print("db created")

#de orderlines inserten
#deze functie normaliseerd de ProductNames
insert_orders_db(orderlines, names, cursor)
#opslaan
conn.commit()

products = pd.read_csv("ProductInfo.csv", delimiter=";").to_dict(orient='records')
insert_products_db(products, cursor)
conn.commit()


#db connectie sluiten
conn.close()