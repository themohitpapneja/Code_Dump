import pandas as pd
songs={'Album':["abc","fgh","xyz","uiop","abc","abc"],
       'Year':["122","456","545","5465","456","545"],
       'length':[21,45,54,5,5,5]}

data_frame=pd.DataFrame(songs)
print(data_frame)

##unique function used to find unique elements
print(data_frame['length'].unique())

## this returns true or false for each value
print(data_frame['length']>=10)
df1=data_frame[data_frame['length']>=10]
## to print data we can use the following
print(df1)

#we can also save this data frame
#D:\Users\Mohit\PycharmProjects\PythonLab\venv\Pandas
df1.to_csv('newfile.csv')
