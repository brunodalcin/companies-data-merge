
import csv
import json
from process_data import Data

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# Extract data
data_company_a = Data.read_data(path_json, 'json')
data_company_b = Data.read_data(path_csv, 'csv')

# Transforming data
key_mapping ={'Nome do Item': 'Nome do Produto',
              'Classificação do Produto': 'Categoria do Produto',
              'Valor em Reais (R$)': 'Preço do Produto (R$)',
              'Quantidade em Estoque': 'Quantidade em Estoque',
              'Nome da Loja': 'Filial', 
              'Data da Venda': 'Data da Venda',
              }


print(data_company_b.columns_name)
print(data_company_a.columns_name)
joined_data = Data.join(data_company_a, data_company_b)

# Loadin data
combined_data_path = 'data_processed/combined_data.csv'
#joined_data.save(combined_data_path)