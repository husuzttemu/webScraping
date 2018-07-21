from bs4 import  BeautifulSoup

from locators.book_pages_locators import BookPageLocators
from parses.book_parser import BookParser

class BookPage:

    def __init__(self,page):
        self.soup = BeautifulSoup(page,'html.parser')

    @property
    def book(self):
        locator = BookPageLocators.BOOKPAGE
        booktags = self.soup.select(locator)
       # print(booktags)
        print([BookParser(e) for e in booktags])
        return [BookParser(e) for e in booktags]