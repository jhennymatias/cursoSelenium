from selenium.webdriver import Chrome

browser = Chrome()
url     = 'http://selenium.dunossauro.live/aula_04_b.html'
browser.get(url)

# busca a primeira ul
lista_n = browser.find_element_by_tag_name('ul')

#busca todos os li
lis     = lista_n.find_elements_by_tag_name('li')

#busca do primeiro li busca tag a e seu texto
a_name  = lis[0].find_element_by_tag_name('a').text
