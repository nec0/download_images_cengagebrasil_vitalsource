    # # height pages (método alternativo - screenshot)
    # time.sleep(10)

    # url = 'https://jigsaw.vitalsource.com/books/{}/pages/{}'.format(str(codigo_livro),str(first_page+1))
    # browser.get(url)

    # time.sleep(10)

    # height = browser.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight )")
    
    # # browser does not open window
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--window-size=1920,{}".format(height))
    # print(height)
    # chrome_options.add_argument("--hide-scrollbars")
    # browser = webdriver.Chrome()
    # # browser = webdriver.Chrome(options=Chrome_options)

    # # salvando imagens
    # page_cont = 1
    # for page in range(first_page, final_page):
    #     url = 'https://jigsaw.vitalsource.com/books/{}/pages/{}'.format(codigo_livro, page)
    #     browser.get(url)
    #     time.sleep(8)

    #     browser.save_screenshot('{}.png'.format(page_cont))
    #     page_cont = page_cont + 1