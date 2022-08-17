#With this line we import the whole module
#import converters
#With the 2 lines below we import specific functions from the module and we can tell like would with regular functions
from converters import lbs_to_kg
from converters import kg_to_lbs
from utils import find_max
#importing modules from a package
import ecommerce.shipping
print(lbs_to_kg(120))
print(kg_to_lbs(67))
numbers = [1, 6, 60, 31, 69, 77, 88, 2, 3, 5, 87]
print(find_max(numbers))
