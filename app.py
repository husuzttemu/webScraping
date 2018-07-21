import  requests

from books.books_page import BookPage

page_content = requests.get('http://www.dr.com.tr/search?q=steve%20jobs').content

page = BookPage(page_content)
print(page_content)

for book in page.book:
    print(book)



