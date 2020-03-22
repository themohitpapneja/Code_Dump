import pandas as pd
songs={'Album':["abc","fgh","xyz","uiop"],
       'Year':["122","456","545","5465"],
       'length':["21","45","54","5"]}
df=pd.DataFrame(songs)
print(df)
##df.ix[0,0]
## ix is depreciated
## noice- refer to pandas documentation-slicing ranges
## variable of the data frame
print(df[:2])