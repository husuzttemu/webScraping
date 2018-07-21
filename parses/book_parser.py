import  re

from locators.book_locators import BookLocators

class BookParser:

    def __init__(self,parent):
        self.parent = parent

    def __repr__(self):
        return f' "{self.title}" is written by {self.author} and selling only {self.price}₺. it was {self.oldprice} '


    @property
    def title(self):
        locator = BookLocators.TITLE
        return self.parent.select_one(locator).string

    @property
    def price(self):
        locator = BookLocators.PRICE
        item_price = (self.parent.select_one(locator).string).replace(',','.')
      #  print(item_price)
      #  return item_price
        pattern = '([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        return (matcher.group(1))

    @property
    def oldprice(self):
        locator = BookLocators.OLDPRICE
        item_price = (self.parent.select_one(locator).string).replace(',', '.')
        print('a ' + item_price)
        #  return item_price
        pattern = '([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        return (matcher.group(1))

    @property
    def author(self):
        locator = BookLocators.AUTHOR
        return self.parent.select_one(locator).string