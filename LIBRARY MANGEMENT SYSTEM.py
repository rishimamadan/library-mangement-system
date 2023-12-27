import mysql.connector as my_sql
   
    # Function for new user registration
def register():
    mydb=my_sql.connect(host="localhost",user="sqluser",password="password",database="Library_Management")
    cur = mydb.cursor()
    
    enroll = int(input("\nEnter Enrollment Number : "))
    name = input("Enter Student Name : ")
    course = input("Enter Course Name : ")
    email = input("Enter Email Id : ")
    phone = int(input("Enter Phone Number : "))
    password = int(input("Enter Login Password : "))
    ins = "insert into user values(%s,'%s','%s','%s',%s,%s)"%(enroll,name,course,email,phone,password)
    cur.execute(ins)
    mydb.commit()
    print("\nNew Registration Succesful!!! Kindly login!!!")

    mydb.close()

    #Function to search a book
def  search():
    mydb= my_sql.connect(host="localhost",user="sqluser",password="password")
    cur = mydb.cursor()
    cur.execute("Use Library_Management")
    print("\nSearch By: ")
    print("\n1.ISBM Code \n2.Book Title \n3.Author Name \n4.Genre \n5.Publisher \n6.Show all books")
    a=int(input("\nPlease enter your choice number: "))

    #For search by ISBM Code
    if (a==1):
        code=int(input("Please enter ISBM code: "))
        ins="select * from book where ISBM_code='%s'"%(code)
        cur.execute(ins)
        print("___________________________________________________________")
        print("\nISBM_Code\tBook_Title\tAuthor_Name\tGenre\tPublisher\n")
        print("___________________________________________________________")
        for row in cur:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4])
    
    # For search by Book Title
    if (a==2):
        title=input("Please Enter Book Title: ")
        ins="select * from book where Book_Title='%s'"%(title)
        cur.execute(ins)
        print("___________________________________________________________")
        print("\nISBM_Code\tBook_Title\tAuthor_Name\tGenre\tPublisher\n")
        print("___________________________________________________________")
        for row in cur:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4])

    # For search by Author
    if (a==3):
        author=input("Please Enter Author Name: ")
        ins="select * from book where Author_Name='%s'"%(author)
        cur.execute(ins)
        print("___________________________________________________________")
        print("\nISBM_Code\tBook_Title\tAuthor_Name\tGenre\tPublisher\n")
        print("___________________________________________________________")
        for row in cur:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4])

    # For search by Genre
    if (a==4):
        genre=input("Please Enter Genre: ")
        ins="select * from book where Genre='%s'"%(genre)
        cur.execute(ins)
        print("___________________________________________________________")
        print("\nISBM_Code\tBook_Title\tAuthor_Name\tGenre\tPublisher\n")
        print("___________________________________________________________")
        for row in cur:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4])

    # For search by Publisher
    if (a==5):
        publisher=input("Please Enter Publisher: ")
        ins="select * from book where Publisher='%s'"%(publisher)
        cur.execute(ins)
        print("___________________________________________________________")
        print("\nISBM_Code\tBook_Title\tAuthor_Name\tGenre\tPublisher\n")
        print("___________________________________________________________")
        for row in cur:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4])
        
    # For showing all books
    if (a==6):
        ins="select * from book"
        cur.execute(ins)
        print("___________________________________________________________")
        print("\nISBM_Code\tBook_Title\tAuthor_Name\tGenre\tPublisher\n")
        print("___________________________________________________________")
        for row in cur:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4])

    mydb.close()

    # Function to issue a book
