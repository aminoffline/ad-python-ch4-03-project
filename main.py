from bs4 import BeautifulSoup
#from Database import db, Insert_Table
import requests
import csv

table_key = ["vehicle_title","vehicle_mileage","vehicle_color","vehicle_condition","vehicle_location","vehicle_price"]
brand = 'ford'
response = requests.get(f'https://www.truecar.com/used-cars-for-sale/listings/{brand}')

print(response, response.ok, response.url)
soup = BeautifulSoup(response.text, 'lxml')
post = soup.find('div', attrs={"data-test": "cardContent"})
heading = post.find('div', class_="vehicle-card-top")
v_maker_model = heading.find('span', class_="vehicle-header-make-model text-truncate")
v_trim = heading.find('div', attrs={"data-test": "vehicleCardTrim"})
v_year = heading.find('span', class_="vehicle-card-year font-size-1")
car_title = f'{v_maker_model.text} {v_year.text} \n{v_trim.text} '
v_mileage = post.find('div', attrs={"data-test":"vehicleMileage"})
v_color = post.find('div', attrs={"data-test": "vehicleCardColors"})
v_condition = post.find('div', attrs={"data-test": "vehicleCardCondition"})
v_location = post.find('div', attrs={"data-test":"vehicleCardLocation"})
v_price = post.find('div', attrs={"data-test":"vehicleListingPriceAmount"})

print(post.prettify())
print(car_title)
print(f"{v_mileage.text}, {v_color.text}, {v_condition.text}, {v_price.text} \n {v_location.text}")