import requests
import time

def baixar_robots_txt(url):
    # URL do site que você deseja baixar
    url_robots = (url + "robots.txt")
    # Fazendo a requisição GET para obter o conteúdo da página
    try:
        response = requests.get(url)
    except:
        print(url)
        return 0

    # Verificando se a requisição foi bem-sucedida (código 200)
    if response.status_code == 200:
        print("Sucesso ao acessar o conteúdo da url:", url_robots, "\n")
        # Conteúdo HTML da página
        return(response.content.decode('utf-8'))
        
    else:
        print("Falha ao acessar o conteúdo HTML.")
        time.sleep(10)
        return 0

    # Delay para não fazer muitas requisições
    time.sleep(10)