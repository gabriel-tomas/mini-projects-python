import pandas as pd
arquivo = 'project12/Vendas.xlsx'
#dic = {'produto':['Sapato', 'Calça'],
#'valor':[24.23, 55.20],
#'parcelado/avista':['Sim', 'Não'],
#'valor final': ['24.23 / 2', '55.20']
#}
dados_dtf = pd.read_excel(arquivo)
describe = dados_dtf.describe()
produtos = dados_dtf['ID Loja']
print(dados_dtf.loc[[dados_dtf['Produto'] == 'Camiseta'], dados_dtf['ID Loja'] == 'Shopping Recife'])
