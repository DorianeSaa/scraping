import requests
from bs4 import BeautifulSoup





url='https://books.toscrape.com/catalogue/category/books/default_15/index.html'  

r = requests.get(url)
print('product_page_url :' + url)

soup = BeautifulSoup(r.text)

# title = soup.find('title')
# print(title.text)

results = soup.find('form', {'class':'form-horizontal'})

print(results)



# lien des catégogory

linko=[]
lin=[]

for a in soup.find('ul',{'class':'nav nav-list'}).findAll('a', href=True):
	linko = a['href'].replace('../','')
	lin.append('https://books.toscrape.com/catalogue/category/books/' + linko)

print(lin)