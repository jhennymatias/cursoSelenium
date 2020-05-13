from selenium.webdriver import Chrome
from time import sleep
def find_by_text(browser, tag, text):
    elementos = browser.find_elements_by_tag_name(tag)
    for elemento in elementos:
        if elemento.text == text:
            return elemento


def find_by_href(browser, link):
    elementos = browser.find_elements_by_tag_name('a')
    for elemento in elementos:
        if link in elemento.get_attribute('href'):
            return elemento

browser = Chrome()

browser.get('http://selenium.dunossauro.live/aula_04_b.html')

nomes_das_caixas = ['um', 'dois', 'tres', 'quatro']

for nome in nomes_das_caixas:
    find_by_text(browser, 'div', nome).click()

for nome in nomes_das_caixas:
    sleep(0.7)
    browser.back()

for nome in nomes_das_caixas:
    sleep(0.7)
    browser.forward()
