import google.generativeai as genai

def extract_datas(texto):

    API_KEY = open('API_KEY_GEMINI').read()
    genai.configure(api_key=API_KEY)

    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])

    description = open('.\\text_files\\description.txt', encoding='utf-8').read()

    response = chat.send_message(description)
    response = chat.send_message(texto)

    return(response.text)