from lxml import html
import requests
import chardet
import re

def get_html_page_job(url):
    response = requests.get(url)
 
    # Verificando se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Obtendo o conteúdo HTML da resposta
        html_content = response.text

        with open('jobPage.html', 'w') as file:
            file.write(html_content)

    else:
        print('Erro ao fazer solicitação. Código de status:', response.status_code)
        return (False)

    return (True)

def get_text_page_job(url):
    if not get_html_page_job(url):
        return (False)

    with open('jobPage.html', 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']

    with open('jobPage.html', 'r', encoding=encoding) as file:
        content = file.read()

    tree = html.fromstring(content)

    # Usando XPath para extrair os resultado
    description = tree.xpath('.//div[@class="col-md-12 notice-of-vacancy notice-of-vacancy-preview"]')

    # Extraindo o texto dos elementos e salvando em um arquivo
    with open('elements_text.txt', 'w', encoding='utf-8') as file:
        for element in description:
            text_content = element.text_content().strip().replace("  ", "")

            # Substituindo múltiplas quebras
            cleaned_text = re.sub(r'\n\n', '\n', text_content)
            cleaned_text = re.sub(r'\n\n\n+', '\n\n', cleaned_text) 

            file.write(f"{cleaned_text}\n")
            print("escreveu hem!")