import Return
import Addbook
import ListSplit
import dt
import Borrow

def start():
    while True:
        print("       Welcome to Library Management System   ")
        print("-"*45)
        print("Enter 1. To Display books")
        print("Enter 2. To Borrow books")
        print("Enter 3. To Add books ")
        print("Enter 4. To Return books ")
        print("Enter 5. To Exit")
        try:
            a=int(input("Select a choice from (1-5): "))
            print()
            if a==1:
                with open("stock.txt","r")as f:
                    lines=f.read()
                    print(lines)
                    print()
            elif a==2:
                ListSplit.listSplit()
                Borrow.borrowBook()
            elif a==3:
                Addbook.addbook()
            elif a==4:
                ListSplit.listSplit()
                Return.returnBook()
            elif a==5:
                print("Thank you for using library management system")
                break
            else:
                print("Please enter a valid choice from(1-5)")
        except ValueError:
            print("Please input as suggested .")
start()
