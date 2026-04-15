import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self,arg1: int, arg2: int = None)-> int:
        if arg2 is None:
            area_of_circle = math.pi * (arg1 ** 2)
            return round(area_of_circle, 2)
        else:
            area_of_rectangle = arg1 * arg2
            return area_of_rectangle


    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
