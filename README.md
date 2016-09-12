import MySQLdb as mdb
import pandas.io.sql as sql
from pandas import *
import numpy
import seaborn
import matplotlib.pyplot as plt
import pandas.io.sql as psql

data = pandas.read_csv("/Users/Tedd...../nesarc_pds.csv")
>>> (data)
43093
>>> columns
3008
>>> print (ls)

 ETHRACE2A ETOTLCA2  IDNUM   PSU  STRATUM       WEIGHT  CDAY  CMON  CYEAR  \
0          5               1  4007      403  3928.613505    14     8   2001   
1          5   0.0014      2  6045      604  3638.691845    12     1   2002   

   REGION      ...       SOL12ABDEP  SOLP12ABDEP  HAL12ABDEP  HALP12ABDEP  \
0       4      ...                0            0           0            0   
1       4      ...                0            0           0            0   


>>>

count  43093.000000  43093.000000  43093.000000  43093.000000  43093.000000   
mean       0.018634      0.095027      0.000348      0.004618      0.000093   
std        0.186201      0.383204      0.030082      0.106426      0.015233   
min        0.000000      0.000000      0.000000      0.000000      0.000000   
25%        0.000000      0.000000      0.000000      0.000000      0.000000   
50%        0.000000      0.000000      0.000000      0.000000      0.000000   
75%        0.000000      0.000000      0.000000      0.000000      0.000000   
max        3.000000      3.000000      3.000000      3.000000      3.000000  
means.plot()
