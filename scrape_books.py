import requests
from bs4 import BeautifulSoup
import csv
import time

# Base URL (multiple pages)
BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

# Output file name
OUTPUT_FILE = "books.csv"

# List to store all books
all_books = []

# Number of pages to scrape
TOTAL_PAGES = 10  

print("Starting Web Scraping Project...")
print("--------------------------------")

for page in range(1, TOTAL_PAGES + 1):
    print(f"Scraping Page {page}...")
    
    url = BASE_URL.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        # Book Name
        name = book.h3.a["title"]

        # Price
        price = book.find("p", class_="price_color").text

        # Rating
        rating = book.find("p", class_="star-rating")["class"][1]

        # Availability
        availability = book.find("p", class_="instock availability").text.strip()

        # Save data
        all_books.append([name, price, rating, availability])

    time.sleep(1)  

print("Scraping completed.")
print("Saving data to CSV file...")


with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Book Name", "Price", "Rating", "Availability"])
    writer.writerows(all_books)

print("Data saved successfully in books.csv")
print("Project completed.")