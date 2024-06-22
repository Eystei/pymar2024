import xml.etree.ElementTree as ET
from operator import itemgetter
from datetime import datetime
import pprint

# XML data
XML_DATA = '''<?xml version="1.0"?>
<catalog>
    <book id="bk101">
        <author>Gambardella, Matthew</author>
        <title>XML Developer's Guide</title>
        <genre>Computer</genre>
        <price>44.95</price>
        <publish_date>2000-10-11</publish_date>
        <description>An in-depth look at creating applications with XML.</description>
    </book>
    <book id="bk102">
        <author>Ralls, Kim</author>
        <title>Midnight Rain</title>
        <genre>Fantasy</genre>
        <price>5.95</price>
        <publish_date>2000-12-16</publish_date>
        <description>A former architect battles corporate zombies, an evil sorceress, and her own childhood to become queen of the world.</description>
    </book>
    <book id="bk103">
        <author>Corets, Eva</author>
        <title>Maeve Ascendant</title>
        <genre>Fantasy</genre>
        <price>7.00</price>
        <publish_date>2001-11-17</publish_date>
        <description>After the collapse of a nanotechnology society in England, the young survivors lay the foundation for a new society.</description>
    </book>
</catalog>'''

# Parse XML data
root = ET.fromstring(XML_DATA)

# Convert XML data to a list of dictionaries
books = []
for book in root.findall('book'):
    book_data = {
        'id': book.get('id'),
        'author': book.find('author').text,
        'title': book.find('title').text,
        'genre': book.find('genre').text,
        'price': float(book.find('price').text),
        'publish_date': book.find('publish_date').text,
        'description': book.find('description').text.strip()
    }
    books.append(book_data)

# 1. Print the IDs of all books
print("IDs of all books:")
for book in books:
    print(book['id'])

# 2. Count the number of books and print it
print("\nNumber of books:", len(books))

# 3. Sort books by price
books_sorted_by_price = sorted(books, key=itemgetter('price'))
print("\nBooks sorted by price:")
pprint.pprint(books_sorted_by_price)

# 4. Sort books by publish date
books_sorted_by_date = sorted(books, key=lambda x: datetime.strptime(x['publish_date'], '%Y-%m-%d'))
print("\nBooks sorted by publish date:")
pprint.pprint(books_sorted_by_date)

# 5. Print books published in 2000
print("\nBooks published in 2000:")
books_2000 = [book for book in books if book['publish_date'].startswith('2000')]
pprint.pprint(books_2000)

# 6. Find books in the genre 'Computer'. Print their author, publish date, price, and description
print("\nBooks in the genre 'Computer':")
computer_books = [book for book in books if book['genre'] == 'Computer']
for book in computer_books:
    print(f"Author: {book['author']}, "
          f"Publish Date: {book['publish_date']}, "
          f"Price: {book['price']}, "
          f"Description: {book['description']}")
