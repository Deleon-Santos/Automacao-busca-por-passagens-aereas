"""Esta aplicação atomatiza um processo de pesquisa por passagens aereas, o projeto foi copiado do canal hashtag e otimizado para 
para correção de erros, incersão de multiplas entradas e armazenamento em doc.txt"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

lista_companias = ['yR1fYc','A8qKrc','uVdL1c','uj4xv']

navegador = webdriver.Chrome()

link = "https://www.google.com/travel/flights/search?tfs=CBwQAhoqEgoyMDI1LTAxLTAxag0IAhIJL20vMDIycGZtcg0IAxIJL20vMDRzaHRfGioSCjIwMjUtMDEtMzFqDQgDEgkvbS8wNHNodF9yDQgCEgkvbS8wMjJwZm1AAUgBcAGCAQsI____________AZgBAQ&hl=pt-BR&gl=BR&tcfs=UgRgAXgB"
navegador.get(link)

time.sleep(3)

for classe in lista_companias:
    try:
        elemento = navegador.find_element(By.CLASS_NAME, classe).text 
        elemento =elemento.replace('é',"e").replace('õ',"o").replace(' – ',"a").replace(' – ',"a") 
        print(f"\nClasse '{classe}' encontrada:\n {elemento}")
      
        
    except NoSuchElementException:
        print(f"Classe {classe} não encontrada.")

with open("texto.txt","a" ,encoding="utf-8") as arquivo:
    arquivo.write(elemento)
       

#mxvQLc ceis6c uj4xv uVdL1c A8qKrc
#mxvQLc ceis6c uj4xv uVdL1c A8qKrc