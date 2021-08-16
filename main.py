import csv
from os import write

item_list=[
    {"name":"front wing", "quantity":5, "unit":"szt", "unit_price":100},
    {"name":"grear box", "quantity":7, "unit":"szt", "unit_price":670},
    {"name":"engine","quantity":12, "unit":"szt", "unit_price":1000}
]
sold_items=[]

def user_input():
    uinput=input("What would you like to do?")
    if uinput == "exit":
        print("Bye")
        exit(1)
    elif uinput=="show":
        print("List of products:")
        get_items()
        user_input()
    elif uinput=="add":
        add_items()
        user_input()
    elif uinput=="sell":
        sell_items()
        user_input()
    elif uinput=="profit":
        print(show_revenue())
        user_input()
    elif uinput=="save":
        export_file_location=input("Please insert location in which data should be saved:")
        export_file_name=input("Name the file:")
        print(f"Exporting data to {export_file_location}/{export_file_name}.csv")
        export_to_csv(export_file_location,export_file_name)
        user_input()
    elif uinput=="import":
        importfile=input("Which file should be imported:")
        print(f"Importing data from {importfile}")
        import_from_csv(importfile)
        user_input()
    elif uinput not in ["exit","show","add","sell","profit","save","import"]:
        print("Invalid command\nValid commands are : exit, show, add, sell, profit, save, import")
        user_input()



def get_items():
    print("Name\t   Quantity\tUnit\tUnit Price (PLN)")
    for i in item_list:
        name='{:{width}}'.format(i.get("name"), width=10)
        quantity='{:{width}}'.format(round(float(i.get("quantity")),2), width=4)
        unit='{:{width}}'.format(i.get("unit"), width=4)
        price='{:{width}}'.format(round(float(i.get("unit_price")),2), width=12)
        print(f"{name} {quantity} \t {unit} {price}")

def add_items():
    name=input("Item name:")
    quantity=input("Item quantity:")
    unit=input("Items unit of measure:")
    price=input("Unit price:")
    item_list.append({"name":name, "quantity":quantity, "unit":unit, "unit_price":price})
    print(f"Added name:{name}, quantity:{quantity}, unit:{unit}, unit_price:{price}")

def sell_items():
    name=input("What would you like to sell?")
    for i in range(len(item_list)):
        if item_list[i].get("name")==name:
            quantity=float(input("How much?"))
            item_list[i]["quantity"]-=quantity
            sold_items.append({"name":name, "quantity":quantity, "unit":item_list[i].get("unit"), "unit_price":item_list[i].get("unit_price") })
            print(f"Sold {quantity} {item_list[i].get('unit')} of {name}")
            break
        elif i ==len(item_list)-1 and item_list[i].get("name")!=name:
            print(f"{name} doesn't exist in database")
    
def get_costs():
    cost=0
    for i in item_list:
        cost+=i.get("quantity")*i.get("unit_price")
    return cost

def get_income():
    income=0
    for i in sold_items:
        income+=i.get("quantity")*i.get("unit_price")
    return income

def show_revenue():
    profit=get_income()-get_costs()
    return profit

def export_to_csv(export_path,file_name):
    with open(f"{export_path}/{file_name}.csv", "w", newline='') as csvfile:
        fieldnames=["name", "quantity", "unit", "unit_price"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in item_list:
            writer.writerow({'name':i.get("name"), "quantity":i.get("quantity"), "unit":i.get("unit"), "unit_price":i.get("unit_price")})

def import_from_csv(file_path="magazyn.csv"):
    list.clear(item_list)
    with open(file_path, newline='') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            item_list.append({"name":row['name'],"quantity":float(row['quantity']),"unit":row['unit'],"unit_price":float(row['unit_price'])},)

import_from_csv()
user_input()