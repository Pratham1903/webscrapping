from bs4 import BeautifulSoup
import requests

main_url = "https://en.wikipedia.org/wiki/A._P._J._Abdul_Kalam"

req = requests.get(main_url)
soup = BeautifulSoup(req.text, "html.parser")

title = soup.find("table", class_="infobox vcard")

data={}
for row in title.find_all('tr'):
    for rows in row.find_all('th'):
        for cols in row.find_all('td'):
            data[rows.text]=cols.text
            print(data)


