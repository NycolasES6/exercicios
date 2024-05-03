import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# HTML da notícia
noticia = site.find('div', attrs={'class': 'feed-post-body'})

# Título
titulo = site.find('span', attrs={'class': 'feed-post-header-chapeu'})

# Subtítulo
sub_titulo = noticia.find('a', attrs={'class': 'feed-post-link'})


print(sub_titulo.prettify())
