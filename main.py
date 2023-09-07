from bs4 import BeautifulSoup
import requests as rq

html = rq.get("https://bsi.gov.in/page/en/medicinal-plant-database#").text

soup = BeautifulSoup(html,"lxml")
plant_name_tags = soup.find_all("em")
plant_order_tags = soup.find_all("td",class_ = 'text')

plant_name_scrape = str(plant_name_tags).split(",")
plant_order_scrape = str(plant_order_tags).split(",")

plant_names,plant_order = [],[]

for i in plant_name_scrape:
    formatted_names = i.replace("<em>","").replace("</em>","").replace("[","").replace("]","")
    plant_names.append(formatted_names.strip())

for j in plant_order_scrape:
    formatted_orders = j.replace('<td class="text">',"").replace("</td>","").replace("[","").replace("]","")
    if "</p>" not in formatted_orders:
        plant_order.append(formatted_orders.strip())

with open("Ayurvedic Data.csv",'a',encoding='utf-8') as file:
    for i in range(len(plant_names)):
        file.write(f"{plant_names[i]},{plant_order[i]}\n")