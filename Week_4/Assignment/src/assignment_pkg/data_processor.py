import logging
import os

class InvalidInputError(Exception):
    """Raised when input values are invalid"""
    pass


class DataProcessor:
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
    
    def add_values(self, a: int, b: int) -> int:
        """Return the sum of two integers"""
        if not isinstance(a, int) or not isinstance(b, int):
            self.logger.exception("Invalid input detected")
            raise InvalidInputError("Inputs must be integers")
        return a + b
    
    
    def multiply_and_add(self, a: int, b: int, multiplier: int) -> int:
        """Call add_values() and multiply the result"""
        self.logger.info(
            "Running multiply_and_add with values a=%d, b=%d, multiplier=%d", 
            a, b, multiplier
        )
        return multiplier * (self.add_values(a, b))
    
    
    def save_result(self, result: int, filename: str) -> str:
        """Saving the results to a file inside a folder called results"""
        
        # Finding the folder I want to save the results in
        base_dir = os.path.dirname(os.path.abspath(__file__))
        src_dir = os.path.dirname(base_dir)                        
        assignment_dir = os.path.dirname(src_dir)
    
        # Creating folder
        results_dir = os.path.join(assignment_dir, "results")
        os.makedirs(results_dir, exist_ok=True)
        path = os.path.join(results_dir, filename)
        
        # Opening the file in the created folder
        with open(path, "w") as f:
            f.write(str(result))
        
        # Gathering the full path to the saved file
        abs_path = os.path.abspath(path)
        self.logger.info(f"Results saved {abs_path}")
        
        return abs_path
    
processor = DataProcessor()
path = processor.save_result(42, "output.txt")
print(path)