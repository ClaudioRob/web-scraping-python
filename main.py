# importando as bibliotecas
import requests
from bs4 import BeautifulSoup

# requisição de dados e conteúdo da página
link = "https://www.google.com/search?q=salario+minimo"
requisicao = requests.get(link)
print(requisicao)
# print(requisicao.text)

site = BeautifulSoup(requisicao.text, "html.parser")
# print(site.prettify())

title = site.find('textarea')
print(title)

pesquisa = site.find_all('textarea', value="salario minimo")
print(pesquisa)