def issue():
    from datetime import date
    mydb= my_sql.connect(host="localhost",user="sqluser",password="password")
    cur = mydb.cursor(buffered=True)
    cur.execute("Use Library_Management")
    enroll=int(input("\nEnter Enrollment Number : "))
    name=input("Enter student Name : ")
    course=input("Enter Course Name : ")
    code=int(input("Enter ISBM Code of the book : "))
    title=input("Enter Book Title : ")
    author=input("Enter the Author Name : ")
    date=date.today()
    ins = "insert into issue values(%s,'%s','%s',%s,'%s','%s','%s')"%(enroll,name,course,code,title,author,date)
    cur.execute(ins)
    mydb.commit()    

    ins1="Select Issue from book where ISBM_code=%s"%code
    cur.execute(ins1)
    a=cur.fetchone()
    b=a[0]
    
    if (b=="No"):
        c='Yes'
        cur.execute("update book set issue='%s' where ISBM_Code=%s"%(c,code))
        mydb.commit()
        print("\nBook Successfully issued to",name,"!!!")
        
    if (b=="Yes"):
        print ("Sorry!!! This book is already issued")
    
    mydb.close()

    #Function to return a book
def returnbook():
    from datetime import date
    mydb= my_sql.connect(host="localhost",user="sqluser",password="password")
    cur = mydb.cursor(buffered=True)
    cur.execute("Use Library_Management")
    enroll=int(input("\nEnter Enrollment Number : "))
    name=input("Enter student Name : ")
    code=int(input("Enter ISBM Code of the book : "))
    title=input("Enter Book Title : ")
    date=date.today()
    
    c='No'
    cur.execute("update book set issue='%s' where ISBM_Code=%s"%(c,code))
    mydb.commit()

    print("\nYour Book has been sucessfully returned!!!")

    mydb.close()
    

    # Function to see user borrowing history
