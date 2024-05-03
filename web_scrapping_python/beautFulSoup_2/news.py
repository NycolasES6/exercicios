import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('https://g1.globo.com/')

lista_noticias = []

content = response.content

site = BeautifulSoup(content, 'html.parser')

# HTML da notícia
noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
    subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})

    if subtitulo:
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '', titulo['href']])

news = pd.DataFrame(lista_noticias, columns=['titulo', 'subtitulo', 'url'])

news.to_excel('noticias4.xlsx', index=False)

print(news)
