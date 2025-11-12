class DataProcessor:
    
    def add_values(self, a: int, b: int) -> int:
        return a + b
    
    
    def multiply_and_add(self, a: int, b: int, multiplier: int) -> int:
        return multiplier * (self.add_values(a,b))