def history():
    from datetime import date
    mydb= my_sql.connect(host="localhost",user="sqluser",password="password")
    cur = mydb.cursor()
    cur.execute("Use Library_Management")
    enroll=int(input("\nEnter Enrollment Number : "))
    ins="Select * from issue where Enroll_no=%s"%enroll
    cur.execute(ins)
    print("_____________________________________________________________________________________________________________________")
    print("\nEnrollment Number\tName\tCourse\t\tISBM_code\tBook Title\tAuthor Name\tDate of Issue\n")
    print("_____________________________________________________________________________________________________________________")
    for row in cur:
        print(row[0],"\t\t\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5],"\t",row[6])

    mydb.close()


    #For Book Reservation
def BookReservation():
    mydb = my_sql.connect(host="localhost", user="sqluser", passwd="password",  database="Library_Management")
    cur = mydb.cursor()
    cur.execute("Use Library_Management")
    print("\n1. Reserve a book \n2. Cancel a reservation")
    choice = int(input("\nEnter your choice number: "))
    #For reserving a book
    if choice==1:        
        a = input("\nWhich book do you wish to reserve? ")
        reserve = "Update book set reserved = %s where Book_Title = '%s'"%(1,a)
        cur.execute(reserve)
        print("Congrats, the book has been successfully reserved!")
        mydb.commit()
    #For cancelling a reservation
    else:
        b = input("Which reservation do you wish to cancel? ")
        cancel = "Update book set reserved = %s where Book_Title = '%s'"%(0,b)
        cur.execute(cancel)
        print("Congrats, the book has been succesfully unreserved!")
        mydb.commit()

    mydb.close()

    #For Fine Calculation
def FineCalculation():
    mydb = my_sql.connect(host="localhost", user="sqluser", passwd="password", database="Library_Management")
    cur = mydb.cursor()
    cur.execute("Use Library_Management")
    cur.execute("select date(issue_date) as IssueDate from issue;")
    cur.execute("select Current_Date")
    cur.execute("select DateDiff(day, IssueDate, Current_Date)")
    a = input("Is the book worn/torn?")
    if a=='yes':
        b = 10
    Total = b+(c*1)
    print("The due fine is: ",Total)
    mydb.commit()

    mydb.close()

    # For Book Management
def bookmanagement():
    mydb= my_sql.connect(host="localhost",user="sqluser",password="password")
    cur = mydb.cursor()
    cur.execute("Use Library_Management")
    print("\n1.Show All Books \n2.Add a new Book \n3.Delete a book \n4.Edit a Book")
    a=int(input("\nPlease enter your choice number: "))

    # For displaying all books
    if (a==1):
        ins="select * from book"
        cur.execute(ins)
        print("___________________________________________________________")
        print("\nISBM_Code\tBook_Title\tAuthor_Name\tGenre\tPublisher\tIssued\tReserved\n")
        print("___________________________________________________________")
        for row in cur:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5],"\t",row[6])


    # For Adding a new book
    if (a==2):
        code = int(input("Enter ISBM Code : "))
        title = input("Enter Book Title : ")
        author = input("Enter Author Name : ")
        genre = input("Enter Genre : ")
        publisher = input("Enter Publisher : ")
        ins = "insert into book values(%s,'%s','%s','%s','%s','%s',%s)"%(code,title,author,genre,publisher,'No',0)
        cur.execute(ins)
        mydb.commit()

        print("Book Added Succesfully")

    # For deleting a book
    if (a==3):
        code=int(input("Enter ISBM Code : "))
        ins = "delete from book where ISBM_Code='%s'"%(code)
        cur.execute(ins)
        mydb.commit()
        
        print("Book deleted succesfully")

    # For editing a book details
    if (a==4):
        print("\nEdit")
        print("\n1.Book Title \n2.Author Name \n3.Genre \n4.Publisher")
        b=int(input("\nEnter your choice number : "))

        # For editing book title
        if (b==1):
            code=int(input("Enter any ISBM code : "))
            title=input("Enter new Book Title : ")
            ins = "update book set Book_Title='%s' where ISBM_code=%s"%(title,code)
            cur.execute(ins)
            mydb.commit()

        # For editing Author name
        if (b==2):
            code=int(input("Enter any ISBM code : "))
            author=input("Enter new Author Name : ")
            ins = "update book set Author_name='%s' where ISBM_code=%s"%(author,code)
            cur.execute(ins)
            mydb.commit()

        # For editing Genre
        if (b==3):
            code=int(input("Enter any ISBM code : "))
            genre=input("Enter new Genre : ")
            ins = "update book set Genre='%s' where ISBM_code=%s"%(genre,code)
            cur.execute(ins)
            mydb.commit()

        # For editing Publisher
        if (b==4):
            code=int(input("Enter any ISBM code : "))
            publisher=input("Enter new Publisher : ")
            ins = "update book set Publisher='%s' where ISBM_code=%s"%(publisher,code)
            cur.execute(ins)
            mydb.commit()
            
        print("Book updated succesfully")   
            
    mydb.close()
    

    # For User Management
