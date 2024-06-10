from modules.scraping import page_description, page_vacancys
from modules import gemini
import pandas as pd
import time

def engine_jobs_search(url_vancancy):
    page_description.get_text_page_job(url_vancancy)

    with open('elements_text.txt','r', encoding='utf-8') as file:
        datas_job = file.read()

    response = gemini.extract_datas(datas_job)

    return(response)

# Pasta onde os arquivos serão salvos
output_folder = "\\Users\\Iruziky\\Desktop\\respostas"

default_url = 'https://www.curriculum.com.br'
search_url = 'https://www.curriculum.com.br/candidatos/vagas-emprego/'

end_page = 'https://www.curriculum.com.brjavascript:void(0)'

columns = ['Position', 'Modality', 'Workload', 'Salary', 'State', 'City', 'Link']
df = pd.DataFrame(columns=columns)

minTimeForRequest = 15

condition = True
while condition:
    startTime = time.time()

    page_vacancys.get_urls_jobs(default_url, search_url)

    with open('results_jobsLinks.txt', 'r') as file:
        listUrls = file.read().split("\n")

    for url in listUrls:
        startTimeChild = time.time()

        try:
            jobLine = engine_jobs_search(url)
            jobLine = (jobLine + "\\t" + url).split("\\t")

            dfLine = pd.DataFrame([jobLine], columns=columns)

            df = pd.concat([df, pd.DataFrame(dfLine)], ignore_index=True)

            nextPage = default_url + page_vacancys.pagination('vacancysPage.html')        

            endTimeChild = time.time() 
            totalTimeChild = endTimeChild - startTimeChild
            print(f"Tempo decorrido para uma vaga: {totalTimeChild}\n")

            if totalTimeChild < minTimeForRequest:
                time.sleep(minTimeForRequest - totalTimeChild)

        except Exception as e:
            print("Pulando uma iteração\n")
            print(e)

            endTimeChild = time.time() 
            totalTimeChild = endTimeChild - startTimeChild
            print(f"Tempo decorrido para uma vaga: {totalTimeChild}\n")

            if totalTimeChild < minTimeForRequest:
                time.sleep(minTimeForRequest - totalTimeChild)
            continue
        
        print(df)
    
    df.to_csv('Dataframe.csv')

    nextPage = default_url + page_vacancys.pagination('vacancysPage.html')

    condition = not nextPage == end_page
    search_url = nextPage

    endTime = time.time()
    totalTime = endTime - startTime
    print(f"Tempo decorrido para uma seção de vagas: {totalTime}\n\n")

    if totalTime < minTimeForRequest:
        time.sleep(minTimeForRequest - totalTime)