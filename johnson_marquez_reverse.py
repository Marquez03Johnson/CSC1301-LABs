# -*- coding: utf-8 -*-
"""Johnson_Marquez_reverse.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iFNsqZSZog3MLRTLLxWzpq0vU14HnMjp
"""

while True:
  line_text = input('Please Enter Your String:')
  if line_text.lower() in {'q', 'quit'}:
    print('Session Ended')
    break
else:
  reversed_text= line_text[::-1]
  print('Reversed:',reversed_text)