def usermanagement():
    mydb= my_sql.connect(host="localhost",user="sqluser",password="password")
    cur = mydb.cursor()
    cur.execute("Use Library_Management")
    print("\nUser Management")
    print("\n1.Show all users \n2.Add a user \n3.Delete a User \n4.Edit User Details")
    a=int(input("\nPlease enter your choice number : "))

    # For Showing all users
    if (a==1):
        ins="select * from user"
        cur.execute(ins)
        print("___________________________________________________________")
        print("\nEnrollment Number\tName\tCourse\tEmail Id\tPhone number\tLogin Password\n")
        print("___________________________________________________________")
        for row in cur:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4],"\t",row[5])

    # For Adding a new user
    if (a==2):
        enroll = int(input("\nEnter Enrollment Number : "))
        name = input("Enter Student Name : ")
        course = input("Enter Course Name : ")
        email = input("Enter Email Id : ")
        phone = int(input("Enter Phone Number : "))
        password = int(input("Enter Login Password : "))
        ins = "insert into user values(%s,'%s','%s','%s',%s,%s)"%(enroll,name,course,email,phone,password)
        cur.execute(ins)
        mydb.commit()

        print("User Added Succesfully!!!")

    # For deleting a user
    if (a==3):
        enroll=int(input("Enter Enrollment Number : "))
        ins = "delete from user where Enroll_No=%s"%(enroll)
        cur.execute(ins)
        mydb.commit()
        
        print("User deleted succesfully!!!")

    # For editing a user details
    if (a==4):
        print("\nEdit")
        print("\n1.Student Name \n2.Course \n3.Email Id \n4.Phone Number \n5.Password")
        b=int(input("\nEnter your choice number : "))

        # For editing Student Name
        if (b==1):
            enroll=int(input("Enter any Enrollment Number : "))
            name=input("Enter new Student Name : ")
            ins = "update user set Name='%s' where Enroll_No=%s"%(name,enroll)
            cur.execute(ins)
            mydb.commit()

        # For editing Course Name
        if (b==2):
            enroll=int(input("Enter any Enrollment Number : "))
            course=input("Enter new Course Name : ")
            ins = "update user set Course='%s' where Enroll_No=%s"%(course,enroll)
            cur.execute(ins)
            mydb.commit()

        # For editing Email Id
        if (b==3):
            enroll=int(input("Enter any Enrollment Number : "))
            email=input("Enter new Email Id : ")
            ins = "update user set Email Id='%s' where Enroll_No=%s"%(email,enroll)
            cur.execute(ins)
            mydb.commit()

        # For editing Phone Number
        if (b==4):
            enroll=int(input("Enter any Enrollment Number : "))
            phone=int(input("Enter new Phone Number : "))
            ins = "update user set Phone_No=%s where Enroll_No=%s"%(phone,enroll)
            cur.execute(ins)
            mydb.commit()

        # For editing Password
        if (b==5):
            enroll=int(input("Enter any Enrollment Number : "))
            password=int(input("Enter new Password : "))
            ins = "update user set Password=%s where Enroll_No=%s"%(password,enroll)
            cur.execute(ins)
            mydb.commit()
            
        print("Book updated succesfully!!!")

    mydb.close()

    # Function for showing list of all books
def BookInventory():
    mydb = my_sql.connect(host="localhost", user="sqluser", password="password", database="Library_Management")
    cur = mydb.cursor()
    cur.execute("Use Library_Management")
    a="Select * from book where reserved = %s"%(0)
    cur.execute(a)
    print("___________________________________________________________")
    print("\nISBM_Code\tBook_Title\tAuthor_Name\tGenre\tPublisher\n")
    print("___________________________________________________________")
    for row in cur:
        print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4])

    mydb.close()

    # Function for Book Recomendation System
def BookRecommendation():
    mydb = my_sql.connect(host="localhost", user="sqluser", password="password", database="Library_Management")
    cur = mydb.cursor()
    cur.execute("Use Library_Management")
    print("\n Search By:")
    print("\n1. Author's Name \n2. Genre")
    a=int(input("\nPlease enter your choice number: "))
    #For search by Author
    if (a==1):
        author=input("Please Enter Author Name: ")
        ins="select * from book where Author_Name='%s'"%(author)
        cur.execute(ins)
        print("Based on your preferences, you may like:")
        print("___________________________________________________________")
        print("\nISBM_Code\tBook_Title\tAuthor_Name\tGenre\tPublisher\n")
        print("___________________________________________________________")
        for row in cur:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4])
    #For search by Genre
    if (a==2):
        genre=input("Please Enter Genre: ")
        ins="select * from book where Genre='%s'"%(genre)
        cur.execute(ins)
        print("Based on your preferences, you may like:")
        print("___________________________________________________________")
        print("\nISBM_Code\tBook_Title\tAuthor_Name\tGenre\tPublisher\n")
        print("___________________________________________________________")
        for row in cur:
            print(row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4])

    mydb.close()

    
     # Function to Login 
