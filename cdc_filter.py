# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 12:37:01 2017

@author: brian
"""

import re

def cdc_a1c_MLP(searchTerm, highlight):
   regex_exp_test_results = r"(\b" + re.escape(searchTerm) + r":?.{0,10}\s\d*\.?\d+)"
   regex_exp_test_range = r"(\b" + re.escape(searchTerm) + r":?.{0,10}(\d*\.)?\d+\s*-\s*(\d*\.)\d+?)"
   #result_compile = re.compile(r'(\bHbA1c:?.{0,10}\s\d*\.?\d+)', flags=re.IGNORECASE)
   result_compile = re.compile(regex_exp_test_results, flags=re.IGNORECASE)
   range_compile = re.compile(regex_exp_test_range, flags=re.IGNORECASE)
   date_compile =re.compile(r'\b[0-3]?[0-9].[0-3]?[0-9].(?:[0-9]{2})?[0-9]{2}')
   res_result = result_compile.search(highlight)
   res_range = range_compile.search(highlight)
   res_date = date_compile.search(highlight)
   if not res_result:
      return False
   elif not res_range and res_date:
      return True
   else:
      return False
  

def cdc_a1c7_MLP(searchTerm, highlight):
   regex_exp_test_results = r"(\b" + re.escape(searchTerm) + r":?.{0,10}\s\d*\.?\d+)"
   print ("regex_exp_test_results: ", regex_exp_test_results)
   regex_exp_test_range = r"(\b" + re.escape(searchTerm) + r":?.{0,10}(\d*\.)?\d+\s*-\s*(\d*\.)\d+?)"
   result_compile = re.compile(r'(\bHbA1c:?.{0,10}\s\d*\.?\d+)', flags=re.IGNORECASE)
   print ("result_compile: ", result_compile)
   range_compile = re.compile(regex_exp_test_range, flags=re.IGNORECASE)
   res_result = result_compile.search(highlight)
   print ("res_result: ", res_result)
   print ("highlight: ", highlight)
   res_range = range_compile.search(highlight)
   #res_date = date_compile.search(highlight)
   print ("res_range:", res_range)
   if not res_result:
      return False
  # res_date returns false and that is why this measure returns false
  # to fix this, stop searching for res_date
  #also, it's important to ensure that this measure actually verifies that
  #the relevant metric is less than 7.0
   elif not res_range: #and res_date:
      return True
   else:
      return False