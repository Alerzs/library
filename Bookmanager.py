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
        return

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