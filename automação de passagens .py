
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

lista_companias = ["yR1fYc"]

navegador = webdriver.Chrome()

link = "https://www.google.com/travel/flights/search?tfs=CBwQAhoqEgoyMDI1LTAxLTAxag0IAhIJL20vMDIycGZtcg0IAxIJL20vMDRzaHRfGioSCjIwMjUtMDEtMzFqDQgDEgkvbS8wNHNodF9yDQgCEgkvbS8wMjJwZm1AAUgBcAGCAQsI____________AZgBAQ&hl=pt-BR&gl=BR&tcfs=UgRgAXgB"
navegador.get(link)

time.sleep(3)

for classe in lista_companias:
    try:
        elemento = navegador.find_element(By.CLASS_NAME, classe).text 
        elemento =elemento.replace('é',"e").replace('õ',"o").replace('-',"a")  
        print(f" {elemento}")
    
    except NoSuchElementException:
        print(f"Classe {classe} não encontrada.")

with open("texto.txt","w") as arquivo:
    arquivo.write(elemento)
       

