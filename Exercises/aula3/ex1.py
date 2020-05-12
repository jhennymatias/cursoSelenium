from selenium.webdriver import Chrome
from time import sleep
browser = Chrome()

# acessar a pagina
url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
browser.get(url)
sleep(1)

#para armazenar o primeiro dict
dic = {}
# usei para criar uma lista de tuplas
new_p =[]

#procura todas as tags p da pagina
pes = browser.find_elements_by_tag_name('p')

# salva os valores de textos das tags p e cria tuplas
for p in range(3):
    new_p.append(('texto'+ str(p+1), pes[p].text))

# criar dict, os dados de new_p precisam ser uma tupla para o construtor funcionar
dic = dict(new_p)

#cria dict final, com h1 como chave
dicFinal = {'h1': dic}

#mostra resultado
print(dicFinal)

#close browser
browser.quit()
