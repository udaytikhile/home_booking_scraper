import os 
from datetime import datetime

def add_new():
    amount = input("Enter amount : ₹")
    category= input("Enter category (food , travle, etc..):")
    date= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note= input("Enter note :")

    with open ("expense.txt","a") as f:
        f.write(f"{date}|{amount}|{category}|{note}\n")
        print("Expense Add ")


def view ():
    if not os.path.exists("expense.txt"):
        print("file NotFound \n")
        return
    
    print("All expenses")
    with open ("expense.txt","r") as f:
        for line in f:
            print(line.strip())

def total_monthly():
    if not os.path.exists("expense.txt"):
        print("file NotFound \n")
        return
    
    month=input("Enter like..(YYYY-MM):")

    total=0
    with open ("expense.txt","r") as f:
        for line in f:
            if month in line:
                try:
                    part=line.split("|")
                    amount=part[1].strip().replace("₹","")
                    total +=float(amount)
                except:
                    continue
        print(f"\n📊 Total expense for {month}: ₹{total}\n")


def total_by_category():
    if not os.path.exists("expense.txt"):
        print("file NotFound \n")
        return

    category_totals = {}

    with open("expense.txt", "r") as f:
        for line in f:
            try:
                parts = line.strip().split("|")
                amount = float(parts[1].replace("₹", "").strip())
                category = parts[2].strip()

                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount
            except:
                continue

    print("\n📊 Category-wise Totals:")
    for cat, amt in category_totals.items():
        print(f"  {cat}: ₹{amt}")
    print()

            


def mean():

    while True:
        print("===Expense Tracker===") 
        print("1:Add new expense ")
        print("2:Veiw expense ")
        print("3:Total of monthly expense ")
        print("4:The Category Total ")
        print("5:Exit ")

        choice=input("Enter choice (1/2/3/4):")

        if choice == "1":
            add_new()
        elif choice == "2":
            view()
        elif choice == "3":
            total_monthly()
        elif choice == "4":
            total_by_category()
        elif choice == "5":
            print("Good bye...")
            break
             


mean()          
        

