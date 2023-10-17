# it is basically template literal in JavsScript
""" 
syntax: 
name="xyz"
print(f"Hello my name is {name}") 

"""

name = "Binod"
print(f"Hello my name is{name}")

"""
if value having more decimal points we want only two decimals
use like this {price:.2f}  
"""

price = 14.6823215468
txt = f"it costs you only {price:0.2f} $"
print(txt)

"""
Docstrings are string literals that appears right after the defination of 
funcitons,classes or modules
IMP NOTE: DOCSTRINGS should be just below function name then actual function 
 code should start
"""


def randomFunc(x):
    """this is just random function to show me as docstring"""
    print(x + x)


randomFunc(5)
print(randomFunc.__doc__)  # it will display string inside function
