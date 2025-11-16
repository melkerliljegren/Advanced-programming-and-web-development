import logging
import os

class InvalidTemperatureError(Exception):
    pass

class WeatherStation:
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
    
    
    def average_temperature(self, temp_list):
        self.logger.info(f"Calculating avearge of {temp_list}")
        return sum(temp_list) / len(temp_list)
    
    
    def temperature_index(self, temp_list, factor):
        try:
            if not all(isinstance(t, (int, float)) for t in temp_list):
                raise InvalidTemperatureError("All temperatures must be numbers")
        
            return self.average_temperature(temp_list) * factor + 5
        except Exception as e:
            self.logger.exception(f"Failed to compute temperature index")
            raise
       
        
    def save_report(self, index, filename, directory="reports"):
        os.makedirs(directory, exist_ok=True)
        path = os.path.join(directory, filename)
        with open(path, "w") as f:
            f.write(f"Temperature index: {index}")
        return os.path.abspath(path)
    
    
    def process_and_save(self, temps, factor, filename):
        try:
            index = self.temperature_index(temps, factor)
            path = self.save_report(index, filename)
            self.logger.info(f"Succesfully saved to {path}")
        except InvalidTemperatureError as e:
            self.logger.error(f"Invalid data: {e}")
    

station = WeatherStation()
station.process_and_save([20, 22, 24], 1.1, "today_report.txt")
