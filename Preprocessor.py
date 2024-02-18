import os
import PyPDF2
import requests

def fetch_ageandas_meetings(links):
    agendas = []
    minutes = []
    for i in links:
        if "minutes" in i:
            minutes.append(i)
        elif "agenda" in i:
            agendas.append(i)
    return agendas,minutes

def fetch_pdfs(path):
    all_files = os.listdir(path)
    pdf_files = [file for file in all_files if file.lower().endswith('.pdf')]
    return pdf_files

def download_pdf(url,path):
    pdf_filename = url[url.rfind("/")+1:]+".pdf"
    pdf_path = os.path.join(path, pdf_filename)
    response = requests.get(url)
    if response.status_code == 200:
        with open(pdf_path, 'wb') as file:
            file.write(response.content)
