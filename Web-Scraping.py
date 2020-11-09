import requests
import pandas as pd
from bs4 import BeautifulSoup


set_url="https://en.wikipedia.org/wiki/COVID-19_pandemic_in_India"

html_page=requests.get(set_url)


soup=BeautifulSoup(html_page.text)


##EXtracting 3rd Table from the html page 
full_table=soup.select('table.wikitable  tbody')[2]
Print(full_table)

table_head=full_table.select('tr th')
print(table_head)

table_col=[]
count=0
for ele in table_head :
  if count < 5 :
    count+=1
    column=ele.get_text(separator=' ',strip=True)
    column=column.replace(" ","_")
    #print(column)
    table_col.append(column)

print(table_col)    

table_rows=full_table.select('tr')
table_values=[]

for index,ele in enumerate(table_rows) :
  if index > 0 :
    row_list=[]
    values=ele.select('td')
    for value in values :
      row_list.append(value.text.strip())

    table_values.append(row_list)

print(table_values)      


df=pd.DataFrame(table_values,columns=table_col)
print(df)

