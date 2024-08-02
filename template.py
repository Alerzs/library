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


    def add_new_book(self , name ,author , genre , quantity):
        #adds new book and append in books_list
        pass

    def search_book_name(self , name):
        #iterates in books_list whenever its name is equal to input name returns the book object otherwise returns false
        pass

    def search_book_author(self , author):
        #like previous method but this time returns a list of book object that has the given author
        pass

    def search_book_genre(self , genre):
        #similar to author search
        pass

    def search_menu(self):

        print("press 'A' to search by author")
        print("press 'N' to search by books name")
        print("press 'G' to search by genre")
        inp = input().upper()

        if inp == "A":
            author = input("please enter author name")
            return self.search_book_author(author)
        elif inp == "N":
            name = input("please enter book name")
            return self.search_book_name(name)
        elif inp == "G":
            genre = input("please enter genre")
            return self.search_book_genre(genre)
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
    
    def add_rent(self , book_obj , rent_obj):
        #creat a tuple out of book obj and rent obj and append it into self.rent_list
        pass





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
        with open('member_data.pkl', 'wb') as otp:
            pickle.dump(self.member_list , otp)




    def add_member(self , name ,code_meli):
        #append member object in member_list
        pass

    def show_all_rent(self):
        #for each Member object in members_list show its rent_list
        pass

    def search_members(self ,code_meli):
        #search member_list for a matching code_meli and returns Member object if not existed return false
        pass

class Rent:

    def __init__(self , start_month , duration) -> None:
        self.__start_month = start_month
        self.__duration = duration
        self.__fine = self.fine_calculate(self , start_month , duration)

    def fine_calculate(self , start_month , duration):
        takhir =  ((int(start_month) + int(duration)) % 12 )
        if takhir > 0:
            jarime = f"{10 * int(takhir)} $"
            return jarime
        return None
     



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
    inp = input()

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
        current_book.set_quantity(inp("enter new quantity : "))
    elif inp == "S":
        books.search_menu()
    elif inp == "R":
        current_member = member.search_members(input("enter members code meli : "))
        print("choose the rented book : ")
        current_book = books.search_menu()
        current_member.add_rent(current_book , Rent(input("enter rents starting month : ") , input("enter rents duration (in month) :")))
    elif inp == "L":
        member.show_all_rent()
    elif inp == "X":
        books.save_book()
        member.save_member()
        exit()











    
    
