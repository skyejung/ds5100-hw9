import pandas as pd
class BookLover():
    def __init__(self, name, email, fav_genre, num_books=0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
        
    def add_book(self,book_name, book_rating):
        if book_name in list(self.book_list.book_name):
            print(f'{book_name} already in list.')
        else:
            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [book_rating]
            })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        
    def has_read(self,book_name):
        return book_name in list(self.book_list.book_name)
    
    def num_books_read(self):
        return len(self.book_list)
    
    def fav_books(self):
        favs = self.book_list.query("book_rating>3")
        return favs
