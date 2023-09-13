import csv
import os
from datetime import datetime
INPUT_DATA_DIR = "../input_data"

class InputDataParser:

    def __init__(self):
        self.inpu_data = []
        self.input_header = None;
        return

    def load_input_data(self, file_name):
        try:
            script_file_path = os.path.dirname(os.path.realpath(__file__));
            file_path = os.path.join(script_file_path,INPUT_DATA_DIR, file_name);

            with open(file_path, mode='r') as file:
                reader = csv.reader(file)

                self.input_header = file.readline()
                # Iterate through the rows in the CSV file
                for row in reader:
                    self.inpu_data.append(row)
        except:
            print(f"Error while reading data file {file_name}")


class PersonalHearthPressureData(InputDataParser):


    def __init__(self):
        super().__init__();
        super().load_input_data('blood_pres_avg.csv')
        self.day_time_format =  "%H:%M"
        self.start_of_night_hour = datetime.strptime('23:59', self.day_time_format)
        self.end_of_night_hour = datetime.strptime('08:00', self.day_time_format)
        
    def is_record_in_day_interval(self, record_time):
        record_time_parsed = datetime.strptime(record_time, self.day_time_format);
        return record_time_parsed <= self.start_of_night_hour and record_time_parsed >= self.end_of_night_hour

    def __get_data_value(self, value_index, day_time_pressure = True):
        result = []
        for row in self.inpu_data:
            record_time = row[0]

            is_record_in_day = self.is_record_in_day_interval(record_time);

            if (day_time_pressure and not is_record_in_day): # skip the night
                continue
            elif (not day_time_pressure and is_record_in_day): # skip the day
                continue;
            
            measurement = row[value_index]

            result.append(int(measurement))
        
        return result
    

    def get_systolic_pressures(self, day_time_pressure = True):
        return self.__get_data_value(1, day_time_pressure)
    
    def get_dyastolic_pressures(self, day_time_pressure = True):
        return self.__get_data_value(2, day_time_pressure)



    





