import time
# from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def screenshot_pages(email, senha, codigo_livro, nome_livro, first_page, final_page):
    browser = webdriver.Chrome()

    # login
    url = 'https://cengagebrasil.vitalsource.com/#/user/signin'

    if url == 'https://cengagebrasil.vitalsource.com/#/user/signin':
        browser.get(url)

        username = browser.find_element_by_id("email-field")
        password = browser.find_element_by_id("password-field")

        time.sleep(10)
        username.send_keys(email)
        password.send_keys(senha)

        login_second = browser.find_element_by_xpath("//*[@class='Button__buttonContent-bIKrMk KaEKF']")
        login_second.submit()

    # height pages
    time.sleep(10)

    url = 'https://jigsaw.vitalsource.com/books/{}/pages/{}'.format(str(codigo_livro),str(first_page+1))
    browser.get(url)

    time.sleep(10)

    height = browser.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight )")
    
    # browser does not open window
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,{}".format(height))
    print(height)
    chrome_options.add_argument("--hide-scrollbars")
    browser = webdriver.Chrome()
    # browser = webdriver.Chrome(options=Chrome_options)

    # salvando imagens
    page_cont = 1
    for page in range(first_page, final_page):
        url = 'https://jigsaw.vitalsource.com/books/{}/pages/{}'.format(codigo_livro, page)
        browser.get(url)
        time.sleep(8)

        browser.save_screenshot('{}.png'.format(page_cont))
        page_cont = page_cont + 1

def main(): 
    email = str(input('Senha: '))
    senha = str(input('Senha: '))
    codigo_livro = int(input('Código do livro: '))
    nome_livro = str(input('Nome do livro: '))
    first_page = int(input('Código primeira página: '))
    final_page = int(input('Código ultima página: '))

    print(screenshot_pages(email, senha, codigo_livro, nome_livro, first_page, final_page))


main()
    













