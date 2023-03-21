from bs4 import BeautifulSoup
import csv
with open('page20.html', 'r' , encoding='utf-8') as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')
divs = soup.find_all('div', class_='sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 AdHolder sg-col s-widget-spacing-small sg-col-12-of-16')

with open('data20.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Link', 'Title', 'Rating', 'Price', 'Reviews'])
    for div in divs:
        try:
            img = div.find('img', class_='s-image')
            link = img['src']
        except:
            link = ''
        try:
            title = div.find('span', class_='a-size-medium a-color-base a-text-normal').text.strip()
        except:
            title = ''
        try:
            rating = div.find('span', class_='a-icon-alt').text.strip()
        except:
            rating = ''
        try:
            price = div.find('span', class_='a-price-whole').text.strip()
        except:
            price = ''
        try:
            reviews = div.find('span', class_='a-size-base s-underline-text').text.strip()
        except:
            reviews = ''
        writer.writerow([link, title, rating, price, reviews])
