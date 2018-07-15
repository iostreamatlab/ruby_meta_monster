
#coding:utf8

import requests
from bs4 import BeautifulSoup
import csv
from collections import Counter

num=2
page = requests.get("http://www.obayashi.co.jp/english/works/location.php?location_id=5&location=Japan&eng_country_name=Japan&p="+str(num))
soup = BeautifulSoup(page.content, 'html.parser')


table=soup.find_all("h3")

obayashi_name="" #项目名称
obayashi_details="" #施工单位＋竣工日期＋城市


f=open('table.csv','w')
csv_writer=csv.writer(f)


for name in table:
	obayashi_name=name.get_text().strip()
	obayashi_details=name.find_next_sibling().get_text().strip()
	print(obayashi_name)
	print(obayashi_details)
	print("****************************************************************************")
	csv_writer.writerow([ x.encode('utf-8') for x in [obayashi_name,obayashi_details]])

f.close()











# for tr in table.find_all("tr"):
# 	for td in tr.find_all("td"):
		
# 		print(td.get_text().strip())
# for name in table.find_all("a"):
# 	cells=name.get_text().strip()
# 	print(cells)

#print(table)

# for tr in table.find_all("tr"):
# 	cells=tr.find_all("td")
# 	high=cells[5].get_text().strip()
# 	low=cells[2].get_text().strip()
# 	excess=cells[6].get_text().strip()
# 	print "Added {0} {1} {2} to the list".format(high,low,excess)




# pp=table.find_all("tr")[3].find_all("td")[3].get_text()
# print(pp)

# for table_row in table.find('tr'):
#     # Each tr (table row) has three td HTML elements (most people 
#     # call these table cels) in it (first name, last name, and age)
#     cells = table_row.find('td')

#     # Our table has one exception -- a row without any cells.
#     # Let's handle that special case here by making sure we
#     # have more than zero cells before processing the cells
#     if len(cells) > 0:
#         # Our first name seems to appear in the second td element
#         # that ends up being the cell called 1, since we start
#         # counting at 0
#         NitrogenFertilizers = cells[0].text.strip()
#         # Our last name is in the first (0 if we start counting 
#         # at 0 like we do in Python td element we encounter
#         Analysis = cells[1].text.strip()
#         # Age seems to be in the last td in our row
#         Nitrogen = cells[2].text.strip()

#         # Let's add our inmate to our list in case
#         # We do this by adding the values we want to a dictionary, and 
#         # appending that dictionary to the list we created above
#         inmate = {'NitrogenFertilizers': NitrogenFertilizers, 'Analysis': Analysis, 'Nitrogen': Nitrogen}
#         inmates_list.append(inmate)

#         # Let's print our table out.
#         print "Added {0} {1}, {2}, to the list".format(NitrogenFertilizers, Analysis, Nitrogen)



# seven_day = soup.find(id="seven-day-forecast")
# forecast_items = seven_day.find_all(class_="tombstone-container")
# tonight = forecast_items[0]

# period = tonight.find(class_="period-name").get_text()
# short_desc = tonight.find(class_="short-desc").get_text()
# temp = tonight.find(class_="temp").get_text()

# print(period)
# print(short_desc)
# print(temp)

