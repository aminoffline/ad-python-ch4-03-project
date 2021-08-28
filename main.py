from bs4 import BeautifulSoup
#from Database import db, Insert_Table
import requests
import csv

table_key = ["vehicle_title","vehicle_mileage","vehicle_color","vehicle_condition","vehicle_location","vehicle_price"]
brand = 'ford'
response = requests.get(f'https://www.truecar.com/used-cars-for-sale/listings/{brand}/')

print(response, response.ok,response.url)
soup = BeautifulSoup(response.text,'lxml')
post = soup.find('div',attrs={"data-test":"cardContent"})
print(post.prettify())