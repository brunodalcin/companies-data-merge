
import csv
import json

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

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

data_json = read_data(path_json,'json')
print(data_json)

# data_csv = read_data(path_csv,'csv')
# print(data_csv)