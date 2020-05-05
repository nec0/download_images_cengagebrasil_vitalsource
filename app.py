import time
# from PIL import Image
# import img2pdf
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


def login_and_save_urls(email, senha, isbn, nome_livro, pagina_inicial, total_paginas):
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

    # abrir páginas e salvar urls da imagem
    time.sleep(3)
    browser.execute_script("window.open()")
    browser.switch_to.window(browser.window_handles[1])

    src_img = []
    for page in range(pagina_inicial, total_paginas+1):

        url = 'https://jigsaw.vitalsource.com/books/'+str(isbn)+'/pages/'+str(page)
        browser.get(url)

        # NÃO ESTÁ RETORNANDO SRC
        time.sleep(2)
        element_src = browser.find_element_by_xpath("html//body//div[@id='epub-container']//iframe[@id='epub-content']//html//body[@class='pbk']//img[@id='pbk-page']")
        print(element_src)

        src_img.append(element_src)

    # funcao download imagens
    return src_img

def main():
    email = str(input('Email: '))
    senha = str(input('Senha: '))
    isbn = int(input('ISBN: '))
    nome_livro = str(input('Nome do livro: '))  # criar pasta para salvar imagem com este nome
    pagina_inicial = 351539662  # fin.element_by ...
    total_paginas = 10
    total_paginas = (pagina_inicial + total_paginas)

    print(login_and_save_urls(email, senha, isbn, nome_livro, pagina_inicial, total_paginas))


main()