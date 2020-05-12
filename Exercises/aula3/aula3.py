from selenium.webdriver import Firefox
from time import sleep
#open browser
browser = Firefox()

# abre a pagina da url
url = 'https://curso-python-selenium.netlify.app/aula_03.html'
browser.get(url)

# espera pra a página carregar
sleep(2)

# encontrar elemento
a = browser.find_element_by_tag_name('a')

for click in range(10):
    a.click()
    pes = browser.find_elements_by_tag_name('p')
    print('numero de clicks: ' + str(click))
    print('numero do p ' + str(pes[-1].text))
#close browser
browser.quit()
