import requests
from bs4 import BeautifulSoup



url='https://books.toscrape.com/catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html'

r = requests.get(url)
print('product_page_url :' + url)


soup = BeautifulSoup(r.text)

title = soup.find('title')
print(title.text)

tds = soup.findAll('td')[2]
print(tds)


# print(tds[0].text)  
# POUR AFFICHER UN ELEMENT PRECIS on met son indice a la fin de son appel ex: soup.find('td')[0]
# [print (td.text + '\n\n') for td in tds]




image = soup.find('img')
# print(image.attrs['src'])

# description = soup.find("meta", attrs={"name":'description'})

description = soup.find("div", {'id': 'product_description'}).find_next("p")

print(description)


review_rating = soup.find('p', {'class': "star-rating Three"})
links = []

links.append("star-rating Three")

print(links)

# books = 'https://books.toscrape.com/catalogue/category/books_1/index.html'
# print(requests.get(books))

cat = soup.find('ul',{'class':'breadcrumb'}).find('li',{'class':'active'}).find_previous()


print(cat)


# books = soup.find('a',{'href':'https://books.toscrape.com/catalogue/category/books_1/index.html'})

# print(books)







     

                

                
