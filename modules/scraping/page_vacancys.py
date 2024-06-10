from lxml import html
import requests
import chardet

def pagination(fileHtml):
    with open('vacancysPage.html', 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']

    with open(fileHtml, 'r',encoding=encoding) as file:
        site = file.read()

    tree = html.fromstring(site)

    listPages = tree.xpath('.//ul[@class="pagination"]/li/a/@href')

    nextPage = listPages[6]

    return (nextPage)

    
def get_urls_jobs(default_url, search_url):
    response = requests.get(search_url)

    # Verifique se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        print("Request sucess full")

        # Obtenha o conteúdo HTML da resposta
        html_content = response.text

        with open('vacancysPage.html', 'w') as file:
            file.write(html_content)

    else:
        print('Erro ao fazer solicitação. Código de status:', response.status_code)

    with open('vacancysPage.html', 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']

    with open('vacancysPage.html', 'r', encoding=encoding) as file:
        content = file.read()

    tree = html.fromstring(content)

    # Usar XPath para extrair os resultados
    links = tree.xpath('.//div[@class="col-md-12 notice-of-vacancy"]/h2/a/@href')

    with open('results_jobsLinks.txt', 'w') as file:
        for link in links:
             file.write((f"{default_url}{link}\n"))

    print('Links extraídos e salvos em results_jobsLinks.txt')
