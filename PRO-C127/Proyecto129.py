import pandas as pd 

final_data=pd.read_clipboard('MergedData.csv')
final_data['mass'].astype(float)
final_data['radius'].astype(float)

final_data['mass']*0.000954588
final_data['radius']*0.102763