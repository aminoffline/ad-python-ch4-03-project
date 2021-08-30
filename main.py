from bs4 import BeautifulSoup
from Database import Insert_Table, Read_all_Data
import requests
# import csv

table_name = 'cars'
table_key = ['vehicle_title', 'vehicle_mileage', 'vehicle_color', 'vehicle_condition', 'vehicle_location', 'vehicle_price']
print('Please enter vehicle Brand for example Alfa-romeo \nEntering WRONG name may cause problem ')
brand = input('>>>')
response = requests.get(f'https://www.truecar.com/used-cars-for-sale/listings/{brand}')
print(response, response.ok, response.url)

# csv_file = open('results.csv', 'w')
# csv.writer = csv.writer(csv_file)
# csv.writer.writerow(table_key)

soup = BeautifulSoup(response.text, 'lxml')
for post in soup.find_all('div', attrs={"data-test": "cardContent"})[:20]:
    try:
        heading = post.find('div', class_="vehicle-card-top")
        v_maker_model = heading.find('span', class_="vehicle-header-make-model text-truncate")
        v_trim = heading.find('div', attrs={"data-test": "vehicleCardTrim"})
        v_year = heading.find('span', class_="vehicle-card-year font-size-1")
        car_title = f'{v_maker_model.text} {v_year.text} ,{v_trim.text} '
        v_mileage = post.find('div', attrs={"data-test": "vehicleMileage"})
        v_color = post.find('div', attrs={"data-test": "vehicleCardColors"})
        v_condition = post.find('div', attrs={"data-test": "vehicleCardCondition"})
        v_location = post.find('div', attrs={"data-test": "vehicleCardLocation"})
        v_price = post.find('div', attrs={"data-test": "vehicleListingPriceAmount"})
        values = [car_title, v_mileage.text, v_color.text, v_condition.text, v_location.text, v_price.text]
      # csv.writer.writerow([car_title, v_mileage.text, v_color.text, v_condition.text, v_location.text, v_price.text])
        Insert_Table(table_name, table_key, values)
    except:
        pass

# to read from Database use section below
"""data = Read_all_Data(table_name)
for i in data:
    print(i)"""