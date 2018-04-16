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
   
   #res_date = date_compile.search(highlight)
   #where on the measure description does it say we need the res_date?
   if not res_result:
      return False
   elif not res_range:# and res_date:
      return True
   else:
      return False
  
#Add test cases for all the indicators, including:
#All three control cases:
      #<7%, <8%, <9%
      #Eye exam performed
      #Medical attention for nephropathy
      #BP Control
    
#evaluates for whether less than 7
def cdc_a1c7_MLP(searchTerm, highlight):
   #regex_exp_test_results = r"(\b" + re.escape(searchTerm) + r":?.{0,6}\s\d*\.?\d+)"
   regex_exp_test_results = r"(\b" + re.escape(searchTerm) + r":?.{0,10}\s[0-6]+\.?\d*)"
   regex_exp_test_range = r"(\b" + re.escape(searchTerm) + r":?.{0,10}(\d*\.)?\d+\s*-\s*(\d*\.)\d+?)"
   result_compile = re.compile(regex_exp_test_results, flags=re.IGNORECASE)
#   date_compile =re.compile(r'\b[0-3]?[0-9].[0-3]?[0-9].(?:[0-9]{2})?[0-9]{2}')
   range_compile = re.compile(regex_exp_test_range, flags=re.IGNORECASE)
   res_result = result_compile.search(highlight)
   res_range = range_compile.search(highlight)
   print ("result_compile: ", result_compile)
   print ("res_result: ", res_result)
   #res_date = date_compile.search(highlight)
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
  
#evaluates for whether less than 8
def cdc_a1c8_MLP(searchTerm, highlight):
   #regex_exp_test_results = r"(\b" + re.escape(searchTerm) + r":?.{0,6}\s\d*\.?\d+)"
   regex_exp_test_results = r"(\b" + re.escape(searchTerm) + r":?.{0,10}\s[0-7]+\.?\d*)"
   regex_exp_test_range = r"(\b" + re.escape(searchTerm) + r":?.{0,10}(\d*\.)?\d+\s*-\s*(\d*\.)\d+?)"
   result_compile = re.compile(regex_exp_test_results, flags=re.IGNORECASE)
#   date_compile =re.compile(r'\b[0-3]?[0-9].[0-3]?[0-9].(?:[0-9]{2})?[0-9]{2}')
   range_compile = re.compile(regex_exp_test_range, flags=re.IGNORECASE)
   res_result = result_compile.search(highlight)
   res_range = range_compile.search(highlight)
   print ("result_compile: ", result_compile)
   print ("res_result: ", res_result)
   #res_date = date_compile.search(highlight)
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
  
#evaluates for whether greather than 9
def cdc_a1c9_MLP(searchTerm, highlight):
   #regex_exp_test_results = r"(\b" + re.escape(searchTerm) + r":?.{0,6}\s\d*\.?\d+)"
   regex_exp_test_results = r"(\b" + re.escape(searchTerm) + r":?.{0,10}\s([9]|1[0-9])+\.?\d*)"
   regex_exp_test_range = r"(\b" + re.escape(searchTerm) + r":?.{0,10}(\d*\.)?\d+\s*-\s*(\d*\.)\d+?)"
   result_compile = re.compile(regex_exp_test_results, flags=re.IGNORECASE)
#   date_compile =re.compile(r'\b[0-3]?[0-9].[0-3]?[0-9].(?:[0-9]{2})?[0-9]{2}')
   range_compile = re.compile(regex_exp_test_range, flags=re.IGNORECASE)
   res_result = result_compile.search(highlight)
   res_range = range_compile.search(highlight)
   print ("result_compile: ", result_compile)
   print ("res_result: ", res_result)
   #res_date = date_compile.search(highlight)
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