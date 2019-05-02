import urllib.request
import json

class CotacaoBtc(object):
	
	def __init__(self):
		self.markets            = self.getContentMarkets()
		self.currency           = ""
		self.table_currencies   = ""
		self.currencies         = set()


	# Obtém os dados de Exchanges via API, faz o parse do JSON para Objetos Python, e retorna o resultado
	def getContentMarkets(self):
		content_markets = urllib.request.urlopen("http://api.bitcoincharts.com/v1/markets.json").read()
		return json.loads(content_markets)


	# Imprime a apresentação do App
	def buildAppHeader(self):
		print()
		print("{:^70}".format("* Bem vindo a Cotação Bitcoin CLI *"))
		print()
		print("É possível realizar a consulta de cotações nas mais diversas moedas, através de seu código ISO 4217.")
		print()
		print("Segue lista das moedas disponíveis para consulta:")


	# Imprime a Listagem de Moedas Disponíveis para consulta, cada Exchange deve ter um volume transacionado maior que zero
	def buildAvailableCurrenciesList(self):
		for market in self.markets:
			if float(market["volume"]) > 0:
				self.currencies.add(market["currency"])
		for cur in self.currencies:
			self.table_currencies += " * " + cur
		print(self.table_currencies)


	# Pergunta ao usuário a moeda que quer realizar sua consulta com base no código ISO passado
	def askCurrencyCode(self):
		while True:	
			print()
			# Pede ao usuário o código ISO da moeda nacional que deseja realizar a consulta de cotação
			self.currency = (input("Digite o código ISO 4217 da moeda na qual deseja verificar a cotação, ex: USD\n>")).upper()
			if self.currency in self.currencies:
				break
			else:
				print("O código ISO deve corresponder à alguma sequência de três letras dos registros acima listados, sem os astericos")

	
	# Imprime o cabeçalho da Tabela de resultado da consulta
	def buildResultTableHeader(self):
		print("-" * 70)
		print(" {:8} | {:8} | {:8} | {:8} | {:8} | {:8}".format("Moeda", "Máxima", "Venda", "Compra", "Média", "Exchange"))
		print("-" * 70)


	# Imprime as linhas da tabela de resultado contendo dados de cada exchange, 
	# Devem ter transacionado volume maior que zero e negociarem na moeda nacional consultada
	def buildResultTableBody(self):		
		for market in self.markets:
			if market["currency"] == self.currency and float(market["volume"]) > 0:
				print(" {:8} | {:06.2f} | {:06.2f} | {:06.2f} | {:06.2f} | {:17}".format(
					self.currency,
					market["high"], 
					market["bid"], 
					market["ask"], 
					market["avg"], 
					market["symbol"]))
				print("-" * 70)

