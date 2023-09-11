import csv
import os
INPUT_DATA_DIR = "../input_data"

class InputDataParser:



    def __init__(self):
        self.inpu_data = []
        return

    def load_input_data(self, file_name):
        try:
            script_file_path = os.path.dirname(os.path.realpath(__file__));
            file_path = os.path.join(script_file_path,INPUT_DATA_DIR, file_name);

            with open(file_path, mode='r') as file:
                reader = csv.reader(file)
                
                # Iterate through the rows in the CSV file
                for row in reader:
                    print(row)
        except:
            print(f"Error while reading data file {file_name}")


class PersonalHearthPressureData(InputDataParser):

    def __init__(self):
        print("graphm")
        super().load_input_data('input.csv')
        return;

    def get_systolic_pressures(self, day_time_pressure = True):
        
        print(self.inpu_data)
    





