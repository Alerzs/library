import pickle

class Book:

    def __init__(self , name , author ,genre , quantity) -> None:
        self.__name = name
        self.__author = author
        self.__genre = genre
        self.__quantity = quantity

    def get_name(self):
        return self.__name
    
    def get_author(self):
        return self.__author
    
    def get_genre(self):
        return self.__genre
    
    def get_quantity(self):
        return self.__quantity

    
    def set_quantity(self ,new_quantity):
        self.__quantity = new_quantity
        

class BookManager:

    def __init__(self) -> None:
        try:
            with open('books_data.pkl', 'rb') as inp:
                data = pickle.load(inp)
                inp.close()
                self.books_list = data
        except:
            self.books_list = []
    
    def save_book(self):
        with open('books_data.pkl', 'wb') as otp:
            pickle.dump(self.books_list , otp)


    def add_new_book(self, name, author, genre, quantity):

        for book in self.books_list:
            if book.get_name() == name:
                print("This book already exists.")
                return
        new_book = Book(name , author , genre , quantity)
        self.books_list.append(new_book)
        print("New book added!")

    def search_book_name(self, name):
        for book in self.books_list:
            if book.get_name() == name:
                return book
        return False

    def search_book_author(self, author):
        result = []
        for book in self.books_list:
            if book.get_author() == author:
                result.append(book)
        return result


    def search_book_genre(self, genre):
        result = []
        for book in self.books_list:
            if book.get_genre() == genre:
                result.append(book)
        return result



    def search_menu(self):

        print("press 'A' to search by author")
        print("press 'N' to search by books name")
        print("press 'G' to search by genre")
        inp = input().upper()

        if inp == "A":
            author = input("please enter author name : ")
            result = self.search_book_author(author)
            if result:
                print("   book name\tauthor\tgenre\tquantity\n")
                for indx , book in enumerate(result):
                    print(f"{indx+1})  {book.get_name()}         {book.get_author()}\t{book.get_genre()}\t{book.get_quantity()}")
            else:
                print("no match found")
            num = input("enter your choice number : ")
            try:
                return self.books_list[int(num)-1]
            except:
                return False
            
        elif inp == "N":
            name = input("please enter book name : ")
            result = self.search_book_name(name)
            if result:
                print("book name\tauthor\tgenre\tquantity\n")
                print(f"{result.get_name()}\t\t\t{result.get_author()}\t{result.get_genre()}\t{result.get_quantity()}")
                return result
            else:
                print("no match found")    

        elif inp == "G":
            genre = input("please enter genre : ")
            result = self.search_book_genre(genre)
            if result:
                print("   book name\tauthor\tgenre\tquantity\n")
                for indx , book in enumerate(result):
                    print(f"{indx+1})  {book.get_name()}         {book.get_author()}\t{book.get_genre()}\t{book.get_quantity()}")
            else:
                print("no match found")
            num = input()
            try:
                return self.books_list[int(num)-1]
            except:
                return False
        else:
            print("wrong option")
            self.search_menu()

class Member:

    def __init__(self ,name ,code_meli) -> None:
        self.__name = name
        self.__code_meli = code_meli
        self.__rent_list = []

    def get_name(self):
        return self.__name
    
    def get_code_meli(self):
        return self.__code_meli
    
    def get_rent_list(self):
        return self.__rent_list

    def add_rent(self, book_obj, rent_obj):  
        self.__rent_list.append((book_obj, rent_obj))  




class MemberManager:

    def __init__(self) -> None:
        try:
            with open('member_data.pkl', 'rb') as inp:
                data = pickle.load(inp)
                inp.close()
                self.member_list = data
        except:
            self.member_list = []

    def save_member(self):
        with open('member_data.pkl', 'wb') as otp:
            pickle.dump(self.member_list , otp)


    def add_member(self , name ,code_meli):
        for member in self.member_list:
            if member.get_code_meli == code_meli:
                print("a member with submited code meli already exists")
                return
        self.member_list.append(Member(name ,code_meli))
        print("the member was added successfully")
        

    def show_all_rent(self):
        print("member name\tcode meli\tbook name\tstarting month\tduration\tfine")
        for member in self.member_list:
            rent_list = member.get_rent_list()
            if rent_list:
                for i in rent_list:
                    book = i[0]
                    rent = i[1]
                    print(f"{member.get_name()}\t\t{member.get_code_meli()}\t\t{book.get_name()}\t\t{rent.get_start_month()}\t\t{rent.get_duration()}\t\t{rent.get_fine()}")

        
    def search_members(self ,code_meli):
        for member in self.member_list:
            if  member.get_code_meli() == code_meli:
                return member
        return False
                

class Rent:

    def __init__(self , start_month , duration) -> None:
        self.__start_month = start_month
        self.__duration = duration
        self.__fine = self.fine_calculate(start_month , duration)


    @staticmethod
    def fine_calculate(start_month , duration):
        takhir =  ((int(start_month) + int(duration)) % 12 )
        if takhir > 0:
            jarime = f"{10 * int(takhir)} $"
            return jarime
        return None
    
    def get_start_month(self):
        return self.__start_month
    
    def get_duration(self):
        return self.__duration
    
    def get_fine(self):
        return self.__fine
     



#====================================================  menu  ====================================================

member = MemberManager()
books = BookManager()

while True:
    print("press 'A' to add new member")
    print("press 'B' to add new book")
    print("press 'Q' to change book inventory")
    print("press 'S' to search books")
    print("press 'R' to add new rent")
    print("press 'L' to see rent list")
    print("press 'X' to exit")
    inp = input().upper()

    if inp == "A":
        name = input("members name : ")
        code = input("members code meli : ")
        member.add_member(name , code)

    elif inp == "B":
        name = input("enter books name : ")
        author = input("enter author name : ")
        genre = input("enter books genre : ")
        quantity =input("enter books count : ")
        books.add_new_book(name , author , genre , quantity)

    elif inp == "Q":
        current_book = books.search_menu()
        if current_book:
            new_quantity = int(input("enter new quantity : "))
            current_book.set_quantity(new_quantity)
        else:
            print("no match found")
            

    elif inp == "S":
        books.search_menu()


    elif inp == "R":
        current_member = member.search_members(input("enter members code meli : "))
        if current_member:
            print("choose the rented book : ")
            current_book = books.search_menu()
            if current_book:
                current_member.add_rent(current_book , Rent(input("enter rents starting month : ") , input("enter rents duration (in month) :")))
            else:
                print("no match for book")
        else:
            print("no match for person")

    elif inp == "L":
        member.show_all_rent()

    elif inp == "X":
        books.save_book()
        member.save_member()
        exit()
