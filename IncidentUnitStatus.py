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
               how = 'inner', 
               left_on = ['AVL_IncidentNumber',
                          'AVL_UnitID',
                          'AVL_UnitStatus'],
               right_on = ['CAD_IncidentNumber',
                           'CAD_UnitID',
                           'CAD_UnitStatus'],
               suffixes = ('_avl', '_cad'))

# ### Inner Join Info ###
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 21696754 entries, 0 to 21696753
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
# memory usage: 1.6+ GB

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
### Info ###
# <class 'pandas.core.frame.DataFrame'>
# Int64Index: 24321445 entries, 0 to 24321444
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
# memory usage: 1.8+ GB

#### Nulls ####
# AVL_IncidentNumber    2624424
# AVL_UnitID            2624424
# AVL_Timestamp         2624424
# AVL_UnitStatus        2624424
# AVL_Speed             2624424
# CAD_IncidentNumber        267
# CAD_UnitID                267
# CAD_Timestamp             267
# CAD_UnitStatus            267
