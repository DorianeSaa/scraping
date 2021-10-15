
import requests
from bs4 import BeautifulSoup

url='https://books.toscrape.com/catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html'

r = requests.get(url)
print('product_page_url :' + url)


soup = BeautifulSoup(r.text)

infos_extraites ={
	"product_page_url": "https://books.toscrape.com/catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html",
	"universal_product_code": soup.find('td'),
	"title" : soup.find('title'),
	"price_excluding_tax": soup.findAll('td')[2],
	"price_including_tax": soup.findAll('td')[3],
	"number_available" : soup.findAll('td')[5],
	"product_description" : soup.find('meta', attrs={'name':'description'}),
	"category" : soup.find('ul',{'class':'breadcrumb'}).find('li',{'class':'active'}).find_previous(),
	"review_rating" : soup.find('p', {'class': 'star-rating'}),
	"image_url" : soup.find('img')


}



print(infos_extraites)