# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 13:19:54 2022

@author: eugen
"""

%clear

from arithmetic_arranger import arithmetic_arranger
from unittest import main


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

# Run unit tests automatically
main(module='test_module', exit=False)