from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
driver = webdriver.Chrome()
driver.get('https://www.mestoreatacado.com.br/categoria/4928607/relogios-e-smartwatch/')

titulos = driver.find_elements(By.XPATH,"//div[@class='nomeProduto']")
precos = driver.find_elements(By.XPATH,"//div[@class='boxPrecosProduto']")

workbook = openpyxl.Workbook()
workbook.create_sheet('produtos')
sheet_produtos = workbook['produtos']
sheet_produtos['A1'].value = 'Produtos'
sheet_produtos['B1'].value = 'Preços'


for titulo , preco in zip(titulos,precos):
     sheet_produtos.append([titulo.text,preco.text])
workbook.save('produtos.xlsx')


  
   