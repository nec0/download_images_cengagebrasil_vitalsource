import time

from PIL import Image
from io import BytesIO

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def url_paginas(isbn, pagina_inicial, pagina_final):
    paginas = []
    book = f"https://jigsaw.vitalsource.com/books/{isbn}"
    for page in range(pagina_inicial, pagina_final+1):
        url = f"{book}/pages/{page}"
        paginas.append(url)

    return paginas


def login(email, senha, driver):
    url = 'https://cengagebrasil.vitalsource.com/#/user/signin'

    driver.get(url)

    time.sleep(3)
    username = driver.find_element_by_id("email-field")
    password = driver.find_element_by_id("password-field")

    time.sleep(5)
    username.send_keys(email)
    password.send_keys(senha)

    time.sleep(3)
    btn_login = driver.find_element_by_xpath("//*[@class='Button__buttonContent-bIKrMk KaEKF']")
    btn_login.submit()
    time.sleep(5)


def save_screenshot(driver, largura, altura, file_name):
    driver.set_window_size(largura, altura)
    img_binary = driver.get_screenshot_as_png()
    img = Image.open(BytesIO(img_binary))
    img.save(file_name)

    print(f"{file_name} salva!")


def open_url(email, senha, lista_urls_paginas, nome_livro, largura, altura):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(chrome_options=options)

    driver.maximize_window()
    login(email, senha, driver)
    
    for page in range(0, len(lista_urls_paginas)):
        driver.get(lista_urls_paginas[page])
        time.sleep(6)
        save_screenshot(driver, largura, altura, f'{nome_livro}_{page}.png', ) 


def main():
    #  Entradas de dados:
    print("\nDOWNLOAD LIVROS DA BIBLIOTECA VITALSOURCE / CENGAGEBRASIL")
    print("Antes de tudo, leia o README para não ocorrer erros!\n")
    continuar = str(input('Continuar? sim/não\n')).upper()

    if continuar == "SIM":
        email = str(input("Email: "))
        senha = str(input("Senha: "))
        isbn = str(input("Qual o ISBN do livro: "))
        nome_livro = str(input("Identifique o livro(ex: algebra): "))
        pagina_inicial = int(input("Qual o número da página inicial, leia o README para maais detalhes: "))

        print(
            "\nRECOMENDO TESTAR AS RESOLUÇÕES ANTES DE IMPRIMIR TODAS AS PÁGINAS!\n"
            "PORTANTO, INSIRA UMA QUANTIDADE MENOR QUE 15 PARA TESTES\n")
        total_paginas = int(input('Quantidade de páginas: '))
        pagina_final = (pagina_inicial + total_paginas)

        print("\nAS PÁGINAS TEM RESOLUÇÕES DIFERENTES A DEPENDER DO LIVRO, REALIZE TESTES OU VERIFIQUE PELO HTML")
        print(
            "RESOLUÇÕES:\n"
            "[1] 800 x 1065\n"
            "[2] 1600 x 2131\n"
            "[3] 2000 x 2664\n"
            "[4] 2000 x 2888\n")

        print("Recomenamos a opção [4]")
        res = int(input("Qual resolução deseja?\nRecomendo a [4]"))

        largura, altura = 0, 0
        if res == 1:
            largura, altura = 800, 1065
        elif res == 2:
            largura, altura = 1600, 2130
        elif res == 3:
            largura, altura = 2000, 2664
        elif res == 4:
            largura, altura = 2000, 2888

        
        lista_urls_paginas = url_paginas(isbn, pagina_inicial, pagina_final)

        open_url(email, senha, lista_urls_paginas, nome_livro, largura, altura)
    
    else:
        print('LEIA O README!')
    


main()