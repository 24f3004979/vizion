# Loading Dataset

User Enters the file -> sends to the server -> data loader -> preprocess and cleaning interface

**1. Data Loading flow**
+ Load into one unified data frame as source information
+ Internal auto pipeline initiates with user verified report on cleaning plan

**2. Initial Data processes**

Needs to work out making flow with editing and fetch information from the source dataset
with working round trip workflow with the dataset.

+ Version for editing and further process passing
+ Fetch utilities works into directed source of truth
+ Editing tools require to mentain version for rollback


## Data clearing techniques

Fixing missing values
1. Approximate dataset --> file new feature containing info about data presense

2. One Hot encoding
encoding three cities
is_delhi, is_chennai, is_mumbai
delhi, 1, 0, 0
chennai
mumbai
... Such way 

2. Ordinal encoding

make basic, pro, premium -> 1,2,3

One hot encoding categorical compression
+ With onehot we can group rare stuff into one category,
and bunch up the other into one.

----
Numerical Dataset insights

+ Age and income two features
we would apply scaller to both of the columns
with XGBoost and other models we can ignore the scalling
+ With KNN / SVM [ preprocessing is critical to be used with]

    - Standard scaller, skwed with outlier with depended into mean
    - MinMax scaller: 0 -1
    - Robust Scaler : Takes min, mean, max | robust to outlier

+ Histogram , bix plot to know about outlier
+ Fixing with using cap into the core graph for considering dataset into consideration

+ with skwed datapoints use log transformation
How to do log transformation ?
