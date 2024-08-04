import pickle  

class Book:  
    def __init__(self, name, author, genre, quantity) -> None:  
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

    def set_quantity(self, new_quantity):  
        self.__quantity = new_quantity  


class BookManager:  
    def init(self) -> None:  
        try:  
            with open('books_data.pkl', 'rb') as inp:  
                data = pickle.load(inp)
                self.books_list = data  
        except:  
            self.books_list = []  

    def save_book(self):  
        with open('books_data.pkl', 'wb') as otp:  
            pickle.dump(self.books_list, otp)  

    def add_new_book(self, name, author, genre, quantity):  
        for book in self.books_list:  
            if book.get_name() == name:  
                print("This book already exists.")  
                return  
        new_book = Book(name, author, genre, quantity)  
        self.books_list.append(new_book)  
        self.save_book()  
        print("New book added!")  

    def search_book_name(self, name):  
        for book in self.books_list:  
            if book.get_name() == name:  
                return book  
        return None  

    def search_book_author(self, author):  
        result = []  
        for book in self.books_list:  
            if book.get_author() == author:  
                result.append(book)  
        if result:
            return result
        else:
            return  

    def search_book_genre(self, genre):  
        result = []  
        for book in self.books_list:  
            if book.get_genre() == genre:  
                result.append(book)  
        if result:
            return result
        else:
            return  

    def search_menu(self):  
        print("Press 'A' to search by author")  
        print("Press 'N' to search by book's name")  
        print("Press 'G' to search by genre")  
        inp = input().upper()  

        if inp == "A":  
            author = input("Please enter author name: ")  
            return self.search_book_author(author)  
        elif inp == "N":  
            name = input("Please enter book name: ")  
            return self.search_book_name(name)  
        elif inp == "G":  
            genre = input("Please enter genre: ")  
            return self.search_book_genre(genre)  
        else:  
            print("Wrong option")  
            return self.search_menu()  


class Member:  
    def __init__(self, name, code_meli) -> None:  
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
            with open('members_data.pkl', 'rb') as inp:  
                data = pickle.load(inp)
                inp.close()
                self.member_list = data  
        except:  
            self.member_list = []  

    def save_member(self):  
        with open('members_data.pkl', 'wb') as otp:  
            pickle.dump(self.member_list, otp)  

    def add_member(self, name, code_meli):
        self.name = name
        self.code_meli = code_meli
        for member in self.member_list :
            if member.get_code_meli() == self.code_meli:
                return
        self.member_list.append(self.member)

    def show_all_rents(self):  
        c = ""
        for member in self.member_list:
            a = member
            b = Member.get_rent_list()
            c = f"{c} \n   {a}  {str(b)} " 
        return c
        
    def search_members(self, code_meli):  
        for member in self.member_list:  
            if member.get_code_meli() == code_meli:  
                return member  
        return None  


class Rent:  
    def __init__(self, start_month, duration) -> None:  
        self.__start_month = start_month  
        self.__duration = duration  
        self.__fine = self.fine_calculate(start_month, duration)  

    def fine_calculate(self, start_month, duration):  
        takhir = (int(start_month) + int(duration)) % 12  
        if takhir > 0:  
            jarime = f"{10 * takhir} $"  
            return jarime  
        return None  

#====================================================  menu  ====================================================  

member_manager = MemberManager()  
book_manager = BookManager()  

while True:  
    print("Press 'A' to add new member")  
    print("Press 'B' to add new book")  
    print("Press 'Q' to change book inventory")  
    print("Press 'S' to search books")  
    print("Press 'R' to add new rent")  
    print("Press 'L' to see rent list")  
    print("Press 'X' to exit")  
    inp = input().upper()  

    if inp == "A":  
        name = input("Member's name: ")  
        code = input("Member's code meli: ")  
        member_manager.add_member(name, code)  

    elif inp == "B":  
        name = input("Enter book's name: ")  
        author = input("Enter author name: ")  
        genre = input("Enter book's genre: ")  
        quantity = int(input("Enter book count: "))  
        book_manager.add_new_book(name, author, genre, quantity)  

    elif inp == "Q":  
        current_book = book_manager.search_menu()  
        if current_book:  
            new_quantity = int(input("Enter new quantity: "))  
            current_book.set_quantity(new_quantity)  
            book_manager.save_book()  
            print("Book quantity updated.")  

    elif inp == "S":  
        results = book_manager.search_menu()  
        if results:  
            if isinstance(results, list):  
                for book in results:  
                    print(f"Found Book: {book.get_name()} by {book.get_author()}")  
            else:  
                print(f"Found Book: {results.get_name()} by {results.get_author()}")  

    elif inp == "R":  
        current_member = member_manager.search_members(input("Enter member's code meli: "))  
        if current_member:  
            print("Choose the rented book:")  
            current_book = book_manager.search_menu()  
            if current_book:  
                rent = Rent(input("Enter rent's starting month: "), input("Enter rent's duration (in months): "))  
                current_member.add_rent(current_book, rent)  
                print("Rent added.")  
        else:  
            print("Member not found.")  

    elif inp == "L":  
        member_manager.show_all_rents()  

    elif inp == "X":  
        book_manager.save_book()  
        member_manager.save_member()    
        exit()


