from bs4 import BeautifulSoup
import requests
import csv
from selenium import webdriver

csv_file = open('Amazon.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['product_name', 'product_rating', 'num_of_reviews', 'product_price'])

driver = webdriver.Chrome()

productName = "lg tv"
productName = productName.replace(' ','+')

def url(i):
	url=f"https://www.amazon.in/s?k={productName}&page={i}&crid=2HPF3IZH5D4TR&qid=1607409586&sprefix=sam%2Caps%2C306&ref=sr_pg_2"
	return url

def extraction(section):
	try:
		product_name = section.find('span', class_="a-size-medium a-color-base a-text-normal").text
		product_name = product_name.split('with')[0]
	except Exception as e:
		product_name = None
		product_rating = None
		num_of_reviews = None
		product_price = None
		pass
	
	try:
		product_rating = section.find('span',class_="a-icon-alt").text
		product_rating = float(product_rating[:3])
	except Exception as e:
		product_rating = None

	try:
		num_of_reviews = section.find('span', class_="a-size-base").text 
		num_of_reviews = num_of_reviews.replace(',','')
		num_of_reviews = int(num_of_reviews)
	except Exception as e:
		num_of_reviews = None
	
	try:
		product_price = soup.find('span', class_="a-price-whole").text
		product_price = product_price.replace(',','')
		product_price = float(product_price)
	except Exception as e:
		product_price = None
	

	return product_name, product_rating, num_of_reviews, product_price

for i in range(1,11):

	driver.get(url(i))

	soup = BeautifulSoup(driver.page_source, 'html.parser')

	
	for section in soup.find_all('div', class_="a-section a-spacing-medium"):
	
		print(extraction(section))
		csv_writer.writerow(extraction(section))


csv_file.close()