def addbook():
    n=int(input("How many no. of book want you add? "))
    with open("stock.txt",'a')as fin:
        for i in range(1,n+1):
            print(f"Enter book {i} Details\n")
            book_name = input("Enter book name = ")
            Author_name = input("Enter author name = ")
            quantity = int(input("Enter the quantity = "))
            price = input("Enter price = ")
            rec=book_name.title()+','+Author_name.title()+','+str(quantity)+','+'$'+price+'\n'
            fin.write(rec)
        print()
#addbook()
            
