import requests
from bs4 import BeautifulSoup
# appeler une fonction de recuperation d'un livres
from fonction import Visite_d_une_page

link = []
links=[]


url='https://books.toscrape.com/catalogue/category/books/default_15/index.html'  

r = requests.get(url)
# print('product_page_url :' + url)

soup = BeautifulSoup(r.text)

# appeler une fonction de recuperation d'un livres





catego = soup.find('ul',{'class':'breadcrumb'})
print(catego.text)



entete = soup.find('div', {'class':"col-sm-8 h1"})
print(entete.text)



# link=[]
# lin=[]

# for a in soup.find('ul',{'class':'nav nav-list'}).findAll('a', href=True):
# 	link = a['href'].replace('../','')
# 	lin.append('https://books.toscrape.com/catalogue/category/books/' + link )

# print(lin)


for a in soup.find('ul',{'class':'nav nav-list'}).findAll('a', href=True):

	print(a.text)



results = soup.find('form', {'class':'form-horizontal'})

print(results.text)

warning = soup.find('div', {'class': 'alert alert-warning'})
print(warning.text)





# parcourir les differentes pages d'une catégorie

# nbre=152
# nbre_page=(int(nbre/20))
# if (nbre%20 !=0):

# 	print(nbre_page +1)

# for i in range(nbre_page):
# 	print('https://books.toscrape.com/catalogue/category/books/default_15/page-' +str(i))




# lien des livres des pages d'une caegory


for a in soup.find('section').find_all('a',href=True):
	link = a['href'].replace('../','')

	links.append('https://books.toscrape.com/catalogue/' + link  )


	print(links)



# page2= soup.find('li', {'class' : 'next'}).find('a')
# print(page2)

r = requests.get('https://books.toscrape.com/catalogue/category/books/default_15/page-2.html')


soup = BeautifulSoup(r.text)
for b in soup.find('section').find_all('a',href=True):
	link = b['href'].replace('../','')

	links.append('https://books.toscrape.com/catalogue/' + link  )


	print(links)




# 	r = requests.get('https://books.toscrape.com/catalogue/category/books/default_15/page-3.html')


# soup = BeautifulSoup(r.text)
# for b in soup.find('section').find_all('a',href=True):
# 	link = b['href'].replace('../','')

# 	links.append('https://books.toscrape.com/catalogue/' + link  )


# 	print(links)


# r = requests.get('https://books.toscrape.com/catalogue/category/books/default_15/page-4.html')


# soup = BeautifulSoup(r.text)
# for b in soup.find('section').find_all('a',href=True):
# 	link = b['href'].replace('../','')

# 	links.append('https://books.toscrape.com/catalogue/' + link  )


# 	print(links)


# r = requests.get('https://books.toscrape.com/catalogue/category/books/default_15/page-5.html')


# soup = BeautifulSoup(r.text)
# for b in soup.find('section').find_all('a',href=True):
# 	link = b['href'].replace('../','')

# 	links.append('https://books.toscrape.com/catalogue/' + link  )


# 	print(links)



# 	r = requests.get('https://books.toscrape.com/catalogue/category/books/default_15/page-6.html')


# soup = BeautifulSoup(r.text)
# for b in soup.find('section').find_all('a',href=True):
# 	link = b['href'].replace('../','')

# 	links.append('https://books.toscrape.com/catalogue/' + link  )


# 	print(links)


# 	r = requests.get('https://books.toscrape.com/catalogue/category/books/default_15/page-7.html')


# soup = BeautifulSoup(r.text)
# for b in soup.find('section').find_all('a',href=True):
# 	link = b['href'].replace('../','')

# 	links.append('https://books.toscrape.com/catalogue/' + link  )


# 	print(links)







