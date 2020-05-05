import time
# from PIL import Image
# import img2pdf
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


def login_and_save_urls(email, senha, isbn, nome_livro, total_paginas):
    browser = webdriver.Firefox()
    
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
    for page in range(0, total_paginas+1):
        url_1 = 'https://jigsaw.vitalsource.com/books/'+str(isbn)+'/cfi/'
        url_2 = str(page)+'!/4/2@100:0.00?jigsaw_brand=cengageLearningEditoresSaDeCvBrasil&dps_on=false&xdm_e=httpsAFFcengagebrasil.vitalsource.com&xdm_c=default6767&xdm_p=1'
        url = url_1 + url_2
        urls.append(url)

    # abrir páginas e salvar urls da imagem
    time.sleep(5)
    browser.execute_script("window.open()")
    browser.switch_to.window(browser.window_handles[1])

    src_img = []
    for src in range(0, len(urls)):
        browser.get(urls[src])
        time.sleep(6)

        # NÃO ESTÁ RETORNANDO SRC
        element_src = browser.find_element_by_xpath("html//body//div[@id='epub-container']//iframe[@id='epub-content']//html//body[@class='pbk']//img[@id='pbk-page']")
        print(element_src)

        src_img.append(element_src)

    # funcao download imagens


def main():
    email = str(input('Email: '))
    senha = str(input('Senha: '))
    isbn = int(input('ISBN: '))
    nome_livro = str(input('Nome do livro: '))  # criar pasta para salvar imagem com este nome
    pagina_inicial = 351539662  # fin.element_by ...
    total_paginas = int(input('Quantidade de páginas'))
    pagina_final = int(pagina_inicial + total_paginas)

    login_and_save_urls(email, senha, isbn, nome_livro, total_paginas)


main()