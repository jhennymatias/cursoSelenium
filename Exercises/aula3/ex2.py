from selenium.webdriver import Chrome
from time import sleep
import re

browser = Chrome()

# acessar a pagina
url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'
browser.get(url)
sleep(1)

#busca tag a e p
a = browser.find_element_by_tag_name('a')
pes = browser.find_elements_by_tag_name('p')


while(True):
    #verifica se o p tem a mensagem de ganhous
    if re.search('Você ganhou', pes[-1].text):
        #aguarda antes de fechar o navegador
        sleep(2)
        browser.quit()
        break;

    #busca todos os p de novo
    pes = browser.find_elements_by_tag_name('p')
    # clica
    a.click()
