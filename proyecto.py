import bs4
import requests

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

# lista de titulos con 4 o 5 estrellas
title_rating = []

# iterar paginas
for page in range(1, 51):

    # crear sopa en cada pagina
    page_url = base_url.format(page)
    search = requests.get(page_url)
    soup = bs4.BeautifulSoup(search.text, 'lxml')

    # seleccionar datos de los libros
    books = soup.select('.product_pod')

    # iterar libros
    for book in books:

        # chequear que tengan 4 o 5 estrellas
        if len(book.select('.star-rating.Four')) != 0 or len(book.select('.star-rating.Five')) != 0:

            # guardar titulo en variable
            title = book.select('a')[1]['title']

            # agregar libro a la lista
            title_rating.append(title)

# ver libros 4 u 5 estrellas en consola
for t in title_rating:
    print(t)
