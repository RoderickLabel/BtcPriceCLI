from cotacao_btc import CotacaoBtc


def main():
	cotacao = CotacaoBtc()
	cotacao.buildAppHeader()
	cotacao.buildAvailableCurrenciesList()
	cotacao.askCurrencyCode()
	cotacao.buildResultTableHeader()
	cotacao.buildResultTableBody()


if __name__ == '__main__':
	main()