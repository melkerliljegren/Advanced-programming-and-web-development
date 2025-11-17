from assignment_pkg.data_processor import DataProcessor
import os

def test_multiply_and_add(sample_numbers):
    """Testing the function"""
    processor = DataProcessor()
    assert processor.multiply_and_add(sample_numbers["a"], sample_numbers["b"], sample_numbers["multiplier"]) == sample_numbers["expected"]
    
    
def test_multiply_and_add_uses_add_values(monkeypatch):
    """Making sure that the function calls add_values()"""
    processor = DataProcessor()
    called = {"count": 0, "args": None}
    
    
    def fake_add(a, b):
        """Implementing a fake add_values()"""
        called["count"] += 1
        called["args"] = (a, b)
        return 5 # Pretending that values add up to 5
    
    
    monkeypatch.setattr(processor, "add_values", fake_add) # Changing add_values to fake_add()
    result = processor.multiply_and_add(2, 3, 4)
    
    # making sure add_values() been called correct
    assert called["count"] == 1
    assert called["args"] == (2, 3)
    assert result == 5 * 4
    

def test_full_integration(sample_numbers):
    """Making sure that all class methods works together"""
    processor = DataProcessor()
    
    # Counting result with multiply_and_add
    result = processor.multiply_and_add(
            sample_numbers["a"], 
            sample_numbers["b"], 
            sample_numbers["multiplier"]
        )
    
    # Saving result
    path = processor.save_result(result, "integration_test_output.txt")
    
    # Making sure saved file exists
    assert os.path.exists(path)
    
    # Checking that the content in the file matches our result
    with open(path, "r") as f:
        content = f.read().strip()
    assert content == str(result)