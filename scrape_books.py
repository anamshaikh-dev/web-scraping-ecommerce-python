import requests
from bs4 import BeautifulSoup
import csv

# Website URL
url = "https://books.toscrape.com/"

# Send request to website
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all book containers
books = soup.find_all("article", class_="product_pod")

# List to store scraped data
book_data = []

# Loop through each book
for book in books:
    book_name = book.h3.a["title"]
    book_price = book.find("p", class_="price_color").text
    book_rating = book.find("p", class_="star-rating")["class"][1]

    book_data.append([book_name, book_price, book_rating])

# Save data into CSV file
with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Book Name", "Price", "Rating"])
    writer.writerows(book_data)

print("Data scraped successfully and saved to books.csv")