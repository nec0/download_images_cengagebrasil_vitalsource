## Download de imagens de páginas de ebook
Automatize o download de imagens de ebooks do cengagebrasil/vitalsource com o framework [selenium](https://selenium-python.readthedocs.io/) e python

*Desenvolvido com o intuito de estudo, recomendamos que não comercialize ou matenha cópias não autorizadas de livros*

- - -
### O QUE FAZ?
- [x] Login e download de imagns
- [ ] Converter imagens em arquivo(.pdf)

### COMO USAR?
Instale o selenium e faça o download do chromedriver(chrome) ou geckodriver(firefox - necessário alteração no código)

#### INSTALAR O SELENIUM
```python
pip install -U selenium
```

#### VERIFICAR NÚMERO ISBN DO LIVRO
Existem duas formas:
1. Através da própria url: cengagebrasil.vitalsource.com/#/books/`9788522124015`
2. Por meio da página do livro OU internet:

![1](img/isbn.jpg)

#### NÚMERO DA PÁGINA INICIAL
Abra o ebook e com auxilio do navegador inspecione a página e encontre o iframe#epub-content:

![2](img/page.jpg)

*Veja que ali também é possível visualizar o ISBN*

### Utilize o próprio recurso(Imprimir) do Windows para transformar as imagens em PDF
Selecione todas as imagens, clique na primeira(capa) imagem com o botão direito e Imprimir, configure e salve como pdf.

### Salvando várias vezes a mesma página(capa/contracapa/etc)
Recomendo colocar um número maior de páginas, o dobro, e verificar com um tempo se já baixou a ultima página.

- - -

*Sinta-se livre para contribuir!*
