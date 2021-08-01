import pandas as pd
import numpy as np

## Data Imports
avl = pd.read_csv('GMU_2021_Summer_AVL.csv')
cad = pd.read_csv('GMU_2021_Summer_CAD.csv')

## Assign AVL column values
avl.columns = ['AVL_IncidentNumber',
               'AVL_UnitID',
               'AVL_Timestamp',
               'AVL_UnitStatus',
               'AVL_Speed']
avl.dropna(subset = ['AVL_IncidentNumber'],
           inplace = True)
avl.reset_index(inplace = True, drop = True)

## Merge AVL and CAD datasets
# I think doing an outer join is probably better cause then we can figure out what incidents do not have a
# corresponding record between datasets
df = avl.merge(cad, 
               how = 'outer', 
               left_on = ['AVL_IncidentNumber',
                          'AVL_UnitID'],
               right_on = ['CAD_IncidentNumber',
                           'CAD_UnitID'],
               suffixes = ('_avl', '_cad'))

# ### Inner Join Info ###
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 118648062 entries, 0 to 118648061
# Data columns (total 9 columns):
#  #   Column              Dtype 
# ---  ------              ----- 
#  0   AVL_IncidentNumber  object
#  1   AVL_UnitID          object
#  2   AVL_Timestamp       object
#  3   AVL_UnitStatus      object
#  4   AVL_Speed           object
#  5   CAD_IncidentNumber  object
#  6   CAD_UnitID          object
#  7   CAD_Timestamp       object
#  8   CAD_UnitStatus      object
# dtypes: object(9)
# memory usage: 8.8+ GB

# ### Nulls ###
# AVL_IncidentNumber    0
# AVL_UnitID            0
# AVL_Timestamp         0
# AVL_UnitStatus        0
# AVL_Speed             0
# CAD_IncidentNumber    0
# CAD_UnitID            0
# CAD_Timestamp         0
# CAD_UnitStatus        0
# dtype: int64


# ---------------------------------------------------------------------------------------------
### Outer Join Info ###
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 119181238 entries, 0 to 119181237
# Data columns (total 9 columns):
#  #   Column              Dtype 
# ---  ------              ----- 
#  0   AVL_IncidentNumber  object
#  1   AVL_UnitID          object
#  2   AVL_Timestamp       object
#  3   AVL_UnitStatus      object
#  4   AVL_Speed           object
#  5   CAD_IncidentNumber  object
#  6   CAD_UnitID          object
#  7   CAD_Timestamp       object
#  8   CAD_UnitStatus      object
# dtypes: object(9)
# memory usage: 8.9+ GB

### Nulls ###
# AVL_IncidentNumber    533176
# AVL_UnitID            533176
# AVL_Timestamp         533176
# AVL_UnitStatus        533176
# AVL_Speed             533176
# CAD_IncidentNumber         0
# CAD_UnitID                 0
# CAD_Timestamp              0
# CAD_UnitStatus             0
# dtype: int64

# print('record delta: ', 119181238 - 118648062)
# record delta:  533176
