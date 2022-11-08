import math
from typing import List
import numpy as np
from Component import Component

class Component_List(List):
    def __str__(self):
        str = ""
        for component in self:
            str += component.__str__()
        return str
    

# example
comp1 = Component(10)
comp2 = Component(2)
active_components = Component_List()
active_components.append(comp1)
active_components.append(comp2)

print("?")
for component in active_components:
    print(component)
    
print(active_components)
