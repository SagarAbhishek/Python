class Library:
    def __init__(self,list_of_books):
        self.books=list_of_books
    
    def AvailableBooks(self):
        print("The Available books in the library is:")
        for book in self.books:
            print("\t* "+book)
    
    def BorrowBooks(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName} book. Please return it ontime.")
            self.books.remove(bookName)
        else:
            print(f"Sorry, {bookName} is not available now. Please wait until book is available.")
        
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning it. Hope you enjoyed reading it.")

class Student:

    def requestBook(self):
        self.reqBook=input("Enter the name of book you want: ")
        return self.reqBook
    
    def returnBook(self):
        self.retBook=input("Enter the name of book you want to Add or return: ")
        return self.retBook
    
if __name__ =="__main__":
    CentralLibrary=Library(['data structure','algorithm','C program','c++','Python'])
    student=Student()

    while(True):
        msg='''\n======== WELCOME TO CENTRAL LIBRARY ========
                    Please choose an option
                    1.List of Available Book.
                    2.Request a Book.
                    3.Add/Return a Book.
                    4.Exit from Library.
        '''
        print(msg)
        a=int(input("Enter Your Choice: "))
        if a==1:
            CentralLibrary.AvailableBooks()
        elif a==2:
            bookName=student.requestBook()
            CentralLibrary.BorrowBooks(bookName)
        elif a==3:
            bookReturn=student.returnBook()
            CentralLibrary.returnBook(bookReturn)
        elif a==4:
            print("Thanks for Choosing Central Library. Have a great day Ahead!")
            exit()
        else:
            print("Invalid Choice")



