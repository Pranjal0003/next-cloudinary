import numpy as np
import random
from datetime import datetime, timedelta
import pandas as pd

def random_date(start, end):
    delta = end - start
    random_days = random.randrange(delta.days)
    return start + timedelta(days=random_days)

start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 10, 30)

num_rows = 200

random_dt = random_date(start_date, end_date)
random_dates = [random_date(start_date, end_date).strftime("%Y-%m-%d") for _ in range(num_rows)]


record={
"income":[{"date":random_dates,
        "income_source":np.random.choice(['salary', 'freelance'], num_rows),
        "category":np.random.choice(['income'], num_rows),
        "amount":np.random.uniform(30000, 150000, size=num_rows),
        "payment_method":np.random.choice(['online payment', 'cash', 'upi', 'g-pay'], num_rows),
        "description":np.random.choice(['yes','no'], num_rows),}
        ],
"expenses": [{"date": random_dates, 
        "category": np.random.choice(['wages','rent','maintanence','utilities','taxes','insurence','billing'], num_rows), 
        "description": np.random.choice(['yes','no'], num_rows), 
        "amount":np.random.uniform(0, 15000, size=num_rows),
        "type": np.random.choice(['expense'], num_rows),}
        ],
# "Invest":[{"date":random_dates,
#         "amount":10000,
#         "source_of_invest":"Ngo", 
    # }
# ]
}

df = pd.DataFrame(record)
print(df)

df.to_csv('random_financial_data.csv', index=False)

def menu_record():
    for choice in range(1,7):
        print("1. Add Record")
        print("2. View Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Show Summary")
        print("6. Exit")
        choice=input("Enter your choice: ")
        if choice=='1':
            insert()
        elif choice=='2':
            view()
        elif choice=='3':
            update()
        elif choice=='4':
            delete()
        elif choice=='5':
            summary(record)
        elif choice=='6':
            exit
        else:
            print("Invalid choice ! please enter valid choice")


def view():
    for attribute_type in record:
        print(attribute_type)
        for attribute in record[attribute_type]:
            print(attribute)
    print("\n")


def update():
    try:
        category=input("Enter category to Update(incom/expense): ")
        if category not in record:
            raise ValueError("Invalid Category!")
        date=input("Enter the date of record that you want to update (YYYY-MM-DD): ")
        for recs in record:
            for rec in record[recs]:
                if rec["date"]==date:
                    rec["income_source"]=input("Enter new income_source: ")
                    rec["category"]=input("Enter new category: ")
                    rec["amount"]=input("Enter new amount: ")
                    rec["payment_method"]=input("Enter new payment_method: ")
                    rec["description"]=input("Enter new description: ")
                    print("record Updated Successfully...")
                    return
        print("Report not found")
    except ValueError as v:
        print("Error",v)


def delete():
    try:
        category=input("Enter category to delete(income/expense): ")
        if category not in record:
            raise ValueError("Invalid Category!")
        date=input("Enter the date of record that you want to update (YYYY-MM-DD)")
        for recs in record:
            for rec in record[recs]:
                if rec["date"]==date:
                    record[category].remove(rec)
                    print("Record deleted successfully.")
                    return
        print("Record not found.")
    except ValueError as v:
        print(v)


def insert():
    try:
        date=input("Enter date: ")
        income_source=input("enter source of income: ")
        category=input("Enter Category: ")
        amount=input("Enter amount: ")
        payment_method=input("Enter payment method: ")
        description=input("Enter Description: ")
        if category not in record:
            raise ValueError("Invalid Category!")
        record_dict = {'date': date,'income_source':income_source,'category': category,'amount': amount,'payment_method':payment_method,'description': description}
        record[category].append(record_dict)
        print("record inserted successfully...")
    except ValueError as e:
        print(f"Error: {e}")



def summary(records, record_type):
    # record_type_1=record["expenses"]
    # record_type_2=record["income"]

    total_income = summary(record, record_type=record["income"])
    total_expenses = summary(record, record_type=record["expenses"])
    net_savings = total_income - total_expenses
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Net Savings: {net_savings}")
    sum_1=[sum(record['amount']) for record in records[record_type]]

    return sum_1

menu_record()

