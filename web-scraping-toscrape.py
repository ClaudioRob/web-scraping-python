# Web Scraping de frases ditas por famosos
## Projeto que irá retornar diversas frase ditas por famosos do site https://toscrape.com/

## Criar repositório local
## Instalar o Python e suas dependências
## Criar e habilitar ambiente virtual
## Instalar Bibliotecas
## Desenvolvimento do código 

# importando bibliotecas
import requests
from bs4 import BeautifulSoup

# fazendo a requisição dos dados e conteúdo da página
pagina = requests.get('https://quotes.toscrape.com/')
dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

todas_frases = dados_pagina.find_all('div', class_="quote")

# imprime frases no formato texto
for div in todas_frases:
    # print(dados_pagina.prettify()) # retorna conteúdo html
    texto = div.find('span', class_="text").text
    print(texto)