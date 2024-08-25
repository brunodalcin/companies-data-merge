
import csv
import json

# functions
def read_json(path_json):
    data_json = []
    with open(path_json, 'r') as file:
         data_json = json.load(file)
    return data_json     

def read_csv(path_csv):
    data_csv = []
    with open(path_csv, 'r') as file_csv:
        spamreader = csv.DictReader(file_csv,delimiter=',') 
        for row in spamreader:
            data_csv.append(row)
            
    return data_csv      

def read_data(path, file_type):
    data = []
    if file_type == 'csv':
        data = read_csv(path)
    elif file_type == 'json':
        data = read_json(path)
    return data;

def get_columns(data): 
    return list(data[0].keys())

def rename_columns(data, key_mapping):
  new_csv_data = []
  for old_dict in data:
      dict_temp = {}
      for old_key, value in old_dict.items():
          dict_temp[key_mapping[old_key]] = value
      new_csv_data.append(dict_temp)    
  return new_csv_data

def size_data(data):
    return len(data)

def join(data_a,data_b):
    combined_list = []
    combined_list.extend(data_a)
    combined_list.extend(data_b)
    return combined_list

def table_transforming(data, columns_name):
    data_combined_table = [columns_name]
    for row in data:
        line = []
        for columns in columns_name:
            line.append(row.get(columns, 'NULL'))
        data_combined_table.append(line)
    return data_combined_table

def saving_data(data, path):
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# readin docs
data_json = read_data(path_json,'json')
data_csv = read_data(path_csv,'csv')

# transforming data
key_mapping ={'Nome do Item': 'Nome do Produto',
              'Classificação do Produto': 'Categoria do Produto',
              'Valor em Reais (R$)': 'Preço do Produto (R$)',
              'Quantidade em Estoque': 'Quantidade em Estoque',
              'Nome da Loja': 'Filial',
              'Data da Venda': 'Data da Venda'
              }

data_csv = rename_columns(data_csv, key_mapping)
combined_data = join(data_csv,data_json)
combined_columns = get_columns(combined_data)

#saving data
combined_data = table_transforming(combined_data, combined_columns)
saving_data(combined_data, 'data_processed/combined_data.csv')