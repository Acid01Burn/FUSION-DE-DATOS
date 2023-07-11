from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page=requests.get(START_URL)

BeautifulSoup=BeautifulSoup(page.text,'html.parse')
star_table=BeautifulSoup.find_all('table', {"class":"wikitable sortable"})
total_table=len(star_table)

temp_list=[]
table_rows=star_table[1].find_all('tr')

for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)

start_names=[]
distance=[]
mass=[]
radius=[]

print(temp_list)

for i in range(1,len(temp_list)):
    start_names.append(temp_list[i][0])
    distance.append(temp_list[i][5])
    mass.append(temp_list[i][7])
    radius.append(temp_list[i][8])

headers=['start-name','distance','mass','radius']
dwarf_start=pd.DataFrame(list(zip(start_names,distance,mass,radius,)),columns=['star_name','distance','mass','radius'])
print(dwarf_start)
dwarf_start.to_csv('dwarf_stars-scraped_data.csv',index=True,index_label="id")
print("Creado exitosamente el csv")