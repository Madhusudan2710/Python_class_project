import dt
import ListSplit
import Addbook

def borrowBook():
    success=False
    while True:
        firstName=input("Enter the first name of the borrower = ")
        if firstName.isalpha():
            break
        print("Please input alphabet A-z")
    while True:
        lastName=input("Enter the last name of the borrower = ")
        if lastName.isalpha():
            break
        print("Please input alphabet A-z")
    t="Borrow-"+firstName+".txt"
    with open (t,"w+") as f:
        f.write("\t"*4+"Library Management System\n")
        f.write("\t"*4+"   Borrowed By: "+firstName.title()+lastName.title()+"\n")
        f.write("\tDate : "+dt.getDate()+"\t"*4+"Time: "+dt.getTime()+"\n\n")
        f.write("S.N.\t\tBookname"+"\t"*4+"Authorname\n")
    while success ==False:
        print("Please select a option below ")
        for i in range(len(ListSplit.bookname)):
            print("Enter",i,"to borrow book",ListSplit.bookname[i])
        try:
            a=int(input())
            try:
                if (int(ListSplit.quantity[a])>0):
                    print("Book is available !")
                    with open (t,"a")as f:
                        f.write("1.\t\t"+ListSplit.bookname[a]+"\t"*4+ListSplit.authorname[a]+"\n")
                    ListSplit.quantity[a]=int(ListSplit.quantity[a])-1
                    with open("stock.txt","w+") as f:
                        for i in range(len(ListSplit.bookname)):
                            f.write(ListSplit.bookname[i]+','+ListSplit.authorname[i]+','+str(ListSplit.quantity[i])+','+'$'+ListSplit.cost[i]+'\n')
                    #success=False
                    #multiple book borrowing code
                    loop=True
                    count=1
                    while loop==True:
                        choice=input("Do you want to borrow  more books? However you cannot borrow same book twice.Press Y for Yes and N for No.")
                        if choice.upper() == "Y":
                            count+=1
                            print("Please select an option below :")
                            for i in range (len(ListSplit.bookname)):
                                print("Enter ",i," to borrow book ",ListSplit.bookname[i])
                            a=int(input())
                            if (int(ListSplit.quantity[a])>0):
                                print("Book is available !")
                                with open (t,"a")as f:
                                    f.write(str(count)+".\t\t"+ListSplit.bookname[a]+"\t"*4+ListSplit.authorname[a]+"\n")
                                ListSplit.quantity[a]=int(ListSplit.quantity[a])-1
                                with open("stock.txt","w+") as f:
                                    for i in range(len(ListSplit.bookname)):
                                        f.write(ListSplit.bookname[i]+','+ListSplit.authorname[i]+','+str(ListSplit.quantity[i])+','+'$'+ListSplit.cost[i]+'\n')
                                        success = False
                            else:
                                loop=False
                                break
                        elif(choice.upper()=='N'):
                            print("Thank you for borrowing books from us.")
                            print(" ")
                            loop=False
                            success=True
                        else:
                            print("Please choose as instructed")
                            
                        
                else:
                    print("Book is not available")
                    borrowBook()
                    success=False
            except IndexError:
                print(" ")
                print("Please choose book acording to their number .")
        except ValueError:
            print(" ")
            print("Please choose as suggested !")
#borrowBook()
