import time
# from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def login_and_save_urls(email, senha, isbn, nome_livro, total_paginas):
    browser = webdriver.Chrome()

    # login
    url = 'https://cengagebrasil.vitalsource.com/#/user/signin'

    if url == 'https://cengagebrasil.vitalsource.com/#/user/signin':
        browser.get(url)

        username = browser.find_element_by_id("email-field")
        password = browser.find_element_by_id("password-field")

        time.sleep(5)
        username.send_keys(email)
        password.send_keys(senha)

        time.sleep(5)
        btn_login = browser.find_element_by_xpath("//*[@class='Button__buttonContent-bIKrMk KaEKF']")
        btn_login.submit()

    # listar urls de páginas
    urls = []
    for page in range(0, total_paginas):
        url_1 = 'https://jigsaw.vitalsource.com/books/'+str(isbn)+'/cfi/'
        url_2 = str(page)+'!/4/2@100:0.00?jigsaw_brand=cengageLearningEditoresSaDeCvBrasil&dps_on=false&xdm_e=httpsAFFcengagebrasil.vitalsource.com&xdm_c=default6767&xdm_p=1'
        url = url_1 + url_2
        urls.append(url)

    # abrir páginas e salvar urls da imagem
    browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

    src = []
    for src in range(0, len(urls)):
        browser.get(urls[src])
        time.sleep(8)
        browser.find_element_by_xpath()  # falta conseguir isto!        

    browser.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 

def main(): 
    email = str(input('Senha: '))
    senha = str(input('Senha: '))
    isbn = int(input('ISBN: '))
    nome_livro = str(input('Nome do livro: '))
    first_page = int(input('Código primeira página: '))
    final_page = int(input('Código ultima página: '))

    print(screenshot_pages(email, senha, codigo_livro, nome_livro, first_page, final_page))


main()
    













