import bs4
import requests

search = requests.get('https://escueladirecta-blog.blogspot.com/2022/11/que-significa-if-name-main.html')
soup = bs4.BeautifulSoup(search.text, 'lxml')

special_text = soup.select('b')[3].getText()
print(special_text)

lateral = soup.select('.sidebar-container article')
for p in lateral:
    print(p.getText())

img = soup.select('img')[1]['src']
imagen = requests.get(img)
f = open('imagen.jpg', 'wb')
f.write(imagen.content)
f.close()
