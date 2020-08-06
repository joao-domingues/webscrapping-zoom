from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq 
my_url = "https://www.zoom.com.br/console-de-video-game/playstation-4"
#abre a conexão
uClient = uReq(my_url)
page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("li",{"class":"item tp-default"}) 

#cria o sheet com os títulos
out_filename = "produtos.csv"
headers = "Nome,Preço \n"
f = open(out_filename, "w")
f.write(headers)


for container in containers:
	nome = container.div.a["title"]
	price_container = container.findAll("div", {"class":"price-container"})
	price = price_container[0].text.strip("( a partir de,.avaliações nenhuma,em lojas, Nenhuma avaliação, em, lojas ")
	print("nome: " + nome + "\n")
	print("preco: " + price + "\n")

	f.write(nome + ", " + price + "\n" )
f.close()
