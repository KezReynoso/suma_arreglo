from venv import create
import numpy as np

def createList(n):
    lst = []
    for i in range(n+1):
        lst.append(i)
    return(lst)


nums = createList(99)
print(nums)

my_array = np.array(nums)

suma_de_nums = sum(my_array)
cantidad_de_nums = len(my_array)

print("Se tienen", cantidad_de_nums, "números que suman", suma_de_nums)
