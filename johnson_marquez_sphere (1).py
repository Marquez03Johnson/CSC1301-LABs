# -*- coding: utf-8 -*-
"""Johnson_Marquez_Sphere.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uU7lYfoIUYnReaOd-_s6uwRTqAjxWXQ1
"""

import math
print('Please enter the radius of the sphere:')
sphere = int(input())
volume = 4/3 * math.pi * math.pow(sphere,3)
print('The volume of a sphere with radius of', sphere, 'is' , volume)
fact_o= math.factorial (sphere)
print('The factorial of', sphere, 'is', fact_o)