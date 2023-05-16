import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')
content = response.content

# Converte a classe do Site "bytes -> bs4. BeautifulSoup" para BeautifulSoup
site = BeautifulSoup(content, 'html.parser')

# Imprimir o site no padrão HTML
# print(site.prettify())

# HTML da Notícia
noticia = site.find('div', attrs={'class': 'feed-post-body'})

# Título da Notícia
titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
print(titulo)

# Subtitulo
subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
print(subtitulo.text)