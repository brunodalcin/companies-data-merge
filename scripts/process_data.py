import json
import csv

class Data:
    def __init__(self, path, type):
        self.path = path
        self.type = type
        self.data = self.read_data()
        self.columns_name = self.get_columns()
        self.size = self.size_data()
        
    def read_json(self):
        data_json = []
        with open(self.path, 'r') as file:
            data_json = json.load(file)
        return data_json     

    def read_csv(self):
        data_csv = []
        with open(self.path, 'r') as file_csv:
            spamreader = csv.DictReader(file_csv,delimiter=',') 
            for row in spamreader:
                data_csv.append(row)
                
        return data_csv      

    def read_data(self):
        data = []
        if self.type == 'csv':
            data = self.read_csv()
        elif self.type == 'json':
            data = self.read_json()
        elif self.type == 'list':
            data = self.path
            self.path = 'list in memory'
        return data;     

    def get_columns(self): 
        return list(self.data[0].keys())   
    
    def rename_columns(self, key_mapping):
        new_data = []
        for old_dict in self.data:
            dict_temp = {}

            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_data.append(dict_temp)

        self.data = new_data
        self.columns_name = self.get_columns()

    def size_data(self):
        return len(self.data)
    
    def join(data_a,data_b):
        combined_list = []
        combined_list.extend(data_a.data)
        combined_list.extend(data_b.data)
        
        return Data(combined_list,'list')
    
    def table_transforming(self):
        data_combined_table = [self.columns_name]
        for row in self.data:
            line = []
            for columns in self.columns_name:
                line.append(row.get(columns, 'NULL'))
            data_combined_table.append(line)

        return data_combined_table   
    
    def save(self, path):
        data_combined_table = self.table_transforming()
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(data_combined_table)     