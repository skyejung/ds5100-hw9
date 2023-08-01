import unittest
import pandas as pd
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test1 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test1.add_book("War of the Worlds", 4)
        expected = pd.DataFrame({'book_name':['War of the Worlds'], 'book_rating':[4]})
        message = 'The book is not in the list!'
        self.assertTrue(expected.book_name.isin(test1.book_list.book_name).bool(),message)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test2 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test2.add_book("War of the Worlds", 4)
        test2.add_book("War of the Worlds", 4)
        expected = 1
        message = 'That book is in the list twice!'
        self.assertEqual(test2.num_books_read(),expected,message)
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test3 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test3.add_book("War of the Worlds", 4)
        message = 'That book has not been read!'
        self.assertTrue(test3.has_read('War of the Worlds'),message)
      
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test4 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test4.add_book("War of the Worlds", 4)
        message = 'That book has not been read!'
        self.assertFalse(test4.has_read('The Great Gatsby'),message)
 
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test5 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test5.add_book("War of the Worlds", 4)
        test5.add_book("Jane Eyre", 4)
        test5.add_book("Fight Club", 3)
        test5.add_book("The Divine Comedy", 5)
        test5.add_book("The Popol Vuh", 5)
        expected=5
        message = 'The number of books does not match num_books'
        self.assertEqual(test5.num_books_read(),expected,message)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test6 = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test6.add_book("War of the Worlds", 4)
        test6.add_book("Jane Eyre", 4)
        test6.add_book("Fight Club", 3)
        test6.add_book("The Divine Comedy", 5)
        test6.add_book("The Popol Vuh", 5)
        test6.fav_books
        self.assertTrue(all(test6.fav_books().book_rating>3))
     
if __name__ == '__main__':
    
    unittest.main(verbosity=3)
