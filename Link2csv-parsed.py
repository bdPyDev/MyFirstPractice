from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import pandas as pd
html_page = urlopen("http://www.bdjobs.com/")

soup = BeautifulSoup(html_page, "html.parser")

#for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
    #listedlink = (link.get('href'))
    #print(listedlink)

#for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    #print(link)


# To Export to csv file, we used belew code, also above code will be works ii we dont like to export to csv
links = []
for link in soup.findAll('a', attrs={'href': re.compile("^http")}):
    links.append(link.get('href'))

df = pd.DataFrame(links)
df.to_csv('dataframe.csv')

#print(df)