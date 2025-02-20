#!/usr/bin/env python3
import sys

class Book:
    def __init__(self, title, page_count):  
        self.title = title
        self.page_count = page_count  

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Title must be a non-empty string")
        self._title = value

    @property
    def page_count(self):  # ✅ FIX: Added `self`
        return self._page_count  # ✅ FIX: Returns the correct attribute
    
    @page_count.setter
    def page_count(self, value):  
        if not isinstance(value, int):
            print("page_count must be an integer")  
        elif value <= 0:
            raise ValueError("Page count must be a positive integer")
        else:
            self._page_count = value  # ✅ FIX: Sets the correct attribute

    # ✅ `turn_page` method
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

# ✅ Test the class
my_book = Book("Harry Potter", 350)
print(f"Page Count: {my_book.page_count}")  # ✅ Should print 350
my_book.turn_page()  # ✅ Should print: "Flipping the page...wow, you read fast!"
