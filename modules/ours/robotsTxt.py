from bs4 import BeautifulSoup
import requests

def get_text_from_url(url):
    # Enviar uma requisição GET para a URL
    response = requests.get(url)
    
    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Criar um objeto BeautifulSoup com o conteúdo da página
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extrair todo o texto da página
        page_text = soup.get_text()
        
        return page_text
    else:
        return f"Erro ao acessar a página. Status code: {response.status_code}"
