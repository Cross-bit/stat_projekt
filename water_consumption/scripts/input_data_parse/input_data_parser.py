import csv
import os
from datetime import datetime
INPUT_DATA_DIR = "../input_data"

class InputDataParser:

    def __init__(self):
        self.input_data = []
        self.input_header = None;
        return

    def load_input_data(self, file_name):
        try:
            script_file_path = os.path.dirname(os.path.realpath(__file__));
            file_path = os.path.join(script_file_path,INPUT_DATA_DIR, file_name);

            with open(file_path, mode='r') as file:
                reader = csv.reader(file)

                self.input_header = reader.__next__();
                # Iterate through the rows in the CSV file
                for row in reader:
                    self.input_data.append([el.replace(',', '.') for el in row ])
        except:
            print(f"Error while reading data file {file_name}")


class WaterConsumption(InputDataParser):


    def __init__(self):
        super().__init__();
        super().load_input_data('water_consumption_september_2022.csv')
        self.day_time_format =  "%H:%M"
        self.start_of_night_hour = datetime.strptime('23:59', self.day_time_format)
        self.end_of_night_hour = datetime.strptime('08:00', self.day_time_format)
        
    def is_record_in_day_interval(self, record_time):
        record_time_parsed = datetime.strptime(record_time, self.day_time_format);
        return record_time_parsed <= self.start_of_night_hour and record_time_parsed >= self.end_of_night_hour

    
    def get_all_data(self):
        return self.input_data
    
    def get_total_consumption_flat_block_tripple(self):
        result = []

        for row in self.input_data:
            res_row = row[0:2]
            res_row.append(sum([float(el) for el in row[4:-2]]))
            
            result.append(res_row)

            

        return result
    
    def get_flat_in_block(self, block_code = ""):
        result = []

        is_block = False
        for row in self.input_data:
            if (block_code == "" or row[1] == block_code):
                is_block = True
                result.append(int(row[0]));
            elif is_block:
                return result

        return result
    
    def get_total_consumptions(self):
        result = []

        for row in self.input_data:
            result.append(sum([float(el) for el in row[4:-2]]))

        return result

    def get_all_consumption_matrix(self, include_header = False):
        result = []

        if (include_header):
            result.append(self.input_header[4:-2])
        
        for row in self.input_data:
            result.append([float(el) for el in row[4:-2]])

        return result

    def get_consumption_in_day_flat(self, flat_number, include_header = False):
        result = []

        if (include_header):
            result.append(self.input_header[4:-2])
        
        for row in self.input_data:
            if int(row[0]) == flat_number: 
                result.append([float(el) for el in row[4:-2]])
                return result
            

    def get_consumptions_in_block(self, block_code, include_header = False):
        result = []

        if (include_header):
            result.append(self.input_header[4:-2])


        is_block = False
        for row in self.input_data:
            if (row[1] == block_code):
                is_block = True
                result.append([float(el) for el in row[4:-2]]);
            elif is_block:
                return result
            
        return result; # this is actually needed for the last block

    def get_all_flats_array(self):
        return [row[0] for row in self.input_data]
    



    





