# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 14:05:31 2024

@author: admin
"""

import matplotlib.pyplot as plt
catogories=['0-10','10-20','20-30','30-40','40-50']
values=[55,48,25,68,90]
plt.bar(catogories,values,color='skyblue')
plt.xlabel('overs')
plt.ylabel('runs')
plt.title('bar plot showing runs scored in an odi match')
plt.show()
