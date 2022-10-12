import pandas as pd
from difflib import SequenceMatcher
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

df1 = pd.DataFrame({'District': ['Kathmandu', 'Dhanusha', 'Kavre palanchowk'],
                    'KPI_1': [.8, .85, .75]})
df2 = pd.DataFrame({'District': ['Kathmandu', 'Kavrepalanchowk', 'Dhanusha'],
                    'KPI_2': [.35,.65,.6]})

def dist(df):
  for (column_name,column_data) in df.iteritems():
    if column_name is 'District':
      return column_data.values
dist_list1=dist(df1)
dist_list2=dist(df2)
for name1 in dist_list1:
  for name2 in dist_list2:
    if name1 == name2:
      break
    elif similar(name1,name2) > 0.9:
     df2['District']=df2['District'].replace(name2,name1)

df3 = pd.merge(df1, df2)
print(df3)

