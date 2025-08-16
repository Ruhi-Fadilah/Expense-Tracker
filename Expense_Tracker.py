import csv

def add_expense():
    date=input("Enter Date(DD/MM/YYYY): ")
    category=input("Enter Category: ")
    amount=input("Enter Amount: ")

    with open("expense.csv" , "a" , newline="") as file:
        writing= csv.writer(file)
        writing.writerow([date, category, amount])
    print("Expense added successfully!")



def view_expense():
    try:
        with open ("expense.csv", "r") as file:
            read= csv.reader(file)
            print("\nDate\t\tCategory\tAmount")
            for row in read:
                print(f"{row[0]}\t{row[1]}\t\t{row[2]}")
    except FileNotFoundError:
        print("No expense found. Please Add some first")



def total_expense():
    total=0
    try:
        with open("expense.csv", "r") as file:
            read = csv.reader(file)
            next(read)
            for row in read:
                total += float(row[2])
        print(f"Total expense: {total}")
    except FileNotFoundError:
        print("No expense detected. Add some first!")


def delete_expense():
    try:
        with open ("expense.csv", "r") as file:
            read= list(csv.reader(file))

        if not read:
            print("No expense to delete")
            return
        
        print("\nExpenses present: ")
        for i, row  in enumerate(read,1):
            print(f"{i}. {row[0]} | {row[1]} | {row[2]}")

        
        choice = int (input("Enter the number of expense you want to delete: "))
        if 1<= choice <=len(read):
            removed = read.pop(choice - 1)

            with open("expense.csv", "w", newline="") as file:
                write = csv.writer(file)
                write.writerows(read)
            print(f"Deleted expense: {removed}\n")
        else:
            print ("Invalid number")
    except FileNotFoundError:
        print("No expense detected. Add some first!") 

def main():
    while True:
        print("---Expense Tracker---")
        print("1. Add expense")
        print("2. View expense")
        print("3. total Expense")
        print("4. Delete Expense")
        print("5. Exit")
       
        option = input("Enter your option: ")

        if option=="1":
            add_expense()
        elif option=="2":
            view_expense()
        elif option=="3":
            total_expense()
        elif option=="4":
            delete_expense()
        elif option=="5":
            print("Okay then until next time!!")
        else:
            print("Please enter a valid option ")
main()

