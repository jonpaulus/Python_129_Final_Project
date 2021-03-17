import numpy as np
import pandas as pd

#assemble sample dataset containing year of manufacture of ford vechiles
#and a total count of recalls

#use a dictionary to represent columns / series as the keys
#row  data contain in a list like structure as the values
# 
recalls = {'tot_recalls' : [34,67,89, 120,56], 'severe_recalls' :[13,40,64,None,40], 'model':['focus', 'ranger', 'f-150', None, None] }


df = pd.DataFrame(recalls)

df.describe

 