def login():
    mydb=my_sql.connect(host="localhost",user="sqluser",password="password",database="Library_Management")
    cur = mydb.cursor()

    print("\n1.Login as Admin \n2.Login as User ")
    a=int(input("\nEnter your choice number: "))

    # To login as admin
    if (a==1):
        uname=input("\nUsername : ")
        password=int(input("Password : "))
        cur.execute("Select * from admin where Username='%s' and password=%s"%(uname,password))
        if cur.fetchone():
            print("\n\t\t\tLogin Succesful!!!")

            # Giving controls to admin
            print("\t\t\tWelcome "+uname+"!!!")
            ch='y'
            while ch=='y' or ch=='Y':
                print("\n\nMenu")
                print("1.Book Search and Browsing \n2.Book Issue \n3.Book Return \n4.User borrowing history tracking")
                print("5.Book reservation System \n6.Fine Calculation \n7.Book Management")
                print("8.User Management \n9.Book Inventory \n10.Logout \n0 to exit")
                x=int(input("\nPlease enter your choice number : "))

                # For searching book
                if (x==1):
                    search()

                # For Book Issue
                if (x==2):
                    issue()

                # For Book Return
                if (x==3):
                    returnbook()

                # For User borrowing history
                if (x==4):
                    history()
    
                # For Book reservation
                if (x==5):
                    BookReservation()
    
                # For Fine Calculation
                if (x==6):
                    FineCalculation()
    
                # For Book Management
                if (x==7):
                    bookmanagement()
    
                # For User Management
                if (x==8):
                    usermanagement()
    
                # For Book Inventory
                if (x==9):
                    BookInventory()
    
                # For Logout
                if (x==10):
                    main()


                ch=input("Do you wish to continue? (Y/N)")
                
            else:
                print("\nPlease enter valid credentials")

               
    # To login as user
    if (a==2):
        enroll=int(input("\nEnrollment Number : "))
        password=int(input("Password : "))
        cur.execute("Select * from user where Enroll_no=%s and password=%s"%(enroll,password))
        if cur.fetchone():
            print("\nLogin Succesful!!!")

            print("\t\t\tWelcome")
            ch='y'
            while ch=='y' or ch=='Y':
                print("\n\nMenu")
                print("1.Book Search and Browsing \n2.Book Issue \n3.Book Return \n4.User borrowing history tracking")
                print("5.Book reservation System \n6.Fine Calculation \n7.Book Recomendation System")
                print("8.Book Inventory \n9.Logout \n0 to exit")
                x=int(input("\nPlease enter your choice number : "))

                 # For searching book
                if (x==1):
                    search()

                # For Book Issue
                if (x==2):
                    issue()

                # For Book Return
                if (x==3):
                    returnbook()

                # For User borrowing history
                if (x==4):
                    history()
    
                # For Book reservation
                if (x==5):
                    BookReservation()

                #Fine Calculation
                if (x==6):
                    FineCalculation()

                # Book Recomendation System
                if (x==7):
                    BookRecommendation()

                 # For Book Inventory
                if (x==8):
                    BookInventory()

                # For Logout
                if (x==9):
                    main()

                ch=input("Do you wish to continue? (Y/N)")

                    
    else:
        print("\nPlease enter valid credentials")

    mydb.close()

    
print("\t\t\t\tWelcome to Library Management System!!!")
print("\n\n")
def main():
    print("\n\nMenu")
    print("\n1.Login \n2.New Registration \n3.Book Search and Browsing \n4.Issue Book \n5.Return Book ")
    print("6.Logout \n0 to exit")
    c=int(input("\nPlease enter your choice number : "))

    # For login
    if (c==1):
        login()
    # For new registration
    if (c==2):
        register()
    # For searching books
    if (c==3):
        search()
    # For Book Issue
    if (c==4):
        issue()
    #For returning a book
    if (c==5):
        returnbook()
        
main()