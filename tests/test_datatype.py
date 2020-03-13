# from PrepPy import PrepPy as pp
from PrepPy import datatype

import pandas as pd
import numpy as np

test_dict = {'cat1': ['apple', None, 'pear', 'banana', 'blueberry', 'lemon'],
             'num1': [0, 1, 2, 3, 4, 5],
             'cat2': [True, False, False, True, False, None],
             'num2': [0, 16, 7, None, 10, 14],
             'num3': [0.5, 3, 3.9, 5.5, 100.2, 33]}

test_data = pd.DataFrame(test_dict)

def test_datatype1():
    assert datatype.data_type(test_data)[0].equals(test_data[['num1', 'num2', 'num3']])
    
def test_datatype2():
    assert datatype.data_type(test_data)[1].equals(test_data[['cat1', 'cat2']])