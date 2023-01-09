class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
    
        stack = []
        stack.append(celsius + 273.15)
        stack.append(celsius * 1.80 + 32.00)
        return stack
