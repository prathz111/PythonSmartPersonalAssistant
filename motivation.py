import random

from bs4 import BeautifulSoup
import requests
import urllib.request

authors = []
quotes = []

def scrape_website():
    page_number=random.randint(1,50)
    page_number=str(page_number)
    print(page_number)
    URL = 'https://www.goodreads.com/quotes/tag/inspirational?page='+page_number
    webpage = requests.get(URL)
    soup = BeautifulSoup(webpage.text, 'html.parser')
    quoteText = soup.find_all('div', attrs={'class': 'quoteText'})
    l=[]
    for i in quoteText:
        quote = i.text.strip().split('\n')[0]
        l.append(quote)
    quote1=random.choice(l)
    print(quote1)
    return quote1

def main():
    scrape_website()

if __name__ == '__main__':
    main()





