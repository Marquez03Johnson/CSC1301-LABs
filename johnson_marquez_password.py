# -*- coding: utf-8 -*-
"""Johnson_Marquez_Password.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G3YVDcX9h5LTJjdgOl_KIAJppA9JCU13
"""

stronger_characters={
    'o': '0',
    'i': '1',
    'a': '@',
    'e': '3',
    'A': '4',
    'B': '8',
    's': '$',
    }
password = (input('Please Enter Your Password: '))
new_password = password
for char in new_password:
  if char in stronger_characters:
    new_password = new_password.replace(char, stronger_characters[char])
print(f'Your new strong password is:{new_password}')