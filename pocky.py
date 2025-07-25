import pandas as pd
import numpy as np

exam_data = {'name': ['anastasia', 'jim', 'kate', 'dima', 'katherine', 'james', 'laura', 'poopy',
'guppy' , 'luppy'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1,3,2,3,2,3,1,1,2,1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DateFrame(exam_data , index=labels)
print("summary of the basic informationabut this dataframe and its data:")
print(df.info())